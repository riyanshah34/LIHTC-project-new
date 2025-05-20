import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from tqdm import tqdm
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from functools import partial
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# Importing score classes 
from aggregate_scoring import (
     CommunityTransportationOptions,
     DesirableUndesirableActivities,
     QualityEducation,
     StableCommunities
)

# Defining Grid Parameters
lon_min, lon_max = -84.911059, -83.799104
lat_min, lat_max = 33.256500, 34.412590
step = 0.01

lats = np.arange(lat_min, lat_max, step)
lons = np.arange(lon_min, lon_max, step)
lat_lon_pairs = [(lat, lon) for lat in lats for lon in lons]

# Load in Datasets

# --- CommunityTransportationOptions ---
df_transit = pd.read_csv(os.path.join(PROJECT_ROOT, "data/raw/scoring_indicators/community_trans_options_sites/georgia_transit_locations_with_hub.csv"))

# --- DesirableUndesirableActivities ---
rural_gdf = gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/USDA_Rural_Housing_by_Tract_7054655361891465054/USDA_Rural_Housing_by_Tract.shp")).to_crs("EPSG:4326")
rural_union = rural_gdf.unary_union

csv_desirable = pd.read_csv(os.path.join(PROJECT_ROOT, "data/processed/scoring_indicators/desirable_undesirable_activities/desirable_activities_google_places_v3.csv"))
csv_usda = pd.read_csv(os.path.join(PROJECT_ROOT, "data/raw/scoring_indicators/desirable_undesirable_activities/usda/food_access_research_atlas.csv"), dtype={'CensusTract': str})
tract_shape = gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/tl_2024_13_tract/tl_2024_13_tract.shp"))
csv_undesirable = pd.read_csv(os.path.join(PROJECT_ROOT, "data/processed/scoring_indicators/desirable_undesirable_activities/undesirable_hsi_tri_cdr_rcra_frs_google_places.csv"))

# --- QualityEducation ---
df_school = pd.read_csv(os.path.join(PROJECT_ROOT, "data/processed/scoring_indicators/quality_education_areas/Option_C_Scores_Eligibility_with_BTO.csv"))
gdf_school_boundaries = [
    gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/quality_education/Administrative.geojson")).to_crs("EPSG:4326"),
    gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/quality_education/APSBoundaries.json")).to_crs("EPSG:4326"),
    gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/quality_education/DKE.json")).to_crs("EPSG:4326"),
    gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/quality_education/DKM.json")).to_crs("EPSG:4326"),
    gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/quality_education/DKBHS.json")).to_crs("EPSG:4326")
]

# --- StableCommunities ---
df_indicators = pd.read_csv(os.path.join(PROJECT_ROOT, "data/processed/scoring_indicators/stable_communities/stable_communities_2024_processed_v3.csv"))
shp_tract = gpd.read_file(os.path.join(PROJECT_ROOT, "data/raw/shapefiles/tl_2024_13_tract/tl_2024_13_tract.shp")).to_crs("EPSG:4326")



# Defining kwargs for scoring classes
kwargs = {
    # --- CommunityTransportationOptions ---
    "transit_df": df_transit,

    # --- DesirableUndesirableActivities ---
    "rural_gdf_unary_union": rural_union,
    "desirable_csv": csv_desirable, 
    "grocery_csv": csv_desirable,
    "usda_csv": csv_usda,
    "tract_shapefile": tract_shape,
    "undesirable_csv": csv_undesirable,

    # --- QualityEducation ---
    "school_df": df_school,
    "school_boundary_gdfs": gdf_school_boundaries,       
    "state_avg_by_year": {
        "elementary": {
            2018: 77.8,
            2019: 79.9
        },
        "middle": {
            2018: 76.2,
            2019: 77
        },
        "high": {
            2018: 75.3,
            2019: 78.8
        }
    },

    # --- StableCommunities ---
    "indicators_df": df_indicators,
    "tracts_shp": shp_tract,
    
    # # --- HousingNeedsCharacteristics ---
    # "census_tract_data": pd.read_csv("../../data/processed/scoring_indicators/housing_needs_characteristics/merged_housing_data.csv"),
    # "tracts_gdf": gpd.read_file("../../data/raw/shapefiles/HousingNeeds/tl_2020_13_tract/tl_2020_13_tract.shp").to_crs("EPSG:4326"),
    # #"revitalization_score": 4,
    # "in_qct": False  # Required for housing need eligibility
} 

global_kwargs = kwargs.copy()

def score_point_parallel(lat_lon):
    lat, lon = lat_lon
    try:
        ct = CommunityTransportationOptions(lat, lon, **global_kwargs)
        dua = DesirableUndesirableActivities(lat, lon, **global_kwargs)
        sc = StableCommunities(lat, lon, **global_kwargs)
        qe = QualityEducation(lat, lon, **global_kwargs)

        ct_score = ct.calculate_score()
        dua_score = dua.calculate_score()
        sc_score = sc.calculate_score()
        qe_score = qe.calculate_score()

        return [{
            "lat": lat,
            "lon": lon,
            "community_transportation_options_score": ct_score,
            "desirable_undesirable_activities_score": dua_score,
            "stable_communities_score": sc_score,
            "quality_education_areas_score": qe_score,
            "total_score": ct_score + dua_score + sc_score + qe_score,
            "geometry": Point(lon, lat)
        }]
    except Exception as e:
        print(f"Error at (lat={lat:.4f}, lon={lon:.4f}): {e}")
        return []
    

if __name__ == "__main__":
    with Pool(processes=cpu_count()) as pool:
        results = list(tqdm(pool.imap_unordered(score_point_parallel, lat_lon_pairs), total=len(lat_lon_pairs)))

    # Flatten the list
    all_records = [record for group in results for record in group if 'geometry' in record]

    if all_records:
        gdf = gpd.GeoDataFrame(all_records, geometry="geometry", crs="EPSG:4326")
        gdf.to_file("final_scores.geojson", driver="GeoJSON")
    else:
        print("No records to save.")
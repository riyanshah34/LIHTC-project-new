# Mapping Opportunity: A Data-Driven Approach to Low-Income Housing Tax Credit Scoring

### Overview
This repository contains the full codebase, data, and map visualizations for a project aimed at deconstructs the location-based scoring components of Georgia's 2024 Qualified Allocation Plan (QAP) for Low-Income Housing Tax Credit (LIHTC) developments.

Using spatial data science and automation, the project builds an open-source platform that helps developers identify viable locations, simulate potential scores, and navigate Georgia's technically demanding LIHTC application process.

---

### Problem Context
The LIHTC program is the nation's largest source of affordable housing financing. In Georgia, nearly 34% of an application's total score is tied to location-based criteria, most of which require technical GIS skills, custom code, and access to fragmented public data. 

The result: smaller, community-rooted, and first-time developers are often excluded from competing effectively. 

The project simplifies these geographic components by automating the scoring process across five key categories:
- Community Transportation Options
- Desirable/Undesirable Activities
- Housing Needs Characteristics
    - *Note: This category was not included in the aggregate scoring functions because only 13 tracts (out of 2,000+) were eligible for points. Most projects instead qualify through other categories like Stable Communities or Revitalization Plans.*
- Quality Education Areas
- Stable Communities

---

### Project Goals
This project was developed in response to persistent challenges in the QAP process. It is designed to reduce
barriers to participation and improve transparency in the LIHTC application process through a data-driven, equity-focused platform. 

Specifically, the project aims to:
- Visualize spatial scoring criteria across metro Atlanta to help developers identify competitive sites
- Highlight areas of both opportunity and need to support equity-centered development
- Enable informed site selection through predictive tools that simulate how proposed
developments are likely to score
- Centralize fragmented public datasets into a clean, open-source resource

---

### Repository Layout
```text
├── aggregate_scoring/      # Core scoring logic and simulation tools
│   ├── aggregate_scoring.py                 # Script to combine all category scores and create final scoring dataset for mapping
│   ├── site_level_aggregate_scoring.ipynb   # For site-level scoring, just enter long/lat points of interest and run the script
│   └── grid_scoring_loop.ipynb              # Used to run the scoring function for each grid cell in the metro Atlanta area (for mapping)
│
├── data/                   # Raw → preprocessed → processed datasets
│   ├── raw/                # Source files exactly as downloaded
│   ├── preprocessed/       # Cleaned / reshaped for analysis (CSV / GeoJSON)
│   ├── processed/          # Final, ready-to-use indicator tables for scoring functions
│   └── map/                # GeoJSONs files used to create maps 
├── scripts/                # Python modules & notebooks for each QAP category
│   ├── community_transportation_options/ # Scripts for preprocessing and processing needed data, and creating score function for Community Transportation Options
│   ├── desirable_undesirable_activities/ # Scripts for collecting, preprocessing, and processing needed data, and creating score function for Desirable/Undesirable Activities
│   ├── housing_needs_characteristics/    # Scripts for preprocessing and processing needed data, and creating score function for Housing Needs Characteristics
│   ├── quality_education_area/           # Scripts for preprocessing and processing needed data, and creating score function for Quality Education Area
│   ├── stable_communities/               # Scripts for preprocessing and processing needed data, and creating score function for Stable Communities
│   └── maps/                             # Script to make folium maps
|
├── maps/                   # HTML heatmaps exported 
├── requirements.txt        # Exact package versions
└── README.md               # You are here
```
---

### Data Sources
No proprietary data was used in this project. This project integrates publicly available datasets and APIs to compute location-based scores defined in Georgia’s 2024 QAP. Key data sources by category:
- **Desirable / Undesirable Activities**
  - Google Places API (e.g., parks, clinics, auto shops)
  - U.S. EPA: Recovery Act Information System, Toxics Release Inventory (TRI), Chemical Data Reporting (CDR)
  - Georgia EPD: Hazardous Site Inventory
  - USDA: Food Access Research Atlas
- **Community Transportation Options**
  - Google Places API (Transit stops & hubs)
  - OpenStreetMap (Network walking distance)
- **Quality Education Areas**
  - Georgia Department of Education (CCRPI, Beating the Odds)
  - Governor’s Office of Student Achievement
  - Atlanta Public Schools Office of Student Assignment
  - Dekalb County ArcGIS Portal
- **Stable Communities**
  - U.S. Census Bureau: American Community Survey (Poverty Rate, Median Income)
  - Georgia Housing Needs Assessment (Environmental Health Index, Transit Access, Jobs Proximity)
- **Applicant Location Data**
  - Georgia Department of Community Affairs (LIHTC applications, 2022–2024)

### Contact 
Questions, suggestions, or contributions welcome via GitHub Issues or Pull Requests.

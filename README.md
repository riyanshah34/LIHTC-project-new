# Mapping Opportunity: A Data-Driven Approach to Low-Income Housing Tax Credit Scoring

**Overview**
This repository contains the full codebase, data, and map visualizations for a project aimed at demystifying the location-based scoring components of Georgia's 2024 Qualified Allocation Plan (QAP) for Low-Income Housing Tax Credit (LIHTC) developments.

Using spatial data science and automation, the project builds an open-source platform that helps developers identify viable locations, simulate potential scores, and navigate Georgia's technically demanding LIHTC application process.

---

**Problem Context**
The LIHTC program is the nation's most significant tool for financing affordable housing, yet the application process can be technically burdensome and exclusionary, particularly for small-scale or community-based developers. In Georgia, nearly 34% of LIHTC scoring depends on location-based criteria, which require sophisticated spatial analysis and access to fragmented public data sources.

The project simplifies and clarifies these geographic components by automating the scoring process across five key categories:
- Community Transportation Options
- Desirable/Undesirable Activities
- Housing Needs Characteristics
- Quality Education Areas
- Stable Communities

---

**Project Goals**
This project was developed in response to persistent challenges in the QAP process, especially
the burdens it places on small, community-based, or first-time developers. The goal is to reduce
barriers to participation and improve transparency in the Low-Income Housing Tax Credit
application process through a data-driven, equity-focused platform. Specifically, the project aims to:
- Visualize spatial scoring criteria across the Atlanta metro area to help developers identify
viable sites with strong point potential
- Highlight areas of both opportunity and need, allowing developers to prioritize projects
that are competitive and equity-oriented
- Enable informed site selection through predictive tools that simulate how proposed
developments are likely to score
- Centralize essential datasets into an open-source platform to streamline analysis and
reduce the technical burden on applicants
---

## **Project Structure Overview**
This repository contains data and scripts related to replicating and mapping scoring indicators based on the 2024 QAP.

---

## Repository Layout

```text
.
├── data/                   # Raw → preprocessed → processed datasets
│   ├── raw/                # Source files exactly as downloaded
│   ├── preprocessed/       # Cleaned / reshaped for analysis (CSV / GeoJSON)
│   ├── processed/          # Final, ready-to-use indicator tables for scoring functions
│   └── map/                # GeoJSONs files used to create maps 
|
├── scripts/                # Python modules & notebooks for each QAP category
│   ├── aggregate_scoring/  # Combines all category scores and creates final scoring dataset for mapping 
│   ├── community_transportation_options/ # Scripts for preprocessing and processing needed data, and creating score function for Community Transportation Options
│   ├── desirable_undesirable_activities/ # Scripts for collecting, preprocessing, and processing needed data, and creating score function for Desirable/Undesirable Activities
│   ├── housing_needs_characteristics/ # Scripts for preprocessing and processing needed data, and creating score function for Housing Needs Characteristics
│   ├── quality_education_area/ # Scripts for preprocessing and processing needed data, and creating score function for Quality Education Area
│   ├── stable_communities/ # Scripts for preprocessing and processing needed data, and creating score function for Stable Communities
│   └── maps/               # Script to make folium maps
|
├── maps/                   # HTML heatmaps exported for slide decks
├── requirements.txt        # Exact package versions
└── README.md               # You are here

---


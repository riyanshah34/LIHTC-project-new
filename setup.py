from setuptools import setup, find_packages

setup(
    name="aggregate_scoring",
    version="0.1.0",
    packages=find_packages(include=["aggregate_scoring", "aggregate_scoring.*"]),
    install_requires=[
        "pandas",
        "geopandas",
        "shapely",
        "numpy",
        "osmnx",
        "networkx",
        "thefuzz",
        "requests",
        "geopy"
    ],
)
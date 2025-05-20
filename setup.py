from setuptools import setup, find_packages

setup(
    name="aggregate_scoring",
    version="0.1.0",
    packages=find_packages(include=["scripts.aggregate_scoring"]),
    package_dir={"aggregate_scoring": "scripts/aggregate_scoring"},
    install_requires=[
        "pandas",
        "geopandas",
        "shapely",
        "numpy",
        "osmnx",
        "networkx",
        "thefuzz",
        "requests"
    ],
)
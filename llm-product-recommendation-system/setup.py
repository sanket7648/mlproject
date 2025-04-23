# filepath: D:\projectapp\llm-product-recommendation-system\setup.py
from setuptools import setup, find_packages

setup(
    name="llm-product-recommendation-system",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
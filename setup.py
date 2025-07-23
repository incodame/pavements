# setup.py
from setuptools import setup, find_packages

setup(
    name="pavements",
    version="0.1.0",
    packages=find_packages(where="lib"),
    package_dir={"": "lib"},
    install_requires=[],  # Add dependencies here
)
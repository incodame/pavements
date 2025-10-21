from setuptools import setup, find_packages

setup(
    name="pavements",
    version="0.1.0",
    description="A Python module for managing pavements (a sub-graph of application parameters).",
    author="incodame",
    packages=find_packages(where="lib/python"),
    package_dir={"": "lib/python"},
    install_requires=[
        "pyyaml>=5.4",  # Dependency for the yaml module
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Unlicense License (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
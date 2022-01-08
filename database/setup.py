import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent


# This call to setup() does all the work
setup(
    name="commentApi-databaseConnection",
    version="1.0.0",
    description="Module for managing database for simple api example",
    author="Juan Bernardo Benavides",
    license="MIT",
    packages=["database"],
    install_requires=["sqlalchemy"],
)

# Copyright (c) 2019 Andrew Chapkowski
#
# Apache 2.0 License
#
from setuptools import setup

import arcgisprofile

arcgisprofile_classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache 2.0 License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(name="arcgisprofile",
      version=arcgisprofile.__version__,
      author="Andrew Chapkowski",
      author_email="andrewonboe@gmail.com",
      url="https://github.com/achapkowski/profile_tools",
      tests_require=["pytest"],
      py_modules=["arcgisprofile"],
      description="ArcGIS API for Python profile management utilities.",
      long_description=long_description,
      license="Apache 2.0",
      classifiers=arcgisprofile_classifiers,
      python_requires=">=3.4",
      )
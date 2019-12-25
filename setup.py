#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: lynn
# Date: 2019-12-25
# Version: v1.0
"""
setup.py

Convert Common Expression Language To Elasticsearch Query String
"""

from setuptools import setup, find_packages

setup(
    name="pyes_cel",
    version="1.0.0",
    keywords=("pip", "pycel"),
    description="Convert CEL To DSL",
    long_description="Convert Common Expression Language To Elasticsearch Query String",
    license="MIT Licence",
    url="https://github.com/secoba/pyes_cel",
    author="lynn",
    author_email="lynn@sstsec.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)

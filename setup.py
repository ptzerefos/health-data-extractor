

# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='health-data-extractor',
    version='0.1.0',
    description='Data Extractor',
    long_description=readme,
    author='Panagiotis Tzerefos',
    author_email='panagiotis.tzerefos@gmail.com',
    url='https://github.com/ptzerefos/health-data-extractor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name='blitz',
    version=0.1.0,
    description='Blitz is a web based performance stress testing tool',
    long_description="",
    author='Guilherme Hermeto',
    author_email='gui hermeto at gmail com',
    url='http://blitz.io',
    packages=find_packages(),
    test_suite='unittest',
    tests_require=['nose', 'fudge'],
    install_requires=[],
    entry_points={
    },
    classifiers=[
    ],
)
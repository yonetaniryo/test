#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="test",
    version="0.1.0",
    description="test",
    author="Ryo Yonetani",
    author_email="",
    url="",
    install_requires=[
        "torch>=1.5.0",
        "torchvision>=0.6.0",
        "numpy>=1.18.4",
    ],
    packages=find_packages())

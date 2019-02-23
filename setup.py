#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gokulang',
    packages=['gokulang'],

    version='1.0.0',

    license='MIT',

    install_requires=['janome', 'pykakasi', 'semidbm', 'six'],

    author='shonansurvivors',
    author_email='shonansurvivors@gmail.com',

    url='https://github.com/shonansurvivors/goku-lang',

    description='To translate Japanese sentences into Son Goku accent',
    long_description=long_description,
    keywords='gokulang, goku-lang',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
#!/usr/bin/env python

import os, glob
from setuptools import setup, find_packages

setup(
    name='hipston',
    version='0.0.1',
    url='https://github.com/kislyuk/hipston',
    license='TBD',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='High Performance Storage Object Namespace',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

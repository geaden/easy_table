#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    # http://wiki.python.org/moin/Distutils/Cookbook/AutoPackageDiscovery
    import os

    def is_package(path):
        return (
            os.path.isdir(path) and
            os.path.isfile(os.path.join(path, '__init__.py'))
        )

    def find_packages(path='.', base=""):
        """ Find all packages in path """
        packages = {}
        for item in os.listdir(path):
            dir = os.path.join(path, item)
            if is_package( dir ):
                if base:
                    module_name = "%(base)s.%(item)s" % vars()
                else:
                    module_name = item
                packages[module_name] = dir
                packages.update(find_packages(dir, module_name))
        return packages

setup(
    name='easy_table',
    version='0.1.0',
    description='Python script for generating reStructured tables from provided source',
    long_description="""This is python script that generates rSt like table from provided source.
        Please use it on your own risk""",
    author='Gennady Denisov',
    author_email='denisovgena@gmail.com',
    license='BSD',
    url='https://github.com/geaden/easy_table',

    test_suite='tests',
    zip_safe=True,
    packages=find_packages(),
)

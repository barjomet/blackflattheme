#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2016 Cinc-th
#
# All rights reserved.
#
# This software is licensed as described in the file COPYING.txt, which
# you should have received as part of this distribution.
#
from setuptools import setup

setup(
    name='BlackFlatTheme',
    version='1.0',
    packages=['blackflattheme'],
    package_data={'blackflattheme': ['htdocs/css/*.css',
                                     'htdocs/fonts/*',
                                     'htdocs/js/*.js',
                                     'htdocs/*.png',
                                     'templates/*.html']},
    author="Cinc",
    author_email='',
    maintainer='Cinc',
    maintainer_email="",
    description="A responsive, flat, black theme using Bootstrap 3.3.1.",
    license="BSD",
    keywords="trac plugin theme",
    url="https://github.com/barjomet/blackflattheme",
    classifiers=[
        'Framework :: Trac',
    ],
    install_requires=['TracThemeEngine'],
    entry_points = {
        'trac.plugins': [
            'blackflattheme.theme = blackflattheme.theme',
        ]
    }
)

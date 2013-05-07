#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import tornadoencookie

with open('README.md') as stream:
  long_desc = stream.read()

setup(
    name = tornadoencookie.__name__,
    version = tornadoencookie.__version__,
    author = tornadoencookie.__author__,
    author_email = tornadoencookie.__email__,
    packages = ['tornadoencookie'],
    license = tornadoencookie.__license__,
    description = tornadoencookie.__description__,
    url='https://github.com/whardier/tornado-encookie',
    long_description = long_desc,
    install_requires=[
        'tornado',
        'pycrypto',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Framework :: Tornado',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: Session',
    ],
)


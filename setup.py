#!/usr/bin/env python

from __future__ import with_statement
from setuptools import setup

__AUTHOR__ = 'OGURA Daiki'
__AUTHOR_EMAIL__ = '8hachibee125@gmail.com'

readme = open('README.rst').read()

setup(name='pynk',
      version='0.0.5',
      description='LINQ-like list processing library in Python.',
      author=__AUTHOR__,
      author_email=__AUTHOR_EMAIL__,
      maintainer=__AUTHOR__,
      maintainer_email=__AUTHOR_EMAIL__,
      url='https://github.com/hachibeeDI/py-llll',
      license='MIT',
      keywords='python list linq',
      long_description=readme,
      packages=['pynk'],
    )

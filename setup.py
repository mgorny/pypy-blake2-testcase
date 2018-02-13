#!/usr/bin/env pypy

from distutils.core import setup, Extension


setup(name='testmod',
      ext_modules=[Extension('testmod', ['testmod.c'])])

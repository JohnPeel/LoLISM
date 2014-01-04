#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

options = {
	'py2exe': {
		'bundle_files': 1,
		'compressed': True,
		'dll_excludes': ['w9xpopen.exe'],
		'dist_dir': 'dist/LoLISM'
	}
}

setup(
    options = options,
    windows = [{'script': "LoLISM.py"}],
    zipfile = None
)

options['py2exe']['dist_dir'] = 'dist/LoLISM-gui'

setup(
    options = options,
    windows = [{'script': "LoLISM-gui.py"}],
    zipfile = None
)
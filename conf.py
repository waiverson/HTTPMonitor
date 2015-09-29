#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

import os, importlib, sys

sys.path.append(os.getcwd())

os.environ['SETTINGS_MODULE'] = 'settings'

try:
    SETTINGS_MODULE = os.environ['SETTINGS_MODULE']
except:
    raise Exception, "NEED A SETTINGS.PY FILE"

try:
    settings = importlib.import_module(SETTINGS_MODULE)
except ImportError, e:
    raise ImportError, "COULD NOT IMPORT SETTINGS %s" % (SETTINGS_MODULE)

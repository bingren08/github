#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jes
@file: untity.py
@time: 11/8/17 9:47 AM
"""

import re
import os
import sys
from codecs import open
path = os.path.dirname(os.path.abspath(__file__).replace('dm/lr','data'))
def read(f,mode='r',encoding='utf-8'):
    return open('/'.join([path,f]),mode=mode,encoding=encoding).readlines()

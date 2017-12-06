#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jes
@file: lr_22.py
@time: 11/6/17 4:59 PM
"""

import os
import sys

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from  sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
root_path = os.path.dirname(os.path.abspath(__file__).replace('dm/lr','data'))

from sklearn.linear_model import LinearRegression




if '__main__' ==__name__:
    print ('go')
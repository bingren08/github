#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: wukun3
@license: Lenovo Licence 
@contact: wukun3@lenovo.com
@site: http://www.lenovo.com
@software: lenovo
@file: tmp.py
@time: 11/10/17 5:17 PM
"""
import re
import os
import sys
from codecs import open

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# content = content.encode('utf-8','ignore')

def main(self):
    if len(sys.argv) > 2:
        data_path = sys.argv[1]
        save_path = sys.argv[2]
    else:
        data_path = ''
        save_path = ''


if __name__ == '__main__':
    main()
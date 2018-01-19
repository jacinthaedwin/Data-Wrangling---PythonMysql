# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 12:31:38 2017

@author: Jacintha
"""
import re
a = 'lkdfhisoe78347834 (())&/&745  '
result = re.sub('[^0-9]','', a)

print result
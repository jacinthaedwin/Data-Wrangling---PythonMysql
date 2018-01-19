# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:58:45 2017

@author: Jacintha
"""
import xml.etree.cElementTree as ET
count = 10
osm_file='chennai.osm'
for event, element in ET.iterparse(osm_file):
    count += 1
    if element.tag == "node" or element.tag == "way":
        print 'Element name: ', element.tag
        print 'Element attributes: ', element.attrib
        for child in element:
            print 'Child Element name: ', child.tag
            print 'Child Element attributes: ', child.attrib
    if count > 100:
        break
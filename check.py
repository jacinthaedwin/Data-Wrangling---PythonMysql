# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:08:54 2017

@author: Jacintha
"""

import xml.etree.cElementTree as ET
osm_file='chennai.osm'
postal_codes = set()
mapping_postalcode = { "6000036": "600036",
        "6000113": "600113",
            "6000042": "600042"
            }
#zip_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

try:
    for event, element in ET.iterparse(osm_file):
        if element.tag == "node" or element.tag == "way":
            
            for child in element:
                #print 'Child Element name: ', child.tag
                if child.tag == 'tag':
                   # print 'Child Element attributes: ', child.attrib['k']
                    if child.attrib['k'] == 'addr:state':
                        print(child.attrib['v'])
                       
                            
                        
                       #postal_codes.add(child.attrib['v'])
                       #print 'Child Element attributes: ', child
                       #print(child.attrib['v'])
except:
    #print child.tag
    print('Child Element name: ', child.tag)
    print("Unexpected error:", sys.exc_info()[0]) 
    

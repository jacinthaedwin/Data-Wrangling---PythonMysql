# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:55:10 2017

@author: Jacintha
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE_sample = "chennai.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected_city = ["chennai","CHENNAI","chennai-17", "t-nagar","saidapet","CHENNAI", "T.Nagar,Chennai"]
mapping_city={ "chennai": "Chennai",
            "CHENNAI": "Chennai",
            "chennai-17": "Chennai",
            "t-nagar": "Thygaraya Nagar",
            "T.Nagar,Chennai": "Thygaraya Nagar",
            "T Nagar, Chennai":"Thygaraya Nagar",
            "t.nagar, Chennai":"Thygaraya Nagar",
            "t nagar, Chennai":"Thygaraya Nagar",
            "Saidapet, Chennai":"Saidapet",
            "saidapet":"Saidapet",
            "Egmore, Chennai": "Egmore",
            "T.Nagar": "Thygaraya Nagar",
            }

expected_street = ["St", "Ave", "Rd", "rd"]

# UPDATE THIS VARIABLE

mapping_street={ "St": "Street",
            "St.": "Street",
            "Rd.": "Road",
            "Ave": "Avenue",
            "Ave.": "Avenue"
            }

mapping_postalcode = { "6000036": "600036",
            "6000113": "600113",
            "6000042": "600042"
            }

#expected = ["chennai","chennai-17", "t-nagar","saidapet","CHENNAI", "Road", "Street","Salai", "NR", "Avenue","Lane"]
def audit_city(filename):
    osm_file = open(filename, "r")  
    city_list = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:city" and tag.attrib['v'] != "Chennai":
                    city_list.add(tag.attrib['v'])
    return city_list

def fix_city_names(filename):
    #OSMFILE_sample=filename
    osm_file = open(filename, "r")  
    city_list = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:city" and tag.attrib['v'] in expected_city:
                    updated_city = update_city_name(tag.attrib['v'])
                    if(updated_city !=tag.attrib['v'] ):
                        print(tag.attrib['v'],updated_city)
                    
                    
def update_city_name(city):
    if city in mapping_city:
        better_name=city.replace(city, mapping_city[city])
        return better_name
    else:
        return city
 
def audit_streets(filename):
    osm_file = open(filename, "r")  
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:street":
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

def fix_streets(filename):
    osm_file = open(filename, "r")  
    #street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:street":
                    updated_street=update_street_name(tag.attrib['v'])
                    if updated_street!=tag.attrib['v']:
                        print(tag.attrib['v'],updated_street)
    
    
def audit_street_type(street_name):
    m = street_type_re.search(street_name)
    #print(street_name, m)
    if m:
        street_type = m.group()
        
    
    return street_type
def update_street_name(name):

    # YOUR CODE HERE
    m = street_type_re.search(name)
    #print(street_name, m)
    if m:
        street_type = m.group()
        if street_type in mapping_street:
                better_name=name.replace(street_type, mapping_street[street_type])                
                return better_name
        else:            
            return name
    else:
        return name
    
    
def fix_street(filename):
    OSMFILE_sample=filename
    osm_file = open(OSMFILE_sample, "r")  
    #city_list = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:street":
                    #street_type = audit_street_type(tag.attrib['v'])
                    #if(street_type in expected_street):
                        update_street_name(tag.attrib['v'])
#print(fix_street())
#fix_street()
def audit_postcodes(filename):
    osm_file = open(filename, "r")  
    post_codes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode":
                    update_postcodes(tag.attrib['v'])
    osm_file.close()
    return post_codes  

def fix_postcodes(filename): 
    osm_file = open(filename, "r")  
    #post_codes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode":
                    updated_postcode=update_postcodes(tag.attrib['v'])
                    if(tag.attrib['v']!=updated_postcode):
                        print(tag.attrib['v'], updated_postcode)
    osm_file.close()
def update_postcodes(postcode):
    result = re.sub('[^0-9]','', postcode)
    if(len(result)>6):
        if(result in mapping_postalcode):
            updated_postalcode=result.replace(result, mapping_postalcode[result])
            return updated_postalcode
        else:
            return result
    else:
        return result
    return result

print("Res",update_street_name('Anna Salai '))
#fix_city_names('sample.osm')
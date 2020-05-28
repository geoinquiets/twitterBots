import pandas as pd
import requests 
import time
import xmltodict
import json
import sys
from xml.etree import ElementTree

locLink = []
imageLink = []
title = []
imageW = 600
locFail = []
year = []
areageo = []
identi = []
list_csv_output = 'locMapsLinks_sace.csv'
maxrecords = 1024
numcalls = 0
currentCall = 0

url_coleccions = "http://cartotecadigital.icc.cat/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json"
url_imatges_col = "http://cartotecadigital.icc.cat/digital/bl/dmwebservices/index.php?q=dmQuery/{coleccio}/all/all/pointer/{maxrecords}/{start}/1/json"
url_metadata_info = "http://cartotecadigital.icc.cat/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/{coleccio}/{pointer}/json"
url_image_info = "http://cartotecadigital.icc.cat/digital/bl/dmwebservices/index.php?q=dmGetImageInfo/{coleccio}/{pointer}/xml"
url_image = "http://cartotecadigital.icc.cat/utils/ajaxhelper/?CISOROOT={coleccio}&CISOPTR={pointer}&action=2&DMSCALE={scale}&DMWIDTH={width}&DMHEIGHT={height}"
url_single_item = "http://cartotecadigital.icc.cat/cdm/ref/collection/{coleccio}/id/{pointer}"

#collections_json = requests.get(url_coleccions).json() 
collections_json = ['fsace']


for collection in collections_json:
    #alias = collection['alias'][1:]
    alias = collection
    print alias
    sys.stdout.flush()
    images_json = requests.get(url_imatges_col.format(coleccio=alias,maxrecords=maxrecords,start=0)).json()
    totalrecords = images_json['pager']['total']
    if totalrecords > maxrecords:
        numcalls = totalrecords/maxrecords
    print "numcalls: {}".format(numcalls)
    sys.stdout.flush()
    while currentCall <= numcalls:
        print "currentCall: {}".format(currentCall)
        sys.stdout.flush()
        if currentCall > 0:
            images_json = requests.get(url_imatges_col.format(coleccio=alias,maxrecords=maxrecords,start=maxrecords*currentCall)).json()
        for record in images_json['records']:
            pointer = record['pointer']
            try:
                metadata_info = requests.get(url_metadata_info.format(coleccio=alias,pointer=pointer)).json() 
                image_info_response = requests.get(url_image_info.format(coleccio=alias,pointer=pointer))
                image_info = image_info_response.content
                try:
                    image_info = json.loads(json.dumps(xmltodict.parse(image_info), indent=4))
                    width = int(image_info['imageinfo']['width'])
                    height = int(image_info['imageinfo']['height'])
                    if width != 0 and height != 0: 
                        longest_size = width if width > height else height
                        if width != 0:
                            try:
                                scale = (imageW*100)/int(longest_size)
                            except ZeroDivisionError:
                                print "{} {} {} {}".format(alias,pointer,width, height)
                                sys.stdout.flush()
                        else: 
                            scale=20
                        imageLink.append(url_image.format(coleccio=alias,pointer=pointer,scale=scale,width=width,height=height))
                        title.append(metadata_info['title'].encode('utf-8'))
                        locLink.append(url_single_item.format(coleccio=alias,pointer=pointer))
                        areageo.append(metadata_info['coveraa'].encode('utf-8'))
                        identi.append(metadata_info['identi'].encode('utf-8'))
                        if metadata_info['date'] != '':
                            try:
                                year.append(metadata_info['date'].encode('utf-8'))
                            except:
                                year.append('-')
                        else:
                            year.append('-')
                except:
                    print "{} {}".format(alias,pointer)
                    sys.stdout.flush()
            except:
                 print "{} {}".format(alias,pointer)
                 sys.stdout.flush()
        currentCall = currentCall + 1
print "locLink: {}".format(len(locLink))
print "imageLink: {}".format(len(imageLink))
print "title: {}".format(len(title))
print "year: {}".format(len(year))
print "areageo: {}".format(len(areageo))
print "identi: {}".format(len(identi))

locMaps = pd.DataFrame({id:locLink, 'imageLink': imageLink, 'title': title, 'year': year, 'areageo': areageo, 'identi': identi})

locMaps.drop_duplicates(subset='identi', inplace=True)

locMaps.to_csv(list_csv_output)

#locFails = pd.DataFrame({id:locFail})

#locFails.to_csv('locMapsFails_cartoteca.csv')
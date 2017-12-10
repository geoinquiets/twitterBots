import pandas as pd
import requests 
import time

locLink = []
imageLink = []
title = []
year = []
origFormat = []

url_list = ["https://www.loc.gov/collections/cities-and-towns/?fo=json", "https://www.loc.gov/collections/national-parks-maps/?fo=json",
            "https://www.loc.gov/collections/railroad-maps-1828-to-1900/?fo=json", "https://www.loc.gov/collections/civil-war-maps/?fo=json",
            "https://www.loc.gov/collections/sanborn-maps/?fo=json", "https://www.loc.gov/collections/discovery-and-exploration/?fo=json", 
            "https://www.loc.gov/collections/american-revolutionary-war-maps/?fo=json",
            "https://www.loc.gov/collections/finding-our-place-in-the-cosmos-with-carl-sagan/?fo=json",
            "https://www.loc.gov/collections/military-battles-and-campaigns/?fo=json", "https://www.loc.gov/collections/rochambeau-maps/?fo=json",
            "https://www.loc.gov/collections/transportation-and-communication/?fo=json"]

for u in url_list:

    collections_json = requests.get(u).json() 

    while True: 
        for collection in collections_json["results"]: 
            locLink.append(collection["url"])
            title.append(collection["title"].encode('utf8'))
            origFormat.append(collection["original_format"][0])
            if "date" in collection:
                year.append(collection["date"])
            else:
                year.append(0)

            if len(collection["image_url"]) > 4:
    	       imageLink.append(collection["image_url"][3])
            else: 
                imageLink.append("NA")

        next_page = collections_json["pagination"]["next"] 
        if next_page is not None: 
            collections_json = requests.get(next_page).json()
        else:
            break 

locMaps = pd.DataFrame({id:locLink, 'imageLink': imageLink, 'title': title, 'origFormat': origFormat, 'year': year})

locMaps = locMaps[(locMaps['origFormat'] == "map")]  
locMaps.drop_duplicates(subset='imageLink', inplace=True)

locMaps.to_csv('locMapsLinks.csv')
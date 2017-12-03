import os, random, twitter, credentials, pandas as pd

api = twitter.Api(consumer_key = credentials.CONSUMER_KEY,
                     consumer_secret = credentials.CONSUMER_SECRET,
                     access_token_key = credentials.ACCESS_KEY,
                     access_token_secret = credentials.ACCESS_SECRET) 

maps = pd.read_csv('locMaps.csv', skiprows=1, header=None, names=['link', 'imageLink', 'origFormat', 'title'])

n = random.randint(0,12605)

if len(maps.iloc[n]["title"]) > 112:
		maps.iloc[n]["title"] = maps.iloc[n]["title"][:113] + '...'

status = api.PostUpdate(status = maps.iloc[n]["title"] + " " + maps.iloc[n]["link"], media = "https:" + maps.iloc[n]["imageLink"])
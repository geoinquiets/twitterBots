import os, random, twitter, credentials2, pandas as pd

api = twitter.Api(consumer_key = credentials2.CONSUMER_KEY,
                     consumer_secret = credentials2.CONSUMER_SECRET,
                     access_token_key = credentials2.ACCESS_KEY,
                     access_token_secret = credentials2.ACCESS_SECRET) 

maps = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/locMapsLinks_sace.csv', skiprows=1, header=None, names=['link', 'areageo', 'identi', 'imageLink', 'title', 'year'])

random.seed()
n = random.randint(0,len(maps)-1)

resto = 280 - len(str(maps.iloc[n]["year"])) - len(maps.iloc[n]["link"]) - len(maps.iloc[n]["areageo"]) - len(" #CartotecaDigital #ICGC") - 3

title = maps.iloc[n]["title"]

if len(title) > resto:
 	title = title[:resto-4] + '...'

text = title + " " + str(maps.iloc[n]["year"]) + " " + maps.iloc[n]["areageo"] + " " + maps.iloc[n]["link"] + " #CartotecaDigital #ICGC"

status = api.PostUpdate(status = text , media = maps.iloc[n]["imageLink"])

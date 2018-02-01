import os, random, twitter, credentials, pandas as pd

api = twitter.Api(consumer_key = credentials.CONSUMER_KEY,
                     consumer_secret = credentials.CONSUMER_SECRET,
                     access_token_key = credentials.ACCESS_KEY,
                     access_token_secret = credentials.ACCESS_SECRET) 

maps = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/locMapsLinks_cartoteca.csv', skiprows=1, header=None, names=['link', 'imageLink', 'title', 'year'])

random.seed()
n = random.randint(0,len(maps)-1)

resto = 280 - len(str(maps.iloc[n]["year"])) - len(maps.iloc[n]["link"]) - len(" #CartotecaDigital #ICGC") - 2

title = maps.iloc[n]["title"]

if len(title) > resto:
 	title = title[:resto-3] + '...'

text = title + " " + str(maps.iloc[n]["year"]) + " " + maps.iloc[n]["link"] + " #CartotecaDigital #ICGC"

status = api.PostUpdate(status = text , media = maps.iloc[n]["imageLink"])

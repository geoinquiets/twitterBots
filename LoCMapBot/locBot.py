import os, random, twitter, credentials, pandas as pd

api = twitter.Api(consumer_key = credentials.CONSUMER_KEY,
                     consumer_secret = credentials.CONSUMER_SECRET,
                     access_token_key = credentials.ACCESS_KEY,
                     access_token_secret = credentials.ACCESS_SECRET) 

maps = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/locMapsLinks_cartoteca.csv', skiprows=1, header=None, names=['link', 'imageLink', 'title', 'year'])

random.seed()
n = random.randint(0,len(maps)-1)

resto = 140 - len(str(maps.iloc[n]["year"])) - len(maps.iloc[n]["link"]) - len(" #CartotecaDigital #ICGC") - 2

if len(maps.iloc[n]["title"]) > resto:
 		maps.iloc[n]["title"] = maps.iloc[n]["title"][:resto-2] + '...'

status = api.PostUpdate(status = maps.iloc[n]["title"] + " " + str(maps.iloc[n]["year"]) + " " + maps.iloc[n]["link"] + " #CartotecaDigital #ICGC" , media = maps.iloc[n]["imageLink"])
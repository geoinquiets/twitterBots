import twitter
import twitter_config
import json
import random

api = twitter.Api(consumer_key=twitter_config.consumer_key,
                      consumer_secret=twitter_config.consumer_secret,
                      access_token_key=twitter_config.access_token,
                      access_token_secret=twitter_config.access_secret) 

with open('biodiv.json') as json_data:
    biodiv = json.load(json_data)

n = random.randint(0,499)

if len(biodiv[n]["title"]) > 140:
	biodiv[n]["title"] = biodiv[n]["title"][:137] + '...'

status = api.PostUpdate(status = biodiv[n]["title"], media = biodiv[n]["url"])
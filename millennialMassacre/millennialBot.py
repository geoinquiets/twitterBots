import tweepy, time, os, datetime as dt
from random import randint

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('randomNouns.txt','r')
nounList=filename.readlines()
filename.close()

nounList = [n.strip('\n') for n in nounList]

places = ["yoga studio", "yoga retreat", "local coffee shop", "co-working space", "co-living space", "farmer's market", "Coachella Festival", "Lollapalooza Festival", "Bonnaroo Festival", "morning rave", "basement of their parents", "wellness summit", "juice bar", "mixed use development", "pop-up", "gentrifying neighborhood", "converted warehouse", "bar made of salvaged wood", "meditation studio", "crafts festival", "craft brewery", "legal speakeasy", "silent rave", "revitalized city center", "fast casual restaurant", "beer garden", "dog-friendly office", "office's ping pong table", "startup's nap room", "overpriced cycling studio", "meeting of two bike lanes", "Brooklyn of their city", "cat cafe", "food truck", "AirBnB rental", "mountain of their student debt", "local Minecraft server", "Genius Bar", "home they'll never be able to buy", "color run", "crossfit gym", "urban farm", "brunch spot", "line of a reservationless restaurant", "tiny house", "most obscure subreddit"]

weapons = ["kale", "too-hot Sriracha", "mason jars", "the flash of a selfie", "over-fermented craft beer", "moon juice", "poisoned kombucha", "a detox", "a juice cleanse", "natural remedies", "millennial pink overexposure", "$24 avocado toast", "authentic experiences", "scars of the Great Recession", "artisanal crafts", "cord-cutting", "#content", "their participation trophies", "internship-induced poverty", "whatever they did to malls", "the sharp edges of parents' checks", "their inherent superiority", "rank coconut oil", "activated charcoal", "deafening chants of YAS QUEEN", "overprocessed matcha", "toxins, generally", "an expired meal delivery kit", "think pieces about them", "their wokeness", "hand-weaved rope", "artisanal daggers", "the flame of a luxury candle", "a suffocating face mask", "murderous memes", "traditional shaving kits", "small batch liquor", "callous indifference", "machine learning", "the tubes of the interwebs", "the uber of the murder industry", "orders from TaskRabbit", "Netflix binging", "the dulcet tones of a podcast", "day one DLC", "bottomless mimosas", "improperly brewed coffee", "baby boomer disdain"]


today = dt.date.today().strftime('%B %d, %Y')

randomNoun = nounList[randint(0, len(nounList) - 1)]
randomPlace = places[randint(0, len(places) - 1)]
randomWeapon = weapons[randint(0, len(weapons) - 1)]

tweet = "On this day millennials murdered {1} at the {2} with {3}. RIP {1}.".format(today, randomNoun, randomPlace, randomWeapon)

api.update_status(tweet)


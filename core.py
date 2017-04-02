import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from listener import AlertsListener

#we should put the real values of credentials. 
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_secret = '...'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

h = AlertsListener()

twitter_stream = Stream(auth, AlertsListener())
twitter_stream.filter(track=['tsunami', 'cyclone', 'flood', 'tornado'])

#we should filter the tweets using much more filter criteria.
#as an initative I have used 'tsunami', 'cyclone', 'flood' and 'tornado'



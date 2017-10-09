import tweepy
 
consumer_key = "your consumer key"
consumer_secret = "your secret key"
access_token = "your access token"
access_token_secret = "your access token secret"

class Twitter:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
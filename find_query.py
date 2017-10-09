import tweepy
from time import sleep
from credentials import Twitter

for tweet in tweepy.Cursor(Twitter.api.search, q='#IamwithDrKC').items():
	try:
		print('Tweet by: @'+tweet.user.screen_name)
		#Retweet tweets as they are found
		tweet.retweet()
		print('Retweeted the tweet')
		sleep(5)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

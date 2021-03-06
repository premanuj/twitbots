from credentials import *
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#read unicode file
my_file = open('unicode_file.txt', encoding='utf-8')
file_lines = my_file.readlines()
my_file.close()

#create a for loop to iterate over file_lines
for line in file_lines:
	try:
		if line != '\n':
			api.update_status(line)
		else:
			pass
	except tweepy.TweepError as e:
		print(e.reason)
	sleep(1800)
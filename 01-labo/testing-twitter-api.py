import sys
try:
	import tweepy
except:
	print("Please open the Shell and run 'social_install' script")
	sys.exit(1)

#Consumer key
twitter_key = ''

#Consumer secret
twitter_secret = ''

#Access token
twitter_token = ''

#Access token secret
twitter_secretToken = ''

def twitterFunction(cKey, cSecret, aToken, aTSecret):
	auth = tweepy.OAuthHandler(cKey, cSecret)
	auth.set_access_token(aToken, aTSecret)
	twitter_tweet = tweepy.API(auth)
	return twitter_tweet

def twitterUserTimelineFunction(user):
	twitter_tweet = twitterFunction(twitter_key, twitter_secret, twitter_token, twitter_secretToken)
	if user == 'myself':
		public_tweets =twitter_tweet.user_timeline()
	else:
		public_tweets =twitter_tweet.user_timeline(user)
	tweetArray = []
	for tweetTimeline in public_tweets:
		tweetArray.append(tweetTimeline.text)
	return tweetArray

print('Dit is twitter')
print(twitterUserTimelineFunction('VelosofyYT'))
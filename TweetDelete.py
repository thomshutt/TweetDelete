import tweepy
import time
import sys
from datetime import datetime, timedelta

consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]
mins_before_killing = 30

if len(sys.argv) > 5:
  mins_before_killing = int(sys.argv[5])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

while 1:
  try:
    my_tweets = api.user_timeline()
    now = datetime.now()
    for tweet in my_tweets:
      if (now - tweet.created_at) > timedelta(minutes=mins_before_killing):
        print "Deleting: " + tweet.text.encode('utf-8')
        api.destroy_status(tweet.id)
  except:
    print "Error while trying to delete..."
  time.sleep(60 * 4)

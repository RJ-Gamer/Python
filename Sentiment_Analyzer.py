import tweepy
from textblob import TextBlob
file_name = "Tweetter.csv"
WRITE = 'w+'



consumer_key = '2DfkpF7mMYA0Phqp4VMh1Upln'
consumer_secret = 'gemrG77DPTQznGRgLbNAlUQS2RMbn2pMuyGWCIqXqn9jhANr44'

access_token = '355408113-5nzw5Jv1jSH4P0NDeIizUeoFOVs4GsJVSQcAJXo0'
access_token_secret = 'hsM69XIHL9wtEinoKMPCkz2bepuXkMBerT7A39CqUNIA3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitterfile = open(file_name, mode = WRITE)
tweetlist = []
public_tweets = api.search("Rajat")
for tweet in public_tweets:
    tweetlist.append(tweet);
    print(tweetlist)

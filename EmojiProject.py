
# coding: utf-8

# In[6]:

import pandas as pd
import requests
import tweepy
from tweepy import OAuthHandler

consumer_key = '0Ouc8jfN8Nb3AIqEXKefdWfUG'
consumer_secret = 'AZ6KA5WUsOh7kQSNvv7IdrX2wudZhVNxSXKDMTtLSbAImdzVzw'
access_token = '4721235721-JXYaEZ4xIZltEUQpT1XXN6zmnI7Afka6nkuZGm3'
access_secret = 'UMJDL63pvwIt5bj1mlDWvAmLGmhkNPLet2D6qTqbSriEm'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)



api = tweepy.API(auth)


results = []
for tweet in tweepy.Cursor(api.search, q='%23royals').items(500):
    results.append(tweet)

print type(results)
print len(results)
def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet
    in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet
    in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]


    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet
    in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet
    in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet
    in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet
    in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet
    in tweets]

    return DataSet

#Pass the tweets list to the above function to create a DataFrame
tweet_frame = toDataFrame(results)
tweet_frame[0:499]


# In[19]:

candy = tweet_frame[0:2]


# In[20]:

import csv
import codecs
# codecs.EncodedFile() to make csv work with UTF-8
with codecs.EncodedFile(open('test1234.csv', 'wb'), 'UTF-8') as f:
    # Normally UTF-8 files don't have a BOM, so you need to add it manually
    f.write(u'\uFEFF'.encode('UTF-8'))

    # Now add some rows to the csv file:
    writer = csv.writer(f)
    writer.writerow(['GRINNING FACE WITH SMILING EYES', '😁'])
    writer.writerow(['FACE WITH TEARS OF JOY', '😂'])
    writer.writerow([candy])


# In[ ]:




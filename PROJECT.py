
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np


# In[5]:

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'insert_twitter key'
consumer_secret = 'insert_twitter key'
access_token = 'insert_twitter key'
access_secret = 'insert_twitter key'
 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 


api = tweepy.API(auth)


# In[34]:

results = []
for tweet in tweepy.Cursor(api.search, q='%23test432').items(500):
    results.append(tweet)

print type(results)
print len(results)


# In[35]:

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


# In[36]:

tweet_frame[0:1]


# In[37]:

apple = tweet_frame[0:1].to_csv("zebra1.csv", encoding='utf-8')


# In[38]:

nltk_stopwords = stopwords.words("english")

print type(nltk_stopwords)
print len(nltk_stopwords)
my_stopwords = nltk_stopwords + ["br", "\r", "\n", '\r\n\r\n', "said", "000", "amto", "jdemarco", "demarco", "joe","mailto", "ambassador","ambassador hc","mo", "com","Thank", 'revenue management', 'revenue management', 'cc', 'email',
                                 "Ambassador","2015",'thank chrm','thank','chrm','director revenue','pm',"pmto", "cssgbcorporate", 
                                 'director', 'http', 'subject', 'hotel collection', 'hotel','collection', 'managementambassador',
                                 'ambassadorhc','sent','thank chrm', 'corporate', 'ambassadorhotelcollection', 'cssgb',
                                u'00', u'01', u'02', u'03', u'04', u'06', u'08', u'10', u'104', u'104 broadway', u'107', u'107 9th', u'11', u'1111', u'1111 grand', u'12', u'13', u'14', u'15', u'16', u'17', u'18', u'19', '' u'20', u'2016', u'21', u'22', u'23', u'24', u'25', u'26', '________________________________From:', u'27', u'28', u'29', u'30', u'31', u'316', u'316 719', u'326', u'400', u'400 tulsa', u'405', u'64105', u'64105 jdemarco', u'64106', u'64106 816', u'67202', u'67202 316', u'67202 ambassadorhotelcollection', u'704', u'704 770', u'7134', u'7134 suite', u'719', u'719 7192', u'7192', u'7192 wichita', u'74136', u'74136 704', u'770', u'770 8118', u'8118', u'8118 107', u'8118 jdemarco', u'816', u'816 326', u'918', u'9th', u'9th kansas', u'________________________________', u'__________________________________________________', u'__________________________________________________ join', ]
print len(my_stopwords)


# In[39]:

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from __future__ import division
pathname = "C:\Users\joed.AMBHO\Desktop\pycourse\project\zebra1.csv"
pd.set_option('display.max_colwidth', 1500)
sentdf = pathname
sentdf = pd.read_csv(sentdf)
sentdf['newtext'] = map(lambda x: x.decode('latin-1').encode('ascii','ignore'), sentdf['tweetText'])
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


print sentdf.shape
print list(sentdf)
sentdf['newtext'] = map(lambda x: x.replace('\r\n', ''), sentdf['tweetText'])
sentdf['newtext'] = map(lambda x: x.replace('________________________________, ', ''), sentdf['tweetText'])
prelim = CountVectorizer(binary=False, lowercase = False, stop_words = 'english') 
prelim_dm = prelim.fit_transform(sentdf['newtext'])
print prelim_dm.shape
sentdf['newstext'] = sentdf['newtext'].replace('\r\n', '')
names = prelim.get_feature_names()
print type(names), len(names)

count = np.sum(prelim_dm.toarray(), axis = 0).tolist()
print type(count), len(count)
count_df = pd.DataFrame(count, index = names, columns = ['count'])

count_df.sort(['count'], ascending = False).head(20)
import re
news_dict = { ' rate ':' ADR ', ' property ':' hotel ', ' RevPARs ' : ' RevPAR ', ' Brunch' : ' Breakfast ', ' Oklahoma City ' : ' OKC ', ' Kansas City ': ' KC ', ' tulak ': ' Tulsa ', ' ICTAK ': ' Wichita ', ' mciaa ': ' KC ', ' okcak ': ' OKC '}


def multiple_replace(dict, text): 

  """ Replace in 'text' all occurences of any key in the given
  dictionary by its corresponding value.  Returns the new tring.""" 
  text = str(text).lower()

  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

sentdf['newtext'] = map(lambda x: multiple_replace(news_dict, x), sentdf['newtext'])


# # Homework 5: I will be looking at all of my sent and recieved emails

# In[40]:

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open("C:\Users\joed.AMBHO\Desktop\pycourse\week5\AFINN-111.txt") ]))

def afinn_sent(inputstring):
    
    sentcount =0
    for word in inputstring.split():  
        if word in afinn:
            sentcount = sentcount + afinn[word]
            
    
    if (sentcount < 0):
        sentiment = 'Negative'
    elif (sentcount >0):
        sentiment = 'Positive'
    else:
        sentiment = 'Neutral'
    
    return sentiment
    #return sentcount

sentdf['afinn'] = map(lambda x: afinn_sent(x), sentdf['newtext'])
sentdf['afinn'].value_counts()


# In[31]:

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

cv1 = CountVectorizer(lowercase=True, 
                     stop_words='english',
                     binary=False,
                     ngram_range = (1,2)) 
tfidf1 = TfidfVectorizer(lowercase=True, 
                        stop_words='english', 
                        ngram_range = (1,2)) 

choice = TfidfVectorizer(stop_words = 'english') 

cv_dm = cv1.fit_transform(sentdf['newtext'])
tfidf_dm = tfidf1.fit_transform(sentdf['newtext'])
choice_dm = choice.fit_transform(sentdf['newtext'])

print cv_dm.shape
print tfidf_dm.shape
print choice_dm.shape
names = cv1.get_feature_names()
print type(names), len(names)

count = np.sum(cv_dm.toarray(), axis = 0).tolist()
count_df = pd.DataFrame(count, index = names, columns = ['count'])


# In[32]:

afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open("C:\Users\joed.AMBHO\Desktop\pycourse\week5\AFINN-111.txt") ]))

def afinn_sent(inputstring):
    
    sentcount =0
    for word in inputstring.split():  
        if word in afinn:
            sentcount = sentcount + afinn[word]
            
    
    if (sentcount < 0):
        sentiment = 'Negative'
    elif (sentcount >0):
        sentiment = 'Positive'
    else:
        sentiment = 'Neutral'
    
    return sentiment
    #return sentcount

sentdf['afinn'] = map(lambda x: afinn_sent(x), sentdf['newtext'])
sentdf['afinn'].value_counts()


# In[ ]:




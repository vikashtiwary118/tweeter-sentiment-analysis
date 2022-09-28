#importing required libraries
import pandas as pd
from textblob import TextBlob
import tweepy
import re
from config import *
from operator import itemgetter

#searchcriteria
searchtype = "Hashtag"
#searchvalue = "covid"

#assinging secret keys and token
def set_access_token():
    #authenticating
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_s)
    auth.set_access_token(access_token,access_token_s)
    return auth


def tweepy_api_object(auth):
    #create tweepy api object
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api


#searching the tweets
def searchValue(api, searchvalue):
    if searchtype == 'Hashtag':
       searchv  = api.search_tweets(searchvalue, count = 1000, lang='en', tweet_mode= 'extended')
       return searchv
    elif searchtype == 'Username':
        searchv = api.user_timeline(screen_name = searchvalue,count = 1000, lang='en', tweet_mode= 'extended')
        return searchv
    else:
        print('ok')

    
#create dataframe
def create_dataframe(searchv):
        #creating dataframe
    if searchtype == 'Username':
        data = pd.DataFrame([tweet.full_text for tweet in searchv], columns=['tweets'])
        return data
    elif searchtype == 'Hashtag':
        data = pd.DataFrame([tweet.full_text for tweet in searchv], columns=['tweets'])
        return data
    else:
        pass


# remove emoji
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


#creating the function to clean the text 
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9_:]+', '', text) #removin @mention
    text = re.sub(r'#', '', text) #removing '#' syboll
    text = re.sub(r'RT[\s]+', '', text) #removing retweets
    text = re.sub('RT @\w+: '," ",text) 
    text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text)
    text = re.sub(r'https?:\/\/\S+', '', text) #removing links
    text = remove_emoji(text) #remove emoji
    return text.lower()


#creting a funcitno to get subjectivity
def getSubejectivity(text):
    return TextBlob(text).sentiment.subjectivity

#creating a function to get polarity 
def getPolarity(text):
    return TextBlob(text).sentiment.polarity



#creating fucntion for analysis
def computePositivity(polarityvalue):
    if polarityvalue > 0:
        return "Positive"
    elif polarityvalue < 0:
        return "Negative"
    else:
        return "Nutral"
    


def sentimental_analysis(text):
    auth = set_access_token()
    api = tweepy_api_object(auth)
    searchv = searchValue(api, text)
    #creating dataframe
    data = create_dataframe(searchv)
    data['tweets'] = data['tweets'].apply(cleanText)
    #creating a new column for subjectivity and polority 
    data['Polarity'] = data['tweets'].apply(getPolarity)
    data['Subjectivity'] = data['tweets'].apply(getSubejectivity)

    data['Analysis'] = data['Polarity'].apply(computePositivity)

    data_final = data[["tweets", "Analysis"]]
    
    # print(data_final.head())
    rows = []
    for index, row in data_final[['tweets', 'Analysis']].iterrows():
        rows.append({
                'tweets': row['tweets'],
                'Analysis': row['Analysis'],
                })
    # data_final.to_dict('records')
    return rows

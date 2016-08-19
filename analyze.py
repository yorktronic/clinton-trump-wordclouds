#####################################################################################################################
#
# Analyses of tweets, including building word clouds, analyzing sentiment, and generating fake Donald Trump tweets
#
#####################################################################################################################

import getandclean as gc
import matplotlib as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud

accounts = ['@realDonaldTrump']

def getTwitterData(acct_names):

    # Save the tweets in CSV format once cleaned
    for name in acct_names:
        print "getting tweets for screen name {}".format(name)
        tweets = gc.getTweets(name)
        for tweet in tweets:
            tweet.text = gc.cleanTweet(tweet.text)
        gc.storeTweetsJson(tweets, name, clean=True)

def createWordCloud(tweets):
    vec = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_df=.5)
    tfv = vec.fit_transform(tweets)
    terms = vec.get_feature_names()
    wc = WordCloud(height=1000, width=1000, max_words=300).generate(" ".join(terms))

    return wc

def visualizeWordCloud(wc):
    plt.figure(figsize=(10,10))
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

def doIt(file_name):
    tweets = cleanTweets(file_name)
    wc = createWordCloud(tweets)
    visualizeWordCloud(wc)
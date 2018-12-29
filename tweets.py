import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

keyword = input("Enter the search term:")
results = api.search(q=""+keyword, count=1000)
obj = open('tweetfeed.txt','w')

for result in results:
	obj.write(result.text+'\nLINESPLIT ')
obj.close()
lines = open('tweetfeed.txt','r').read().split('\nLINESPLIT ')
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
	score = analyser.polarity_scores(sentence)
	return score
def sentiments(lines):
	result = {'pos': 0 ,'neu': 0,'neg': 0,'count': 0}
	count=0
	for line in lines:
		sentiment = sentiment_analyzer_scores(line)
		if sentiment['compound']>=0.05:
			result['pos']= result['pos']+1
		elif sentiment['compound']<=-0.05:
			result['neg']= result['neg']+1
		else:
			result['neu']=result['neu']+1	
		count = count+1
	result['count'] = count
	return result	
	

countOfSentiments = sentiments(lines)
count = countOfSentiments['count']
positive = countOfSentiments['pos']*100/count
negative = countOfSentiments['neg']*100/count
neutral = countOfSentiments['neu']*100/count

slices = []
slices.append(positive)
slices.append(neutral)
slices.append(negative)
reactions = ['Positive', 'Neutral', 'Negative']
colors = ['g','y','r'] 
plt.pie(slices,labels=reactions, colors=colors,autopct='%1.1f%%',shadow=True,explode=(0.4,0,0))
plt.title('Sentiment of tweets about '+ keyword)
plt.show()
	




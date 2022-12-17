from __future__ import division
from pymongo import MongoClient
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import operator

# Establish connection with database
client = MongoClient()
db = client.test
col = db.twitterBrazil

#######################################################
# Retrieve data from the mongodb database, choosing
# the fields you'll need afterwards
#######################################################
my_tweets = db.twitterBrazil.find({},{'lang':1, '_id':0, 'text':1,
'entities.hashtags':1,'in_reply_to_status_id':1, 'is_quote_status':1,
'retweeted_status':1, 'user.screen_name':1})
numTweets = db.twitterBrazil.count()

####################################################
# Plot of Languages (autodetected by Twitter)
####################################################
langsList = []
for t in my_tweets:
langsList.append(t['lang'])
D = Counter(langsList)
# ----------- Bar Plot ------------------------
plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())
plt.title('Languages spoken in the tweets captured')
plt.show()


############################################################################
# Plot how many of them are retweets, replies, quotations or original tweets
############################################################################
my_tweets.rewind() #Reset cursor
retweets = replies = quotations = originals = 0
for t in my_tweets:
if t.get('retweeted_status') is not None:
retweets=retweets+1
elif t['is_quote_status'] is not False:
quotations = quotations+1
elif t.get('in_reply_to_status_id') is not None:
replies = replies+1
else:
originals = originals+1
# ----------- Pie Chart ------------------------
labels = 'Original Content', 'Retweets', 'Quotations', 'Replies'
sizes = [originals, retweets, quotations, replies]
frequencies = [x/numTweets for x in sizes]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0) # explode 1st slice
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of Tweets depending on how the content is generated')
plt.show()

##################################################################
# Plot secondary hashtags
##################################################################
my_tweets.rewind()
hashList = []
for t in my_tweets:
for e in t['entities']['hashtags']:
h = e['text']
hashList.append(h)
D = Counter(hashList)
subset = dict(D.most_common(15))
sorted_subset = sorted(subset.iteritems(), key=operator.itemgetter(1))
# ----------- Horizontal Bar Plot ------------------------
pos = range(len(sorted_subset))
plt.barh(pos, [val[1] for val in sorted_subset], align = 'center', color =
'yellowgreen')
plt.yticks(pos, [val[0] for val in sorted_subset])
plt.tight_layout()
plt.title('Top 15 of hashtags captured')
plt.show()
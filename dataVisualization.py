import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


tweetSearch = "automation"

tweetFile = open("tweets_small.json","r")
tweetData = json.load(tweetFile)
tweetFile.close()

# combine all of the tweet texts
combinedTweets = ""
for tweet in tweetData:
    combinedTweets += tweet['text']

# create a combined Text Text Blob
tweetBlob = TextBlob(combinedTweets)

# Filter words

wordsToFilter = ["about","https","in","the","thing","will","could","tweetSearch"]

filteredDictionary = dict()

for word in tweetBlob.words:
    # skip tiny words
    if len(word) < 2:
        continue
    # skip words with randomc haracters or numbers
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:
        continue
    # don't want lower case words smaller than 5 letters
    if len(word) < 5 and word.upper() != word:
        continue
    # try lower case only, try with upper case
    filteredDictionary[word.lower()] = tweetBlob.word_counts[word.lower()]

# create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)

plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()

polarityList = []

# [optional] subjectivity
subjectivityList = []

# get sentiment tweetData
for tweet in tweetData:
    tweetBlob = TextBlob(tweet["text"])
    polarityList.append(tweetBlob.polarity)

    subjectivityList.append(tweetBlob.subjectivity)
print(polarityList)
print(subjectivityList)


# create graph

plt.hist(polarityList, bins=[-1.1,-.75,-0.5,-0.25,0,0.25,0.5,0.75,1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1,1.1,0,100])
plt.grid(True)
plt.show()

plt.plot(polarityList,subjectivityList,'ro')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('Tweet polarity vs Subjectivity')
plt.axis([-1.1,1.1,-0.1,1.1])
plt.grid(True)
plt.show()

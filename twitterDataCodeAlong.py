# twitter data is stored in the json format
import json

#we;re not changing anything, just looking a tthe data, so we used r
tweetFile = open("tweets_small.json","r")

tweetData = json.load(tweetFile)

#now that we have the data stored locally, we can close the file
tweetFile.close()

# print("Tweet text: ", tweetData[50]["text"])

#for idx in range(len(tweetData)):
#    print("Tweet text: "+tweetData[idx]["text"])

for myTweet in tweetData:
    print("Tweet text: "+myTweet["text"])

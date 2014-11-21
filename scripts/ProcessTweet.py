"""
Processes each tweet to convert to lower case and replace urls,
usernames, hashtags and punctuations
"""

#import regex
import re

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
output_file = open('processed_file.txt','w')
fp = open('train_full_B.tsv', 'r')
line = fp.readline().split()

while line:
    # processedTweet = processTweet(line)
    tweet_id = line[0]
    tweet_user_id = line[1]
    sentiment = line[2]
    line = line[3:]
    tweet = " ".join(line)
    processedTweet = processTweet(tweet)
    print processedTweet
    newline = tweet_id + " " + tweet_user_id + " " + sentiment + " " + processedTweet + "\n"
    output_file.write(newline)
    line = fp.readline().split()
#end loop
fp.close()
output_file.close()
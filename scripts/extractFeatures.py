# Converts each tweet in the training set to a list of feature vectors

#initialize stopWords
import re
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end


#Read the tweets one by one and process it
fp = open('processed_file.txt', 'r')
line = fp.readline().split()

stopWords = getStopWordList('stopwords.txt')
print stopWords

output_file = open("featuresTweet.txt",'w')
featureListFile = open("featureList.txt",'w')

overall_dic = {}

def updateFrequencyDic(featureVector):
    for feature in featureVector:
        if not feature in overall_dic.keys():
            overall_dic[feature] = 1


while line:
    tweet_id = line[0]
    tweet_user_id = line[1]
    sentiment = line[2]
    line = line[3:]
    processedTweet = " ".join(line)
    print processedTweet
    featureVector = getFeatureVector(processedTweet)
    updateFrequencyDic(featureVector)
    print featureVector
    newftTweet = tweet_id + " " + tweet_user_id + " " + sentiment + " " + " ".join(featureVector) + "\n"
    output_file.write(newftTweet)
    line = fp.readline().split()

fp.close()
output_file.close()

#for the featureListFile
for key in overall_dic.keys():
    featureListFile.write(key+" ")
featureListFile.close()
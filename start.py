import sys
import json
import twitter
import time
from config import twitter_credentials,train_files
from NaiveBayes import NaiveBayes
from DecisionTree import DecisionTree

#default parameters
DEBUG = True
CLASSIFIER = "nb"

#for the api
api = twitter.Api(consumer_key=twitter_credentials["consumer_key"],
			consumer_secret=twitter_credentials["consumer_secret"],
			access_token_key=twitter_credentials["access_token"],
			access_token_secret=twitter_credentials["access_token_secret"])
# print api.VerifyCredentials()

#get the classifier ready
classifier = None
if CLASSIFIER == 'dt':
	classifier = DecisionTree(train_files["stopword_file"],
		train_files["feature_list_file"],
		train_files["train_file"],debug=DEBUG)
else:
	classifier = NaiveBayes(train_files["stopword_file"],
		train_files["feature_list_file"],
		train_files["train_file"],debug=DEBUG)

twitter_stream = api.GetStreamSample()
while True:
	try:
		response = twitter_stream.next()
		if 'text' in response.keys() and 'lang' in response.keys():
			print response['text']
			# print classifier.classify(response['text'])
		time.sleep(5)
	except UnicodeEncodeError:
		#Cannot print hence not processed
		pass
	except:
		#Some other error has occured hence abort
		break
twitter_stream.close()


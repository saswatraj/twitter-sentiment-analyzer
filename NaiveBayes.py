import re
import nltk

class NaiveBayes:
	def __init__(self,stopWordFile,featureListFile,trainingFile,debug=False):
		"""
		Initializes the classifier and trains it based on the training set
		"""
		self.debug = debug
		self.stopWords = self._getStopWordList(stopWordFile)
		self.feature_list = self._getFeatureList(featureListFile)
		self.classifier = self._train(trainingFile)

	def _getFeatureList(self,feature_list_file):
		"""
		Reads the total features collected from the training set 
		@ returns list of all features for creating the feature vector 
		          of a tweet
		"""
		if self.debug:
			print "Extracting features list"
		fp = open(feature_list_file,'r')
		feature_list = fp.readline().split()
		fp.close()
		return feature_list

	def extractFeatures(self,tweet):
		"""
		Generates the required format of the features
		"""
		features = {}
		for word in self.feature_list:
			features['contains(%s)' % word] = (word in tweet)
		return features

	def processTweet(self,tweet):
		"""
		Formats the tweet
		"""
		tweet = tweet.lower()
		tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
		tweet = re.sub('@[^\s]+','AT_USER',tweet)
		tweet = re.sub('[\s]+', ' ', tweet)
		tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
		tweet = tweet.strip('\'"')
		return tweet

	def _getStopWordList(self,stopWordListFileName):
		"""
		Reads the list of stopwords for preprocessing of tweets and the 
		extraction of features
		"""
		stopwords = []
		if self.debug:
			print "Getting the stopwords list"
		stopwords.append('AT_USER')
		stopwords.append('URL')
		fp = open(stopWordListFileName,'r')
		line = fp.readline()
		while line:
			word = line.strip()
			stopwords.append(word)
			line = fp.readline()
		fp.close()
		return stopwords


   	def _replaceExtendedWords(self,word):
   		"""
   		Utility method that replces words extended in social
   		sites for showing emotions like wooooooow !!
   		"""
   		pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
   		return pattern.sub(r"\1\1", word)


	def getFeatureVector(self,tweet):
		"""
		Returns the feature vector for a tweet
		"""
		featureVector = []
		words = tweet.split()
		for w in words:
			w = self._replaceExtendedWords(w)
			w = w.strip('\'"?,.')
			val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
			if(w in self.stopWords or val is None):
				continue
			else:
				featureVector.append(w.lower())
		return featureVector

	def classify(self,tweet):
		"""
		Given a tweet this will classify the tweet into positive, negative
		or neutral sentiments based on the classifier
		"""
		processedTweet = self.processTweet(tweet)
		featureVector = self.getFeatureVector(processedTweet)
		classValue = self.classifier.classify(self.extractFeatures(featureVector))
		return classValue

	def _train(self,trainingFile):
		"""
		Prepares the classifier by generating the required training data and
		training the classifier on the data
		@ returns a trained classifier
		"""
		tweets = []
		tfFile = open(trainingFile,'r')
		line = tfFile.readline().split()
		while line:
			sentiment = line[2]
			featureVector = line[3:]
			tweets.append((featureVector,sentiment))
			line = tfFile.readline().split()
		tfFile.close()
		if self.debug:
			print "Finished reading tweets"
			print "Getting the training set.."
		training_set = nltk.classify.util.apply_features(self.extractFeatures, tweets)
		NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
		if self.debug:
			print "Ready for tweets.."
		return NBClassifier

# ![](https://raw.githubusercontent.com/saswatraj/twitter-sentiment-analyzer/master/logo.png "Twitter-Sentiment-Analyzer")

A classifier that trains on a training set and tries to classify live twitter public tweets as positive negative or neutral. Can be extended to include other features as well.

## Packages needed

* Python 2.7
* Python-nltk
* Python-twitter

Python-twitter is a pre built module for connecting to twitter. You may use the `requests` module in python to establish a connection to the streaming points after authenticating with twitter instead of using python-twitter for more customization. You will also need to change the config file to include the `access_token` and `secret` and the `consumer_token` and the `consumer_secret` that you get after creating an application in your account in twitter.A detailed decription is present in the link below: https://dev.twitter.com/oauth/overview 

## Running the classifier

You can run the classifier by `python start.py` command from terminal. However before this you need to modify the features according to the nltk classifier using the scripts in the scripts folder. These preprocess the features. You also need to modify `config.py` to include the access tokens and the feature file locations as they are required to build the classifier.
`start.py` takes as arguments a debug command that prints the debug messages and the type of classifier needed to classify. We have implimented 2 types: the DecisionTreeClassifier and the NaiveBayesClassifier for classifying. To use the decision tree which is much slower one needs to add a `-dt` to the arguments of the `start.py` file and a `-debug` for the debug mode.

## Bugs 
If you find any bugs please mail to me at : __saswatrj2010@gmail.com__


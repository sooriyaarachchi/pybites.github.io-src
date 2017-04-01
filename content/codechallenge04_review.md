Title: Code Challenge 04 - Twitter data analysis Part 1: Getting Data - Review
Date: 2017-02-03 17:00
Category: Challenges
Tags: codechallenges, code review, github, learning, tweets, Twitter, twitterapi, oop, datamodel, csv, namedtuples
Slug: codechallenge04_review
Authors: PyBites
Summary: It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge04.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge04.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## A possible solution

See [here](https://github.com/pybites/challenges/blob/solutions/04/usertweets.py) and detailed below:


* stdlib imports, pip install tweepy

		from collections import namedtuple
		import csv
		import os

		import tweepy

* we generated our keys through the Twitter API and put them in config.py

		from config import CONSUMER_KEY, CONSUMER_SECRET
		from config import ACCESS_TOKEN, ACCESS_SECRET


* we define some constants:

		DEST_DIR = 'data'
		EXT = 'csv'
		NUM_TWEETS = 100

* we build a tweepy api object. First we had this in the constructor (init), but second thought we set it up as a constant:

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
		API = tweepy.API(auth)

* we use a namedtuple to define Tweet: 

		Tweet = namedtuple('Tweet', 'id_str created_at text')

	Namedtuples are awesome for simple classes to store data without behaviour!

* we define the class, Python3 best practice is to explicitly inherit from object: 

		class UserTweets(object):

* the constructor gets the handle and an optional max_id, latter is to get a fixed set of tweets which we used in test_usertweets.py: 

			def __init__(self, handle, max_id=None):
				self.handle = handle
				self.max_id = max_id
				self.output_file = '{}.{}'.format(os.path.join(DEST_DIR, self.handle), EXT)
				self._tweets = list(self._get_tweets())
				self._save_tweets()

* we get the tweets with the \_get_tweets() helper. It returns a generator of Tweet namedtuple objects containing only the get id_str, created_at and text attributes (you get a lot more returned from the Twitter API!): 

			def _get_tweets(self):
				tweets = API.user_timeline(self.handle, count=NUM_TWEETS, max_id=self.max_id)
				return (Tweet(s.id_str, s.created_at, s.text.replace('\n', '')) for s in tweets)

* the helper \_save_tweets saves tweets to a CSV file. We choose to do it in the constructor, but you can of course take the underscore (\_) out and call it explicitly: obj.save_tweets():

			def _save_tweets(self):
				with open(self.output_file, 'w') as f:
					writer = csv.writer(f)
					writer.writerow(Tweet._fields)
					writer.writerows(self._tweets)

* implementing len and getitem lets you iterate over the tweets (see our [data model post](http://pybit.es/python-data-model.html)) as done in the for loop under \_\_main\_\_:

			def __len__(self):
				return len(self._tweets)

			def __getitem__(self, pos):
				return self._tweets[pos]


		if __name__ == "__main__":

			for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
				print('--- {} ---'.format(handle))
				user = UserTweets(handle)
				for tw in user[:5]:
					print(tw)
				print()

* running the tests:

		$ python test_usertweets.py
		...
		----------------------------------------------------------------------
		Ran 3 tests in 0.001s

		OK

	TODO: twitter data changes and you don't want to call the API (slows tests down, unittests should be fast), need to look at mock ...

## Any issues or feedback?

What did you learn this challenge? Feel free to share you code in the comments below. 

How are you experiencing these challenges? You like the format? What can we do differently and/or better?

## next(challenges)

Next week we use this pre-work to load in tweets of various Twitter users and determine who are most similar using NLP techniques. See you on Monday ...

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/) if you already forked it.

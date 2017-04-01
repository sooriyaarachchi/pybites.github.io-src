Title: Code Challenge 07 - Twitter Sentiment Analysis - Review
Date: 2017-02-26 00:50
Category: Challenges
Tags: codechallenges, code review, learning, Twitter, sentiment, TextBlob
Slug: codechallenge07_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge07.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge07.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Possible solution / learning

### Getting the data

First we let the [data gathering script we provided](https://github.com/pybites/challenges/blob/solutions/07/getting_data.py) run for 5 days and 10 hours. As promised we would do the analysis on [50 shades of darker](http://www.imdb.com/title/tt4465564/):

	$ nohup python getting_data.py 50 shades darker &

It ran Mon Feb 20 09:13 - Sat Feb 25 19:25 and collected > 10K tweets, storing them in data_1487581986.json

We kept it simple, question to be answered: 

> Is there overly positive or negative talk about 50 shades of darker on Twitter?

### Enter TextBlob

> [TextBlob](https://textblob.readthedocs.io/en/dev/) is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

It makes sentiment analysis very easy. 

### Code

Our script is [here](https://github.com/pybites/challenges/blob/solutions/07/sentiment.py). What we did:

* Import required libraries: 

		from collections import defaultdict
		import json
		import sys

		from textblob import TextBlob

	If you want to follow along, create a virtual env and do a pip install -r requirements.txt (from subdirectory 07, after having cloned the challenges repo).

* Each retrieved tweet (and its meta data) was stored as json by the data collector script. This generator retrieves them from the input file (further down):

		def get_tweets(input_file):
			with open(input_file) as f:
				for line in f.readlines():
					yield json.loads(line)


* [TextBlob Quickstart](http://textblob.readthedocs.io/en/dev/quickstart.html) offers an easy API for sentiment analysis:

	> The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity). The polarity score is a float within the range [-1.0, 1.0].

	So we defined:	

		def get_sentiment(polarity):
			if polarity < 0:
				return "negative"
			elif polarity == 0:
				return "neutral"
			else:
				return "positive"

* We pass the script the data_1487581986.json file we collected on our server:

		if __name__ == "__main__":
			if len(sys.argv) < 2:
				print('please provide json data file')
				sys.exit(1)

			input_file = sys.argv[1]

			tweets = get_tweets(input_file)


* We use a defaultdict to store the sentiments. We use a collections.defaultdict + set here (over the simpler collections.Counter) for two reasons: 1. ignore duplicate tweets, 2. store the texts for further inspection (see further down).

	This really shows the magic of external libraries and a nice API: few lines of code, hiding complexity:

			sentiments = defaultdict(set)

			for tw in tweets:
				text = dict(tw)['text'].lower()
				blob = TextBlob(text)
				sent = get_sentiment(blob.sentiment.polarity)
				sentiments[sent].add(text)

* Calculate percentages and print the results:

			total = sum(len(i) for i in sentiments.values())

			perc_pos = len(sentiments["positive"]) / total * 100
			perc_neg = len(sentiments["negative"]) / total * 100
			perc_neu = len(sentiments["neutral"]) / total * 100

			print("Analyzed {} tweets".format(total))
			print("Positive: {:.2f}%".format(perc_pos))
			print("Negative: {:.2f}%".format(perc_neg))
			print("Neutral: {:.2f}%".format(perc_neu))

### The verdict

People talk mostly positive about the movie:

	$ time python sentiment.py data_1487581986.json
	Analyzed 10053 tweets
	Positive: 33.85%
	Negative: 13.86%
	Neutral: 52.29%

Would be nice to break this down further, maybe by region. We wanted to look at gender, but this data was not provided by the Twitter API. 

### Some anonymous examples

We peaked at some tweets for validation. As you see it's not 100% correct (doubts marked with '?'), but it does give you a good indication:

	neutral
	-- 50 shades darker though.. oouuu. 🙆🏽
	-- ❤🤴🏼❤ — watching 50 shades darker...
	-- still don't know what to think of 50 shades darker🤔🤔
	---

	positive
	-- can't get over how amazing 50 shades darker is 😍
	-- i enjoyed 50 shades darker very much
	?-- that 50 shades darker was kind of sorry
	---

	negative
	?-- still haven't seen 50 shades darker :(  
	-- 50 shades darker might be the worst movie i've ever seen ...
	-- 50 shades darker was terrible god i wish i could get those 2 hours back
	---

## Further reading

[This great article by Real Python](https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/) shows another Twitter Sentiment Analysis example adding Docker, Elasticsearch, Kibana to the mix. 

## Feedback

What was your solution? Feel free to share in the comments below.

We hope you enjoy these challenges. Please provide us feedback if we can improve anything ...

If you have an interesting challenge you want us to feature, don't hesitate to reach out to us.

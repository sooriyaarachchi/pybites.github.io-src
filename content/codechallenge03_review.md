Title: Code Challenge 03 - PyBites blog tag analysis - Review
Date: 2017-01-27 9:00
Category: Challenges
Tags: code challenges, code review, github, learning, tags, similarity, blog
Slug: codechallenge03_review
Authors: PyBites
Summary: It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge03.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pybites-code-challenges.png

It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge03.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## A possible solution

See [here](https://github.com/pybites/challenges/blob/solutions/03/tags.py) and commented below.

Some learnings:

* We use the stdlib to its fullest:

		from collections import Counter
		from difflib import SequenceMatcher
		from itertools import product
		import re

* We define constants at the top. We use maketrans to easily extend replacing multiple characters in the future:

		REPLACE_CHARS = str.maketrans('-', ' ')
		IDENTICAL = 1.0
		TOP_NUMBER = 10
		RSS_FEED = 'rss.xml'
		SIMILAR = 0.87

* We used a regular expression to show that you can. A better way would be to use a PyPI package like feedparser or BeautifulSoup (see further down). 
 
		TAG_HTML = re.compile(r'<category>([^<]+)</category>')

		def get_tags():
			"""Find all tags (TAG_HTML) in RSS_FEED.
			Replace dash with whitespace (REPLACE_CHARS)"""
			with open(RSS_FEED) as f:
				tags = TAG_HTML.findall(f.read().lower())
			return [tag.translate(REPLACE_CHARS) for tag in tags]
	
* For everything counting related you really want to use collections.Counter and its most_common method

		def get_top_tags(tags):
			"""Get the TOP_NUMBER of most common tags"""
			return Counter(tags).most_common(TOP_NUMBER)



* For similarities we were going to read up on [NLTK](http://www.nltk.org/) but stdlib has difflib.SequenceMatcher which makes this very easy (found [on Stackoverflow](http://stackoverflow.com/questions/17388213/find-the-similarity-percent-between-two-strings)). We gained quite some performance first matching the first char between tags, but this assumes the first char is always the same. If you don't want that, take that check out. We use itertools.product instead of a double for loop. Lastly yield makes get_similarities a generator which we find more Pythonic.

		def get_similarities(tags):
			"""Find set of tags pairs with similarity ratio of > SIMILAR"""
			for pair in product(tags, tags):
				# performance enhancements 1.992s -> 0.144s
				if pair[0][0] != pair[1][0]:
					continue
				pair = tuple(sorted(pair))  # set needs hashable type
				similarity = SequenceMatcher(None, *pair).ratio()
				if SIMILAR < similarity < IDENTICAL:
					yield pair


* The calling code was given, printing it here for completeness:

		if __name__ == "__main__":
			tags = get_tags()
			top_tags = get_top_tags(tags)
			print('* Top {} tags:'.format(TOP_NUMBER))
			for tag, count in top_tags:
				print('{:<20} {}'.format(tag, count))
			similar_tags = dict(get_similarities(tags))
			print()
			print('* Similar tags:')
			for singular, plural in similar_tags.items():
				print('{:<20} {}'.format(singular, plural))

* Tests pass:

		$ git checkout solutions
		$ python test_tags.py 
		...
		----------------------------------------------------------------------
		Ran 3 tests in 0.153s

		OK

---

## Code challenges != Python's 'preferably only one way'

We know '>>> import this' says: "There should be one-- and preferably only one --obvious way to do it." and usually there is. Yet for our challenges we encourage people to be creative and not stick to the template + tests per se (we improve the code challenge format as we learn ...). 

For example Jeffrey parses our feed directly in [his solution](https://gist.github.com/jrjames83/eeda4324116dde12ea8d45c47a151ab0) with requests and BeautifulSoup not stripping off the dash. This is great addition to our solution, using PyPI whenever you can is recommended. Also by parsing the live feed he created us a tool to run this check every now and then (thanks Jeffrey). We like to see different solutions.

## Any issues or feedback?

What did you learn this challenge? Feel free to share you code in the comments below. 

How are you experiencing these challenges? You like the format? What can we do differently and/or better?

## next(challenges)

Monday we will be back with a fresh new challenge, stay tuned ...

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/) if you already forked it.

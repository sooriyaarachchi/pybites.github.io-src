Title: Parsing Twitter Geo Data and Mocking API Calls by Example
Date: 2017-06-17 23:55
Category: Testing
Tags: twitter, API, mock, geo, data, unittest, pickle, tweepy, testing, 100days
Slug: twitter-api-geodata-mocking
Authors: Bob
Summary: ["Is this Bob or Julian?!"](https://twitter.com/anthonypjshaw/status/875275923930480641) ... yeah tweeting from our shared [@pybites Twitter account](https://twitter.com/pybites) can be confusing! So I made a little script to parse the location of our tweets. Then I extended it to make it testable. I wrote a [decorator](https://pybit.es/codechallenge14.html) to cache a couple of API outputs to be used with the unittest.mock patch decorator I learned about. A simple script turned into a good learning exercise. 
cover: images/featured/pb-article.png

["Is this Bob or Julian?!"](https://twitter.com/anthonypjshaw/status/875275923930480641) ... yeah tweeting from our shared [@pybites Twitter account](https://twitter.com/pybites) can be confusing! So I made a little script to parse the location of our tweets. Then I extended it to make it testable. I wrote a [decorator](https://pybit.es/codechallenge14.html) to cache a couple of API outputs to be used with the unittest.mock patch decorator I learned about. A simple script turned into a good learning exercise. 

### Practice leads to new discoveries
That's the cool thing: even a relatively easy exercise like parsing some Twitter data can grow into something more interesting when you extend your goals, in this case: "how to unittest an API?". I will do a dedicated article on mocking when I learn some more, but for now I wanted to share how I went about testing the Twitter API.

### 1. whotweeted.py 
First of all the script: [whotweeted](https://github.com/pybites/100DaysOfCode/blob/master/080/whotweeted.py): it uses `tweepy` to get the tweet meta data from the Twitter API and parses the country code (`try tweet.place.country_code ... `). 

If Spain it's me, if Australia it's Julian:

	$ python whotweeted.py https://twitter.com/pybites/status/875677559970770944
	Bob tweeted it out

	$ python whotweeted.py https://twitter.com/pybites/status/875639674244444160
	Julian tweeted it out

It raises some exceptions if we input or retrieve bad data. It makes the program longer but more robust: 

	$ python whotweeted.py https://twitter.com/KirkDBorne/status/876176282542891008
	Not a pybites tweet

	$ python whotweeted.py https://twitter.com/pybites/status/844092059988508673
	Location not set on tweet

	$ python whotweeted.py https://twitter.com/pybites/status/844092059988508abc
	Problem getting tweet:
	[{'code': 144, 'message': 'No status found with that ID.'}]

Note that tweet location is not enabled by default, you have to turn it on, see [here](https://support.twitter.com/articles/78525).

### 2. Use mocking to test API calls
This is cool but how can we test our assumptions? We don't want to call the API each time we run our unittests. Enter [mocking](https://stackoverflow.com/questions/2665812/what-is-mocking):

> In short, mocking is creating objects that simulate the behaviour of real objects.

I learned about the unittest.mock patch decorator which I use like this: 

	@patch.object(tweepy.API, 'get_status', return_value=get_tweet('AU'))
	...
	test
	...

	@patch.object(tweepy.API, 'get_status', return_value=get_tweet('ES'))
	...
	another test
	...

Test script is [here](https://github.com/pybites/100DaysOfCode/blob/master/081/test_whotweeted.py).

This imitates a `get_status` method call of the `tweepy.API` object. As `return_value` I load in one of Julian's/my tweets I pickled to a data directory. Not sure if I could have simplified this by using a library like [Faker](https://github.com/joke2k/faker). As I wanted the full `tweepy` response object I added a [cache decorator](https://github.com/pybites/100DaysOfCode/blob/master/080/whotweeted.py) in `whotweeted` to cache (pickle) response data (TODO: put this code in a separate setup script).

The test script is not only much faster (no internet dependency/ latency), you also prevent repeated calls to the API (not sure for Twitter, but some APIs have pretty strict quotas).

To learn more about mocking in Python, checkout the [mock object library](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch) or if you use pytest see [pytest-mock](https://pypi.python.org/pypi/pytest-mock). I have to practice some more with this, I will do a follow-up article on mocking at some point ...

---

Keep Calm and Code in Python!

-- Bob

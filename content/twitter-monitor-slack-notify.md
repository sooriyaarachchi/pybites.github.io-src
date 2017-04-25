Title: How to Write a Simple Slack Bot to Monitor Your Brand on Twitter
Date: 2017-04-25 11:00
Category: Tools
Tags: Twitter, Slack, Automation, monitoring, twython, TwythonStreamer, slacker, configparser, logging, brand, triggers
Slug: twitter-monitor-slack-notify
Authors: Bob
Summary: In this article I show you how to monitor Twitter and post alerts to a Slack channel. We built a nice tool to monitor whenever our domain gets mentioned on Twitter. The slacker and twython modules made this pretty easy. We also use configparser and logging.
cover: images/featured/pb-article.png

In this article I show you how to monitor Twitter and post alerts to a Slack channel. We built a nice tool to monitor whenever our domain gets mentioned on Twitter. The slacker and twython modules made this pretty easy. We also use configparser and logging.

This was [another script](https://twitter.com/pybites/status/854432856386420736) that came out of our [100DaysOfCode challenge](http://pybit.es/special-100days.html). 

The funny thing is that we started out using [mediatrigger.io](https://www.mediatrigger.io/) using a free trial, but soon we thought: 

> How difficult would it be to build this ourselves?

Not that much, in this article we show you how. 

By the way, if at some point you lack inspiration what to build next, apart from [joining our code challenges](http://pybit.es/pages/challenges.html), think about how you can scratch your own itch. When we do this we tend to stumble upon [interesting projects](http://pybit.es/flask-api-part2.html). We think it's the best way to learn.

With that said let's get coding!

## Requirements and Setup

We use [slacker](https://pypi.python.org/pypi/slacker/) and [twython](https://pypi.python.org/pypi/twython) so pip install them or pip install -r [requirements.txt](https://github.com/pybites/100DaysOfCode/blob/master/020/requirements.txt) (after creating [a virtual env](http://pybit.es/the-beauty-of-virtualenv.html)).

You will need Twitter API tokens and a Slack token. We wrote about the [Twitter API](http://pybit.es/tag/twitterapi.html) and [Slack](http://pybit.es/tag/slack.html) before. 

We use configparser to read these tokens in from a [config file](https://github.com/pybites/100DaysOfCode/blob/master/020/config.ini-example). Note we only store the template config file on GH, the real one [is ignored](https://github.com/pybites/100DaysOfCode/blob/master/020/.gitignore) to not reveal any secret info.

For Slack you need to [create a bot first](https://julbob.slack.com/apps/new/A0F7YS25R-bots) and add the bot to your designated channel.

## The code

You can get the full project [here](https://github.com/pybites/100DaysOfCode/tree/master/020) (as said it's part of [our 100DaysOfCode repo](https://github.com/pybites/100DaysOfCode)). Here I go over the script bit by bit:

* Imports and read config, setting the required tokens. 

		import configparser
		import logging

		from slacker import Slacker
		from twython import TwythonStreamer

		config = configparser.ConfigParser()
		config.read('config.ini')

		CONSUMER_KEY = config['Twitter']['cs_key']
		CONSUMER_SECRET = config['Twitter']['cs_secret']
		ACCESS_TOKEN = config['Twitter']['acc_token']
		ACCESS_SECRET = config['Twitter']['acc_secret']
		SLACK_TOKEN = config['Slack']["token"]

* We define some other constants. Note that CHANNEL includes the pound sign (#) and the domain to monitor is defined as a tuple (explained further down). The message is constructed to make it easy to go to the tweet and know who is tweeting:

		CHANNEL = '#pybites-mentions'
		DOMAIN = ('pybit', 'es')
		MSG = '''A new mention of {domain}:

		{user} (name: {name} / followers {followers}) tweeted:
		{tweet_text}

		Link to tweet: https://twitter.com/{user}/status/{tweet_id}
		'''

* Instantiate a Slacker object:

		slack = Slacker(SLACK_TOKEN)

* Set up logging if we need to debug anything on the remote server one day:

		logging.basicConfig(level=logging.DEBUG,
							format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
							datefmt='%m-%d %H:%M',
							filename='bot.log')


* A helper to create the message that shows up in our Slack channel: 

		def create_post(data):
			tweet_text = data['text']
			tweet_id = data['id_str']
			user = data['user']['screen_name']
			name = data['user']['name']
			followers = data['user']['followers_count']
			return MSG.format(domain='.'.join(DOMAIN),
							user=user,
							name=name,
							followers=followers,
							tweet_text=tweet_text,
							tweet_id=tweet_id)

* What really makes this solution cool is the [Streaming API](https://dev.twitter.com/streaming/overview). We also used it [here](http://pybit.es/codechallenge07.html). [TwythonStreamer](https://twython.readthedocs.io/en/latest/usage/streaming_api.html) makes it quite easy to start to monitor Twitter: 6 LOC in the docs, 10 LOC here, because we added exception handling, logging and posting to Slack:

		class MyStreamer(TwythonStreamer):
			''' https://twython.readthedocs.io/en/latest/usage/streaming_api.html '''

			def on_success(self, data):
				post = create_post(data)
				logging.debug(post)
				try:
					slack.chat.post_message(CHANNEL, post, as_user=True)
				except Exception as exc:
					logging.error('cannot post to channel: {}'.format(exc))

			def on_error(self, status_code, data):
				print('An error occurred: {}, exiting'.format(status_code))
				self.disconnect()

* Invoke the Streamer. Important note: pybit.es (one term) did not work so well, so we had to feed stream.statuses.filter 'pybit es' which works as a logical AND, see [here](https://dev.twitter.com/streaming/overview/request-parameters#track):

		if __name__ == "__main__":

			stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
								ACCESS_TOKEN, ACCESS_SECRET)

			# https://dev.twitter.com/streaming/overview/request-parameters#track
			stream.statuses.filter(track=' '.join(DOMAIN))

* Quite amazed how these modules abstract away a lot of complex stuff keeping the script lean. As we [wrote before](http://pybit.es/py-mistakes.html): don't re-invent the wheel.

## Deployment

I run this script on my server. Of course it might die and we want it to work 7x24, so I [included a small shell script](https://github.com/pybites/100DaysOfCode/blob/master/020/bot.sh) to respawn the process if it dies, a technique I learned from [my previous Slack bot](http://pybit.es/simple-chatbot.html).

### Result

Whenever our domain is mentioned we get an instant notification on Slack:

![pybites mentions channel]({filename}/images/pybites-mentions.png)

## What would you Slackify? 

For us this is a great form of monitoring (automation). I hope you've enjoyed this tour of how to interact with 2 APIs. It's not that difficult, yet the options are endless and you can build some really cool stuff.

### Go wild with APIs

On that note, 'Now is better than never' (Python Zen), because [this week's challenge](http://pybit.es/codechallenge16.html) is all about fiddling with Web APIs! Comment below if this inspired you to build something yourself, or [submit your code](https://github.com/pybites/challenges/blob/master/INSTALL.md) to our [challenges community branch](https://github.com/pybites/challenges/tree/community) via a PR.

---

Keep Calm and Code in Python!

-- Bob

Title: How we Automated our 100DaysOfCode Daily Tweet
Date: 2017-04-05 23:00
Category: Tools
Tags: twitter, automation, tools, 100days, logging, tweepy, pytz
Slug: 100days-autotweet
Authors: Bob
Summary: In this article I show you a way to automatically tweet your #100DaysOfCode Challenge progress. This saves you some extra time to focus on the coding. Isn't that all what matters?
cover: images/featured/pb-article.png

In this article I show you a way to automatically tweet your #100DaysOfCode Challenge progress. This saves you some extra time to focus on the coding. Isn't that all what matters?

This is day 007 of our [100 Days of Code](http://pybit.es/special-100days.html) challenge. You can follow along by forking [our repo](https://github.com/pybites/100DaysOfCode).

## Getting ready

You need pytz, tweepy and requests. You can [pip install -r requirements.txt](https://github.com/pybites/100DaysOfCode/blob/master/007/requirements.txt) if you cloned our repo (after cd-ing in 007). We recommend using [virtualenv](http://pybit.es/the-beauty-of-virtualenv.html) to isolate environments.

As explained [in a previous article](http://pybit.es/automate-twitter.html) you need to get a Consumer Key/Secret and Access Token (Secret) from Twitter. I added those to my .bashrc which I load in via os.environ in [config.py](https://github.com/pybites/100DaysOfCode/blob/master/007/config.py). There I also started a logging handler I use to log outgoing tweets and any exceptions that may occur.

## The main script

See [here](https://github.com/pybites/100DaysOfCode/blob/master/007/100day_autotweet.py) and below what I learned:

* As per PEP8 we import stdlib, followed by external modules and own project modules:

		import datetime
		import os
		import re
		import sys

		import requests
		import pytz

		from config import logging, api

* My server (see deployment below) runs on MT tz and I wanted to talk EMEA times. [Pytz (World Timezone Definitions for Python)](https://pypi.python.org/pypi/pytz) to the rescue: it made working with timezones very easy: 

		tz = pytz.timezone('Europe/Amsterdam')
		now = datetime.datetime.now(tz)
		start = datetime.datetime(2017, 3, 29, tzinfo=tz)  # = PyBites 100 days :)

* I define some constants in all capital letters with underscores separating words (PEP8). I start to like datetime: calculating dates is easy:

		CURRENT_CHALLENGE_DAY = str((now - start).days).zfill(3)
		LOG = 'https://raw.githubusercontent.com/pybites/100DaysOfCode/master/LOG.md'
		LOG_ENTRY = re.compile(r'\[(?P<title>.*?)\]\((?P<day>\d+)\)')
		REPO_URL = 'https://github.com/pybites/100DaysOfCode/tree/master/'
		TWEET_LEN = 140
		TWEET_LINK_LEN = 23

* Where would we be without requests? Here I get the LOG.md file from [our repo](https://github.com/pybites/100DaysOfCode), just a single line of code:

		def get_log():
			return requests.get(LOG).text.split('\n')

* I get the script title and day string from the line in LOG.md that matches the exact day string (today = '007'):

		def get_day_progress(html):
			lines = [line.strip()
					for line in html
					if line.strip()]

			for line in lines:
				day_entry = line.strip('|').split('|')[0].strip()
				if day_entry == CURRENT_CHALLENGE_DAY:
					return LOG_ENTRY.search(line).groupdict()

* I create the tweet. I added some code to shorten the script title if the total tweet size is too long:

		def create_tweet(m):
			ht1, ht2 = '#100DaysOfCode', '#Python'
			title = m['title']
			day = m['day']
			url = REPO_URL + day
			allowed_len = TWEET_LEN + len(url) - TWEET_LINK_LEN

			fmt = '{} - Day {}: {} {} {}'
			tweet = fmt.format(ht1, day, title, url, ht2)
			surplus = len(tweet) - allowed_len

			if surplus > 0:
				new_title = title[:-(surplus + 4)] + '...'
				tweet = tweet.replace(title, new_title)
			return tweet

* tweet_status() sends the tweet. We use the imported api object (from config.py) to send the tweet and we log an info if success, or error if any exception:

		def tweet_status(tweet):
			try:
				api.update_status(tweet)
				logging.info('Posted to Twitter')
			except Exception as exc:
				logging.error('Error posting to Twitter: {}'.format(exc))

* We drive the script under main (= if script is run directly/standalone, not imported by another module). I set up some variables to allow for testing / dry runs:

		if __name__ == '__main__':
			import socket
			local = 'MacBook' in socket.gethostname()
			test = local or 'dry' in sys.argv[1:]

* If test I use my local LOG file:

			if test:
				log = os.path.basename(LOG)
				with open(log) as f:
					html = f.readlines()
			else:
				html = get_log()

* If for some reason I don't get a valid return from get_day_progress() I abort the script, logging the error:

			m = get_day_progress(html)
			if not m:
				logging.error('Error getting day progress from log')
				sys.exit(1)

* I create the tweet. If dry run, I just log it, else it tweets automatically:

			tweet = create_tweet(m)
			if test:
				logging.info('Test: tweet to send: {}'.format(tweet))
			else:
				tweet_status(tweet)

## Deployment

On my server I had to do some magic to get it all working: source .bashrc to load in the ENV vars, export PYTHONPATH, and specify the full path to python3. [As explained here](http://unix.stackexchange.com/a/27291): "Cron knows nothing about your shell; it is started by the system, so it has a minimal environment."

	$ crontab -l
	...
	34 14 * * * source $HOME/.bashrc && export PYTHONPATH=$HOME/bin/python3/lib/python3.5/site-packages && cd $HOME/code/100days/007 && $HOME/bin/python3/bin/python3.5 100day_autotweet.py

## Result

What a coincidence: as I write this our [today's progress tweet just went out](https://twitter.com/pybites/status/849721815538712576) :)

![my automated tweet]({filename}/images/auto-tweet.png)

## Logging

The cool thing about the logging module is that you get the external packages' logging for free. When I look at the log I see a lot more than my script's logging:

	$ vi 100day_autotweet.log
	...
	...
	14:34:02 tweepy.binder INFO     PARAMS: {'status': b'#100DaysOfCode - Day 007: script to automatically tweet 100DayOfCode progress tweet https://github.com/pybites/100DaysOfCode/tree/master/007 #Python'}
	...
	many more log entries ...
	...
	14:34:02 requests.packages.urllib3.connectionpool DEBUG    https://api.twitter.com:443 "POST /1.1/statuses/update.json?status=%23100DaysOfCode+-+Day+007%3A+script+to+automatically+tweet+100DayOfCode+progress+tweet+https%3A%2F%2Fgithub.com%2Fpybites%2F100DaysOfCode%2Ftree%2Fmaster%2F007+%23Python HTTP/1.1" 200 2693
	14:34:02 root         INFO     Posted to Twitter ==> my message 

Of course you can mute these by raising the log level (INFO or higher) in logging.basicConfig ([config.py](https://github.com/pybites/100DaysOfCode/blob/master/007/config.py)). See [the docs](https://docs.python.org/3/library/logging.html) for more info.

---

I hope this taught you a bite of Python and it inspired you to automate your 100DaysOfCode and/or other tweets. Let us know how it goes ... Happy coding!

Keep Calm and Code in Python!

-- Bob

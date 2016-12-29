Title: Automate Tweeting: how to build a Twitterbot
Date: 2016-12-29 1:28
Category: Tools
Tags: twitterapi, tweepy, feedparser, rss, logging, podcasts, virtualenv, pyvenv, venv, news, 3.6
Slug: automate-twitter
Authors: Bob
Summary: In this post I will show you how we automate part of our Twitter posting using feedparser and tweepy.
cover: images/featured/automate-twitter.png

## Motivation

I re-used my Twitter bot script of [How to create a simple Twitter bot with Python](http://bobbelderbos.com/2016/06/twitter-bot/). The main goal was to auto-tweet each new post of our blog, but while I was at it I decided to 'watch' a couple of feeds more. Follow [@pybites](https://twitter.com/pybites) to get our updates and other good Python news / content ...

# Getting ready

To auto-post to Twitter you need to get a Consumer Key/Secret and Access Token (Secret) from [https://apps.twitter.com](https://apps.twitter.com), my [previous post](http://bobbelderbos.com/2016/06/twitter-bot/) explains this in more detail (it's pretty easy).

## Feeds

Probably the best site to follow Python news feeds is [Planet Python](http://planetpython.org/), yet for this exercise I found reposting [20+ new links](http://planetpython.org/titles_only.html) a day too much (not another spam bot please!), so I decided to watch these 7:

~~~~
# more feeds 
http://pybit.es/feeds/all.rss.xml
https://talkpython.fm/episodes/rss
https://pythonbytes.fm/episodes/rss
https://dbader.org/rss
https://www.codementor.io/python/tutorial/feed
http://feeds.feedburner.com/PythonInsider
http://www.weeklypython.chat/feed/
~~~~

* I wanted to include [Python Weekly](http://www.pythonweekly.com), but could not find an RSS feed, probably because it's an email service. 

* Need to say it: [Talk Python To Me](https://talkpython.fm/) is awesome, a podcast every Python developer should listen to!

## Code

Code and install instructions (if you want to re-use this) are [on Github](https://github.com/pybites/blog_code/tree/master/twitter_bot). Basically I parse the feeds file above, use [feedparser](https://pypi.python.org/pypi/feedparser) to get the articles for each feed that were published less than 24 hours ago, and use [tweepy](http://www.tweepy.org) to post these to Twitter. 

I hide config.py in .gitignore and provide a blank config.py-example under version control. This is to hide the Twitter key/token stuff. As I run this in a daily cronjob, I turned on [logging](https://docs.python.org/3.6/library/logging.html) for debugging.

All together pretty impressive that you can do all this in just 67 LOC, mainly because we use [PyPI](https://pypi.python.org).

## Env / dependencies

I developed this in a [virtual environment](http://pybit.es/the-beauty-of-virtualenv.html), so a good practice I adopted is to ship the code with [a requirements file](https://github.com/pybites/blog_code/blob/master/twitter_bot/requirements.txt) which I obtained with: 

~~~~
(venv) $ pip freeze > requirements.txt
~~~~

Now you can get this script running simply by cloning my env:

~~~~
$ virtualenv venv [1]
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
~~~~

[1] I was going to say: use pyvenv instead of virtualenv, but [since 3.6](https://docs.python.org/dev/whatsnew/3.6.html) the recommended way is [python3 -m venv](https://docs.python.org/dev/whatsnew/3.6.html#id7).

## Result

Here is a filter of this morning's run where we caught our last post, a new Talk Python podcast episode and a nice new post from Dan Bader:

~~~~
# grep posted pybites_twitter.log 
04:55:54 root         DEBUG    posted status Learning from Python mistakes http://pybit.es/py-mistakes.html #python to twitter
04:55:57 root         DEBUG    posted status #91 Top 10 Data Science Stories of 2016 https://talkpython.fm/episodes/show/91/top-10-data-science-stories-of-2016 #python to twitter
04:56:00 root         DEBUG    posted status The Difference Between “is” and “==” in Python https://dbader.org/blog/difference-between-is-and-equals-in-python #python to twitter
~~~~

Automating Twitter :)

![auto-tweets]({filename}/images/auto-tweets.png)

## Logging all-in

Another cool thing about the [logging module](https://docs.python.org/3.6/library/logging.html) is that you get the imported packages logging for free. The following entries in my log files were not added by the code I wrote, they came from tweepy and/or feedparser and/or their dependencies!

~~~~
# more pybites_twitter.log |cut -d' ' -f2|sort|uniq -c |sort -nr
...
     15 requests_oauthlib.oauth1_auth  
     15 oauthlib.oauth1.rfc5849
      6 requests.packages.urllib3.connectionpool
      3 tweepy.binder
~~~~

## Deployment

Daily cronjob on server. I needed to export the site-packages path defined in PYTHONPATH:

~~~~
0 2 * * * export PYTHONPATH=/path/to/python3.5/site-packages && cd /path/to/twitter_bot && /path/to/python3.5 tweetbot.py
~~~~

TODO: checkout if [Python's sched](https://docs.python.org/3.6/library/sched.html) is a better alternative?

## Conclusion 

Again, [using PyPI](https://pypi.python.org) you save yourself a lot of coding (= time).

In just 67 LOC I could built a complete Twitterbot that will auto-post our new blog posts as well as some other good Python blogs and podcasts. We might add a few more feeds but this will do for starters.

Tests?! Yeah I know ... as I am writing this I am adding some tests using (learning) [pytest](http://doc.pytest.org/en/latest/) (I used unittest so far). I will blog about this framework in an upcoming post ...

---

Any suggestion of feedback use the comments below. Thanks for reading.

And to get our latest posts and other good Python content follow [@pybites](https://twitter.com/pybites).

---

Keep Calm and Code in Python!
 
-- Bob

Title: Code Challenge 06 - When does PyPI reach 100K packages? - review
Date: 2017-02-17 16:00
Category: Challenges
Tags: codechallenges, code review, learning, pypi, prediction, scipy, numpy, matplotlib
Slug: codechallenge06_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge06.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pybites-code-challenges.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge06.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Possible solutions / learning

### 1. Moving average using PyPI's RSS

My first approach was to take the [PyPI New RSS feed](https://pypi.python.org/pypi?%3Aaction=packages_rss) and take the average of time between adding packages. The script is [here](https://github.com/pybites/challenges/blob/solutions/06/pypi100k.py). The problem though is that the RSS feed has only 40 items, not much data. However when I put it in a cronjob and left it running for a week I got pretty similar results: it will happen somewhere at the beginning of March:

	# egrep "Now there are|Result" pypi.log
	2017-02-09 16:09:13,370 [MainThread  ] [INFO ]  Now there are 98435 packages
	2017-02-09 16:09:13,432 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-02-25 13:52:23.701848
	2017-02-09 22:37:59,725 [MainThread  ] [INFO ]  Now there are 98448 packages
	2017-02-09 22:37:59,760 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-03 01:41:22.733771
	2017-02-10 15:57:03,381 [MainThread  ] [INFO ]  Now there are 98513 packages
	2017-02-10 15:57:03,419 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-02-26 03:50:38.528795
	2017-02-10 19:25:43,787 [MainThread  ] [INFO ]  Now there are 98516 packages
	2017-02-10 19:25:43,819 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 13:04:22.486678
	2017-02-10 19:26:20,625 [MainThread  ] [INFO ]  Now there are 98516 packages
	2017-02-10 19:26:20,657 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 13:04:59.557107
	2017-02-10 19:27:11,201 [MainThread  ] [INFO ]  Now there are 98516 packages
	2017-02-10 19:27:11,232 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 13:05:49.999321
	2017-02-10 19:27:16,485 [MainThread  ] [INFO ]  Now there are 98516 packages
	2017-02-10 19:27:16,517 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 13:05:55.404488
	2017-02-10 19:27:55,974 [MainThread  ] [INFO ]  Now there are 98516 packages
	2017-02-10 19:27:56,006 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 13:06:34.758824
	2017-02-11 15:57:03,526 [MainThread  ] [INFO ]  Now there are 98555 packages
	2017-02-11 15:57:03,575 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-09 23:10:14.631885
	2017-02-12 15:57:03,219 [MainThread  ] [INFO ]  Now there are 98614 packages
	2017-02-12 15:57:03,259 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-05 22:31:50.575452
	2017-02-13 15:57:03,029 [MainThread  ] [INFO ]  Now there are 98686 packages
	2017-02-13 15:57:03,071 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-02-27 07:02:47.599206
	2017-02-14 15:57:03,683 [MainThread  ] [INFO ]  Now there are 98791 packages
	2017-02-14 15:57:03,738 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-02-21 20:41:34.775090
	2017-02-15 15:57:03,004 [MainThread  ] [INFO ]  Now there are 98866 packages
	2017-02-15 15:57:03,048 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-02-25 00:01:30.304754
	2017-02-16 15:57:02,965 [MainThread  ] [INFO ]  Now there are 98942 packages
	2017-02-16 15:57:03,001 [MainThread  ] [INFO ]  Result (NOW + time till reach): 2017-03-01 12:52:38.659931

Another source to use if you go this route is [PyPI's XML-RPC methods](https://wiki.python.org/moin/PyPIXmlRpc).

### 2. Using scipy.interpolate on Webarchive data

I was pointed to the [Web Archive](http://web.archive.org/web/20131025235716/https://pypi.python.org/pypi) on [Reddit](https://www.reddit.com/r/learnpython/comments/5trx9z/challenge_when_does_pypi_reach_100k_packages/). This is how you get snapshots of the PyPI page over time == a set of date points and how many packages there were at each time.

	$ python -m venv venv && source venv/bin/activate
	$ pip install waybackpack
	# take 4 years of data (half a GB, delete when done)
	$ waybackpack https://pypi.python.org/pypi -d pypi-snapshots --from-date 20130214 --to-date 20170214
	# few days when by, adjusted end date to 20170217 today
	#
	# prep the data
	$ cd pypi-snapshots
	# sometimes unix is all you need ;)
	$ find . -name 'pypi'|xargs grep "<strong>[0-9][0-9]*</strong>"| perl -pe 's/.*?(\d+)\/.*<strong>(\d+)<\/strong>/\1:\2/g' > ../data.txt
	$ head -2 data.txt
	20130214002304:28061
	20130216031420:28108
	$ tail -2 data.txt
	20170215124232:98825
	20170216124236:98907

This data (and all scripts) are in the [solutions branch](https://github.com/pybites/challenges/tree/solutions/06).

I made [this notebook](https://github.com/pybites/challenges/blob/solutions/06/pypi_pred_webarchive.ipynb) with the analysis. I used [scipy.interpolate - UnivariateSpline](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline) to do the extrapolation, I found this [here](http://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range) (Joma's answer).

## My prediction

As you can see from the notebook I am getting at this time of writing: 1st of March 8:37 pm, first of the month, a nice date and quite in line with the first method.

![the result]({filename}/images/pypi100k.png)

## Feedback

What was your solution? We are happy to hear in the comments below.

We hope you enjoy these challenges. Please provide us feedback if we can improve anything ...

If you have an interesting challenge feel free to reach out to us.

## next(challenges)

Next week we return to the Twitter API to do a sentiment analysis! Stay tuned ...

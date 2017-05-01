Title: Code Challenge 17 - Never Miss a Good Podcast
Date: 2017-05-01 11:00
Category: Challenges
Tags: codechallenges, learning, podcast, feedparser, SQLite, sqlite3, mail, cron
Slug: codechallenge17
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we'll let you import a Podcast feed, store it in SQLite, and email unplayed episodes at a regular interval. Inspiration [here](https://twitter.com/clickdroid/status/857245545185722368). Enjoy!
cover: images/featured/pb-challenge.png

> There is nothing like a challenge to bring out the best in man. - Sean Connery

Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we'll let you import a Podcast feed, store it in SQLite, and email unplayed episodes at a regular interval. Inspiration [here](https://twitter.com/clickdroid/status/857245545185722368). Enjoy!

##The Challenge

Of course [Talk Python](https://talkpython.fm/) is a good use case or [another Python Podcast](https://dbader.org/blog/ultimate-list-of-python-podcasts), but take any podcast you want. 

We want to keep the challenges as open as possible: [last two times](http://pybit.es/pages/challenges.html) that worked pretty well, and [our poll on Twitter](https://twitter.com/pybites/status/857520323956289536) showed the same:

![our challenge poll]({filename}/images/poll_result.png)

However even free form needs some structure to talk the same language. That's why we'd like you to try the following: 

* Pick your favorite podcast and find its feed.

* You can probably use [feedparser](https://pypi.python.org/pypi/feedparser) to easily parse the feed. Don't re-invent the wheel here, use [PyPI](https://pypi.python.org/pypi).

* Load the data into SQLite or some other [persistence form](https://docs.python.org/3.6/library/persistence.html). We recommend the [sqlite3](https://docs.python.org/3.6/library/sqlite3.html) module though: it is stdlib and easy to use. For starters we recommend [this article](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html).

* Mark the episodes as unplayed.

* Figure out how to email from your env. We wrote about this [here](http://pybit.es/python-smtplib.html) and [here](http://pybit.es/python-MIME.html).

* Figure out how to use cronjob in your env or do it with Python (see [sched](https://docs.python.org/3.6/library/sched.html) or [schedule](https://github.com/dbader/schedule)).

* Set up one or two jobs to: A) send a daily (or weekly) email with podcast link(s) for you to consume, and B) update the DB with new episodes.

* Mark the episode(s) as played (done) in the DB.

Bonus:

* As this is code challenge towards a podcast challenge ("listen all episodes of podcast x"), show some stats in each email, for example: "x % done (y out of z)".

---

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking. 

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). Cool PRs will be featured in our end-of-the-week challenge review.

## Archive

You can find all our code challenges so far [here](http://pybit.es/pages/challenges.html). If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

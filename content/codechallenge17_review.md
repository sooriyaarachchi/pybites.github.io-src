Title: Code Challenge 17 - Never Miss a Good Podcast - Review
Date: 2017-05-07 23:59
Category: Challenges
Tags: codechallenges, learning, podcast, feedparser, SQLite, sqlite3, mail, cron, review
Slug: codechallenge17_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge17.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Never Miss a Good Podcast](http://pybit.es/codechallenge17.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Solutions

Wow, this challenge led to some great learning! We got 3 Pull Requests (PRs) which we just merged into our Community branch. Don't want to miss your favorite podcast anymore? Here are some solutions that get you started:

* [clamytoe](https://github.com/clamytoe) built "Podcaster" providing a rich command line interface. Really nice documentation (lot of screenshots) in his README. It uses SQLAlchemy for the back-end and click for the CLI interface (good reminder we need to check this module out!). Another nice feature is that it lets you download episodes. Code is [here](https://github.com/pybites/challenges/tree/community/17/clamytoe).

* [cverna](https://github.com/cverna) wrote a script that fetches the feed of podcastinit.com (keep it Python!) - all nicely done in one script using sqlite3 and feedparser. Cron is done at the OS level (/etc/cron.weekly). Code is [here](https://github.com/pybites/challenges/tree/community/17/cverna).

* [jhervas](https://github.com/jhervas) wrote "Personal Podcast Assistant": a script that will manage a database with your favourite podcasts, notifying you by email when it finds new podcasts. It uses the schedule module for cron (schedule.every().wednesday.at("10:52").do(main) - nice). The script even tries to install the required packages. Code is [here](https://github.com/pybites/challenges/tree/community/17/jhervas).

* We used feedparser to parse a podcast feed which can be given with the --feed option. We also used SQLAlchemy to keep track of episodes and status (done = emailed out). We also print some stats at the bottom of each mail (e.g. "Podcast consumption stats: 0.9% done \[1 of 111\]"). We tried to make the code modular (package) and wrote some tests. Code is [here](https://github.com/pybites/challenges/tree/community/17/bbelderbos)

Best way to learn is to play around with these projects doing a git pull of the Community branch.

---

Again we really enjoyed these nice solutions and we are pumped to deliver more challenges so you can learn by building cool stuff. 

Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...

Title: Code Challenge 23 - Challenge Estimated Time API
Date: 2017-06-13 11:20
Category: Challenges
Tags: codechallenges, APIs, Github, Slack, Flask, tracking, meta, data, platform
Slug: codechallenge23
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we will give you the opportunity to enhance our challenge platform by creating a simple API to track how much time our challenges take (and possibly other metadata).
cover: images/featured/pb-challenge.png

> A smooth sea never made a skilled sailor. - Franklin D. Roosevelt

Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we will give you the opportunity to enhance our challenge platform by creating a simple API to track how much time our challenges take (and possibly other metadata).

Why? To quote one of our challenge takers: 

> Just wanted to say thanks for accepting my PR last week. My first one! I also have a request for the challenges. One of the reasons I am doing these challenges is to improve how efficiently I can write code. At the moment I have a timer on from starting up my venv to the end of unit testing. I'm recording these times each week to see if I improve. I was wondering if you could put a suggested time in the challenge readme. Almost like the 'suggested reading time' Medium have on their articles. 

And we got similar inqueries. We saw that adding reading times to our articles was something our audience really liked. Now challenges take a lot more investment of one's time than reading an article, so it does make sense to work on this feature. 

Estimating the time it takes to do a code challenge however is inherently difficult. People have different levels of experience and the the [open nature](https://twitter.com/pybites/status/857520323956289536) of our challenges allows for different levels of effort.

At least as we get some indication from an increasing amount of participants we can average the data making [our challenges page](https://pybit.es/pages/challenges.html) more informative.

## The challenge

* Basic: make a simple class or API to track and persistently save (e.g. SQLite, Google docs) challenge estimated times (minutes). 

* Intermediate: allow the user to save more attributes about the challenges: difficulty level (1-10), rating (1-5), could complete (True/False).

* Advanced: authenticate with the [Github API](https://developer.github.com/v3/) so we only get real user data. This makes sense because challenge participants == GH users. This also allows you to add validation: user to enter data once per challenge and CRUD: user being able to update what he/she entered. 

* Advanced part II: another idea we really like is making a private Slack for our community and participants could enter this meta data into a dedicated channel. If you like this option you could code something up using the [Slack API](https://api.slack.com/).

As usual you are free to pick the tools you want: Flask, Django, ..., or just vanilla Python. 

## Make our code challenges better!

We challenge you to try to finish all 3 levels providing a complete solution for our PyBites community. Note this could be an integral part of our challenges platform moving forward! Pretty exciting, no?

The best solution not only gets featured on our weekly review, but also on the [challenges page](https://pybit.es/pages/challenges.html) (one of the most visited page on our blog). That is, when it collected enough data we are happy integrating it.

## Additional resources

Here are some similar topics you can reference while taking this challenge:

* Flask is one way to do this, we wrote this article some time ago: [How To Build a Simple API with Flask and Unit Test it](https://pybit.es/simple-flask-api.html).

* A similar tracking app we wrote: [Simple API Part 2 - Building a Deep Work Logger with Flask, Slack and Google Docs](https://pybit.es/flask-api-part2.html).

* This is similar to [Code Challenge 08 - House Inventory Tracker](https://pybit.es/codechallenge08.html), reviewed [here](https://pybit.es/codechallenge08_review.html).

* If you go the Slack route you can check out: [How to Build a Simple Slack Bot](https://pybit.es/simple-chatbot.html).

---

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

## Feedback

If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

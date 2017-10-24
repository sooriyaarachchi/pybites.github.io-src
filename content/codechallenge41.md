Title: Code Challenge 41 - Daily Python Tip Part 2 - Build an API
Date: 2017-10-30 09:00
Category: Challenge
Tags: Daily Python Tip, Django, Flask, Bottle, API
Slug: codechallenge41
Authors: PyBites
Summary: Hi Pythonistas, you heard of [Daily Python Tip](https://twitter.com/python_tip)? It's a Twitter account that posts one python tip per day, run by [@karlafej](https://twitter.com/karlafej) and [@simecek](https://twitter.com/simecek). We partnered up with them and use their awesome collection of tips to build a web app (part 1) and a simple API (part 2).
cover: images/featured/pb-challenge.png
status: draft

> It's not that I'm so smart, it's just that I stay with problems longer. - A. Einstein

Hi Pythonistas, you heard of [Daily Python Tip](https://twitter.com/python_tip)? It's a Twitter account that posts one python tip per day, run by [@karlafej](https://twitter.com/karlafej) and [@simecek](https://twitter.com/simecek). We partnered up with them and use their awesome collection of tips to build a web app (part 1) and a simple API (part 2).

## The Challenge

If you built a web app for [part 1](https://pybit.es/codechallenge40.html) you could use its data / backend. If not just use the *Daily Python Tip*'s backend. We want this challenge to be independent so API lovers are not required to build a web app first.

The goal is to make a simple API using Flask, Django Rest Framework of another (Python) framework. Something the guys at *Daily Python Tip* could actually use!

HTTP verbs / actions:
- GET -> here is [their google spreadsheet](https://t.co/oARrOmrin7)
- POST -> here is [their Google form](https://docs.google.com/forms/d/e/1FAIpQLScsHklRH2-uplGYH_vxhtIin-zJS44bXQkAWCH7_N7nUdrGXw/viewform). "We are consenting adults" so we should prevent duplicates and bad data to be entered so you should add proper validation:
	- no duplicate postings,
	- max length of 140 characters (tips gets posted to Twitter),
	- discard new tips that are too similar to existing (this might be complex but give it some thought ...)

If you took part 1 and are using your own DB / backend you could also implement:
- PUT (edit) -> for example make the Published boolean editable
- DELETE -> not sure if applicable but could be used to remove bad data

## Bonus

1. Add Twitter login / authentication to your API so you can implement more actions:
- Only allow POST upon login
- Add your Twitter handle upon POSTing a new tip
- Make a user endpoint with likes, bookmarks, etc
- Be creative ...
2. Host it to the cloud (Heroku, PythonAnywhere, ...)

## Slack Channel

For a beginner some of our challenges might be overwhelming. Another observation is that the process of doing these challenges is as interesting as the final result.

We are eager to expand our awesome PyBites community. For this reason we are opening up our #codechallenges Slack channel for you to discuss our challenges as you code. Send us [an email](mailto:pybitesblog@gmail.com) if you want to join.

This way you get the opportunity to learn from other Pythonistas and share some of your own learning.

## Credit

To get credit PR your work to our Community branch of our [Challenges repo](https://github.com/pybites/challenges). See detailed instructions [here](https://github.com/pybites/challenges/blob/master/INSTALL.md).

## About

Our goal is to learn and teach you Python through practical exercises. Learning a programming language is way more fun as a community!

For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or [drop us an email](mailto:pybitesblog@gmail.com).

---

Keep Calm and Code in Python!

-- PyBites

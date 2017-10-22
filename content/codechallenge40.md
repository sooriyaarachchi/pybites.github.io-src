Title: Code Challenge 40 - Daily Python Tip Part 1 - Make a Web App
Date: 2017-10-23 09:00
Category: Challenge
Tags: Daily Python Tip, Django, Flask, Bottle, Twitter API, Tweepy
Slug: codechallenge40
Authors: PyBites
Summary: Hi Pythonistas, you heard of [Daily Python Tip](https://twitter.com/python_tip)? It's a Twitter account that posts one python tip per day, run by [@karlafej](https://twitter.com/karlafej) and [@simecek](https://twitter.com/simecek). We partnered up with them and use their awesome collection of tips to build a web app (part 1) and a simple API (part 2).
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, you heard of [Daily Python Tip](https://twitter.com/python_tip)? It's a Twitter account that posts one python tip per day, run by [@karlafej](https://twitter.com/karlafej) and [@simecek](https://twitter.com/simecek). We partnered up with them and use their awesome collection of tips to build a web app (part 1) and a simple API (part 2).

## The Challenge

The goal is to make a web app to make it easier to navigate the collection of tips:

1. Choose a web framework of your choice. Django, Flask, Bottle, use what you like. Make a new virtualenv and pip install it.
2. Make a scheduled job to sync the published tips to a DB from [their google spreadsheet](https://t.co/oARrOmrin7) or [their Twitter](https://twitter.com/python_tip) using a wrapper like Tweepy. Note some tweets have media attached, ideally you would retrieve those links as well. So pull the following fields: Timestamp, Python Tip, Link, Who Posted, Published (if > 1 link you probably need a second table with FK)
3. The tips don't always have hashtags so it might be hard to 'tag' them. That said you could set up routes like yourapp/numpy that retrieve all tips with that have 'numpy' in their body. This way you could make links on the homepage to common categories.
4. We think the best way to navigate them is to have a search box that just does a full text search.
5. As there are hundreds of tips you probably want to use pagination or lazy loading when you display them.

## Bonus

1. Use the Twitter API to retrieve the number of likes and retweets per tip and store those in the DB as well. Show the tips descending on popularity.
2. Provide a Twitter login so you can retweet tips to your Twitter account with one click.
3. Host it to the cloud (Heroku, PythonAnywhere, ...)

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

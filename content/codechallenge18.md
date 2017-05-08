Title: Code Challenge 18 - Get Recommendations From Twitter Influencers
Date: 2017-05-08 09:30
Category: Challenges
Tags: codechallenges, learning, Twitter, books, recommendations, API, TextBlob
Slug: codechallenge18
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we'll do another API exercise: you will parse your Twitter feed searching for book / movie / music / you-name-it recommendations. Can you create a simple [ParrotRead](https://parrotread.com)? Enjoy
cover: images/featured/pb-challenge.png

> There is nothing like a challenge to bring out the best in man. - Sean Connery

Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we'll do another API exercise: you will parse your Twitter feed searching for book / movie / music / you-name-it recommendations. Can you create a simple [ParrotRead](https://parrotread.com)? Enjoy

Ah what if you don't have or like Twitter?! Feel free to use any social media site where you can parse updates from people you follow or respect. Or use your favorite book service, for example [Goodreads](https://www.goodreads.com/).

##The Challenge

* Register an Twitter app and put the key/secret in a private (not under version control) config file or store them in env variables (os.environ). Again if using another API, follow similar steps.

* Make a virtual environment and pip install [Twython](https://twython.readthedocs.io/en/latest/), [Tweepy](http://www.tweepy.org/) or your favorite Twitter API module.

* Parse the updates from your followers. If you don't follow a lot of people you could also work with a set of predefined Twitter handles.

* Come up with a way to identify recommendations of your choice (books / movies / music / whatever you like).

* We want recommendations, so check if the updates are positive (check [this challenge](http://pybit.es/codechallenge07_review.html) where we used TextBlob, however use any tool you want).

### Optional

* Go beyond stdout by notifying the user either by tweet (already using the Twitter API so should be easy) or email (cache the results).

### Bonus

1. Tie this into a simple Flask app / front-end, [here](https://github.com/pybites/100DaysOfCode/tree/master/038) is some code to get Twitter login working in Flask.

2. Make it more intelligent. Ask the user for his/her preferences upfront and use an algorithm (k-means clustering maybe?) to make relevant recommendations.

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

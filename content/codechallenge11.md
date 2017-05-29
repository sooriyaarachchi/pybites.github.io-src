Title: Code Challenge 11 - Generators for Fun and Profit
Date: 2017-03-20 09:00
Category: Challenges
Tags: codechallenges, learning, generators, unix, newquote
Slug: codechallenge11
Authors: PyBites
Summary: A new week, a new 'bite' of Python coding! After [last week's article on generators](http://pybit.es/generators.html) we will get you to practice a bit more with them in our new challenge. Good luck and have fun.
cover: images/featured/pb-challenge.png

> There is nothing like a challenge to bring out the best in man. - Sean Connery

Hi Pythonistas, a new week, a new 'bite' of Python coding! 

After [last week's article on generators](http://pybit.es/generators.html) we will get you to practice a bit more with them.

Inspired by David Beazley's [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) we ask you to turn the following unix pipeline into Python code using generators. To get a bunch of .py files you can use our challenges repo you cloned. Or use a project of your own. 

Note that in our experience one subprocess is not necessarily one generator, for example 'sort|uniq|sort' can be easily combined into one, as well as 'grep|sed'. See [our template](https://github.com/pybites/challenges/blob/master/11/generators-template.py) if you need guidance.

	# assuming you pulled our challenges master and are in our 11/ subdirectory 
	# code this unix pipeline into Python using generators 
	#
	$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
	4 unittest
	4 sys
	3 re
	3 csv
	2 tweepy
	2 random
	2 os
	2 json
	2 itertools
	1 time
	1 datetime

Not familiar yet with Unix pipeline? It's pretty well explained [here](https://en.wikipedia.org/wiki/Pipeline_(Unix)).

### To follow along with our challenges (UPDATES)

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) which should contain everything you need to get up and running (any issue, please open a [GH Issue](https://github.com/pybites/challenges/issues)).

#### Update I) Forking

We got some feedback that Forks don't lead to activity on your Github profile. One of our followers was so nice to update [our INSTALL](https://github.com/pybites/challenges/blob/master/INSTALL.md) (via PR (Pull Request)). Maybe you want to use the workaround under III. if the credit thing is an issue for you. See [issue #2](https://github.com/pybites/challenges/issues/2) for more details.

#### Update II) Submit your Solution

We made [a new 'community' branch](https://github.com/pybites/challenges/tree/community). Another way to get credit is to submit your code via [a new PR](https://github.com/pybites/challenges/compare). We do not merge anything on our master or solutions branches, but if you ping us this way we add your solution to our new community branch (as filename 'topic-GHuser.py') and feature it in [our review](http://pybit.es/pages/challenges.html) if it taught us something cool.

### Code Challenges Archive

See [this page](http://pybit.es/pages/challenges.html) for all code challenges so far, if you have an interesting one you'd like to see featured [contact us](http://pybit.es/pages/about.html), open a [GH Issue](https://github.com/pybites/challenges/issues).

And last but not least: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions end of this week. Good luck and have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

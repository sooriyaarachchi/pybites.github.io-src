Title: Code Challenge 49 - Contribute to Open Source: Clean up Planet Python
Date: 2018-04-01 23:55
Category: Challenge
Tags: Planet, feedparser, RSS, parsing, hacking, scripting, community, debugging
Slug: codechallenge49
Authors: PyBites
Summary: Hi Pythonistas, it has been silent on the Community Blog challenges front, but then again we completed the [100 Days of Code in Python course](https://talkpython.fm/100days?s=pybites) which was a great milestone. Although less frequent, we will keep doing blog challenges though, not to worry! Let's start with a long pending item: cleaning up Python planets feeds, an interesting and valuable open source contribution.
cover: images/featured/pb-challenge.png

> It's not that I'm so smart, it's just that I stay with problems longer. - A. Einstein

Hi Pythonistas, it has been silent on the Community Blog challenges front, but then again we completed the [100 Days of Code in Python course](https://talkpython.fm/100days?s=pybites) which was a great milestone. Although less frequent, we will however,  keep doing blog challenges so not to worry! Let's start with a long pending item: cleaning up Python planets feeds, an interesting and valuable open source contribution.

## The Challenge

See [issue 233](https://github.com/python/planet/issues/233): there are a lot of feeds that are invalid or outdated. For this Challenge you're to write a script that does the cleaning as per requirements stated in the issue:

* Run weekly or monthly
* Iterate all urls on config.ini and also python libraries and python planets list
* Call each URL and assert (following redirects) -
	* Check return code is 200
	* Check data of last update is newer than one year
	* Check feed is valid using feedvalidator/podcastvalidator/othervalidator
* If not valid, store the URL in a simple database (text file, sqlite or something)
	* ACTION: If link returns bad status\invalid 3 times, remove from planet
	* ACTION: If feed is outdated for more than one year, keep in planet but remove from sidebar
	* ACTION: If feed is updated and not in sidebar, put it there again

### Bonus

Ours and potentially a lot of other feeds are not showing up due to what seems to be an SSL issue. Can you solve it and make a lot of Pythonistas happy? Check our inital debugging on [issue 135](https://github.com/python/planet/issues/135) and feel free to chime in (be warned though: might require some very old Python 2.x ...)
 
### Credit

Ready to contribute to this important Python news app? [PR your work via our platform](https://codechalleng.es/challenges/49) - valid PRs will receive our cool [PyBites Contributor Badge](http://codechalleng.es/badge/contributor) added to their dashboards. 

We are moving the review posts to a _featured view_ on our platform (audience > 1800 users and growing), PR and standby ... 

## PyBites Community

A few more things before we take off:

* Do you want to discuss this challenge and share your Pythonic journey with other passionate Pythonistas? Confirm your email on our platform then request access to our Slack via [settings](https://codechalleng.es/settings/).

* PyBites is here to challenge you because becoming a better Pythonista requires practice, a lot of it. For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or ping us on our Slack.

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!

Title: Code Challenge 23 - Challenge Estimated Time API - Review
Date: 2017-06-18 21:32
Category: Challenges
Tags: codechallenges, APIs, Github, PyGithub, PR template, tracking, meta, data, platform, packaging, peewee, click, maya
Slug: codechallenge23_review
Authors: PyBites
Summary: In this article we review last week's [Challenge Estimated Time API](http://pybit.es/codechallenge23.html). This was a cool challenge and we implemented it using Github's awesome platform and [API](https://developer.github.com/v3/).
cover: images/featured/pb-challenge.png

In this article we review last week's [Challenge Estimated Time API](http://pybit.es/codechallenge23.html). This was a cool challenge and we implemented it using Github's awesome platform and [API](https://developer.github.com/v3/).

### More than just parsing data

This challenge was two in one: 

1. We had to think about how to get data from our challenge takers.

2. We had to code up the processing of this data.

The first point took us a bit of brainstorming, but we stumbled upon [Github's PR template methodology](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/) we [happily embraced](https://github.com/pybites/challenges/commit/614b080a16da0b53187ebc93fd95239d18621c68) (yeah "Simple is better than complex").

The cool thing about this is that it puts the template in the comment field when you want to submit a PR:

![PR template upon PR]({filename}/images/pr-template1.png)

Of course you can just nuke the template, but we think this is the best we can get: the folks that do PRs are probably in the best position to provide input on these metrics. Secondly if you provide a Google doc a click is an extra step. Doing it this way it's part of the process you're already following.

Example of a filled in template in the PR submission: 

![PR template filled in]({filename}/images/pr-template2.png)

### Github API

For interacting with the Github API we used the [PyGithub](https://github.com/PyGithub/PyGithub) package which made this pretty easy (although it took some inspection of the various GH API endpoint objects to get to the relevant data).

The code: in [challenge_stats.py](https://github.com/pybites/challenges/blob/community/23/bbelderbos/challenge_stats.py) we get [our challenges repo](https://github.com/pybites/challenges) object with `get_challenge_repo`. From that we parse out the submissions with `get_submissions` in which we loop through all PRs: `for pr in challenge_repo.get_pulls('all')`. 

To get the code challenge number we cannot rely on the PR title. Looking at the PR files we see that they are like: *challenge_number/GH_USER/filename* (e.g. *23/bbelderbos/challenge_stats.py*) so we parse it from there.

In the `_parse_template_response` helper we parse the new feedback template with the help of [some regex](https://pybit.es/mastering-regex.html). We use a `defaultdict(dict)` to store user responses per challenge number. The advantages are: we don't have to initialize keys, and user responses are uniquified this way.

### Example

We only just used the template ourselves so we only have one response :)

Using `pprint` we can see the structure of the submissions defaultdict:

	$ python challenge_stats.py
	defaultdict(<class 'dict'>,
				{'23': {'bbelderbos': {'completed': True,
									'difficulty_level': '4',
									'estimated_time': '2',
									'i_stretched': True,
									'other_feedback': 'another test'}}})

That's where we leave it for now. This will be a handy script to get recorded stats of all PR submissions. When we have enough data, we can write some more code to parse these metrics and show (anonymous) averages on [our challenges page](https://pybit.es/pages/challenges.html).

### PR: PyTrack

We got a nice PR from [clamytoe (Martin)](https://github.com/clamytoe): *PyTrack*

> A simple project/task time tracker for Python 3.6.0+ 

[on community branch](https://github.com/pybites/challenges/tree/community/23/clamytoe) | [original repo](https://github.com/clamytoe/pyTrack/)

To quote the excellent Readme documentation: 

> Helps you keep track of how much time you spend on your projects and tasks. A sqlite database is used to track your time logs, and it is kept simple by only implementing as few commands as needed to get a full featured application. You can add/remove multiple projects, start/stop tracking any of them, or completely reset the database to start with a clean slate.

We like how this works as a stopwatch, just stop and start to track a project, and it stores all timings in a DB. 

It uses click for command line interface, maya for datetime parsing, and peewee for ORM, check out the code if you want to learn about these packages. 

Another nice aspect is that Matin refactored this into a package.

### Thanks for joining

Great work is coming out of these challenges, we are humbled and stoked creating our PyBites community this way!

You can start any challenge at any time, just follow [our instructions](https://github.com/pybites/challenges/blob/master/INSTALL.md) and start coding. Have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

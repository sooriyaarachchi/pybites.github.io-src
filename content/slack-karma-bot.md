Title: From Script to Project part 1. - Building a Karma Bot with Python and the Slack API
Date: 2017-06-25 20:00
Category: Tools
Tags: Slack, karma, bot, API, picle, packaging, logging, Counter
Slug: slack-karma-bot
Authors: Bob
Summary: We love Slack! But what if we can make it even cooler? Imagine: you are geeking out with your fellow developers on Slack and you want to give them credit. Or you can write "stupidsubject--" and it automagically shows "stupidsubject's karma decreased to -2". Enter *Karma Bot*. This is [nothing new](https://blog.hipchat.com/2016/05/02/meet-karma-bot/) but building one myself was a good learning exercise and will kick-start our series on packaging your code. 
cover: images/featured/pb-article.png

We love Slack! But what if we can make it even cooler? Imagine: you are geeking out with your fellow developers on Slack and you want to give them credit. Or you can write "stupidsubject--" and it automagically shows "stupidsubject's karma decreased to -2". Enter *Karma Bot*. This is [nothing new](https://blog.hipchat.com/2016/05/02/meet-karma-bot/) but building one myself was a good learning exercise and will kick-start our series on packaging your code. 

In this first article I will show you how I implemented our Karma Bot using Slack's [Real Time Messaging API](https://api.slack.com/rtm). This will be the groundwork to extend it into a more mature open source package over the next 8 weeks.

## From Script to Project Series

This is my idea for the coming articles, one a week, but I will update if progress warrants a better structure: 

1. You are reading now = [Karma Bot](https://github.com/pybites/karmabot) = theme app for fun and packaging
2. Modularize your code by creating packages
3. Writing tests for the Karma Bot, mocking Slack's API
4. Use Sphinx to provide your users with beautiful documentation 
5. Creating a Python project with Cookiecutter
6. Releasing your code to PyPI
7. Automated testing and deployment 
8. Github collaboration workflow for an Open Source project

## Setup

This exercise is similar to our [How to Build a Simple Slack Bot](https://pybit.es/simple-chatbot.html) article. First you create a bot user and get an API_KEY from Slack. 

The bot user needs to be defined as ID so you need to retrieve it for which I made a helper script:

	$ python3 -m utils.get_botid
	Bot ID for 'karmabot' is xyz

(This calls the get_botid.py script in the utils package. More on packaging next week ...)

Then I stored the following two env variables in my `bashrc`:

	export SLACK_KARMA_BOTUSER=xyz
	export SLACK_KARMA_TOKEN=super-secret

As we will see next week \_\_init\_\_.py makes a folder a package. You can use this file to do setup. I read env variables in, define my (regex) constants, instantiate the `SlackClient` object to talk to the Slack API, and setup logging and caching. See [\_\_init\_\_.py](https://github.com/pybites/karmabot/blob/master/bot/__init__.py).

## Structure

The code for this project is [here](https://github.com/pybites/karmabot).

The [main.py](https://github.com/pybites/karmabot/blob/master/main.py) script is the driver calling methods from the bot package (folder):

- It connects to the [Real Time Messaging API](https://api.slack.com/rtm) with `SLACK_CLIENT.rtm_connect()`.

- Each second it checks our Slack for new messages with the helper `parse_next_msg` ([karma.py](https://github.com/pybites/karmabot/blob/master/bot/karma.py)) which pings the API with `SLACK_CLIENT.rtm_read()` and parses the response.

- One of my favorite regex methods `findall` checks each new message for potential karma actions:

		karma_changes = KARMA_ACTION.findall(text)
	
	where: 
		
		KARMA_ACTION = re.compile(r'(?:^| )(\S{2,}?)\s?([\+\-]{2,})')

	This is a complex regex so let me break it down: 
	
	* start of message or preceding space 
	* two or more non-space characters
	* one optional space (convenient because Slack's autocomplete-select of username inserts one)
	* the voting component = two or more +'s and/or -'s (one + or - led to a lot of false positives!)

- [karma.py](https://github.com/pybites/karmabot/blob/master/bot/karma.py)'s `parse_karma_change` is then called to parse out giver, receiver and points. Giver and receiver are returned by the Slack API as IDs so I need [slack.py](https://github.com/pybites/karmabot/blob/master/bot/slack.py)'s `lookup_username` to convert them to usernames (which I cache in `USERNAME_CACHE`).

- Then [karma.py](https://github.com/pybites/karmabot/blob/master/bot/karma.py)'s `change_karma` is called to increase/decrease the karma and returns a message for the bot to post.

- Lastly `post_msg` ([slack.py](https://github.com/pybites/karmabot/blob/master/bot/slack.py)) is called to have the bot post the karma result message back to the same channel the original message (request) came from.

- To keep track of scores I use a `Counter` object which is stored to disk with `pickle`. This is setup in [\_\_init\_\_.py](https://github.com/pybites/karmabot/blob/master/bot/__init__.py):

		try:
			logging.info('Retrieving karma cache file')
			karmas = pickle.load(open(KARMA_CACHE, "rb"))
		except FileNotFoundError:
			logging.info('No cache file starting new Counter object in memory')
			karmas = Counter()

	... and is backed up every minute with:

		def _save_cache():
			pickle.dump(karmas, open(KARMA_CACHE, "wb"))

	I might actually turn this into a real DB.

## Deploy

When we built our first Slack bot for [How to Build a Simple Slack Bot](https://pybit.es/simple-chatbot.html) we needed a way to keep the bot alive even if it crashed or the process was terminated by the OS. For Karma Bot I went with the same workaround as then: a [run.sh](https://github.com/pybites/karmabot/blob/master/run.sh) wrapper that respawns. So if you want to use this code yourself, you would kick it off like this: 

	$ nohup ./run.sh &

## Example

Test session in private Karma Bot channel:

![karma example]({filename}/images/karma_example.png)

You need to invite the bot to any channel you want to use this in.

## Next week

My first attempt at this was one big script. I then splitted it out into different modules (responsabilities). Unfortunately I did not commit the initial script to compare. No worries though. Next week I go back to basics on modules and packaging, explaining how they work. I will explain how we import from them which often leads to confusion. We now have an interesting app to work with.

---

Keep Calm and Code in Python!

-- Bob

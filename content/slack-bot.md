Title: How to Build a Simple Slack Bot
Date: 2017-04-04 23:30
Category: Tools
Tags: slack, API, bot, chatbot, 
Slug: simple-chatbot
Authors: Bob
Summary: I was playing with Slack's Real Time Messaging API the other day. Building a bot is pretty easy. In this article a simple example.
cover: images/featured/pb-article.png

I was playing with Slack's Real Time Messaging API the other day. Building a bot is pretty easy. In this article a simple example.

This was an interesting coding exercise, but also keep in mind its relevance. Bots are hot, [people have become comfortable with conversational interfaces](http://www.oreilly.com/data/free/what-are-conversational-bots.csp?imm_mid=0ef9cf&cmp=em-data-free-na-ainy17_nurture_em2_what_are_conversational_bots). 

![some commands our bot listens to]({filename}/images/slackbot.gif)

(GIF made with [100DaysOfCode day 003 script](https://github.com/pybites/100DaysOfCode/tree/master/003))

---

About Slack's [Real Time Messaging API](https://api.slack.com/rtm):

> The Real Time Messaging API is a WebSocket-based API that allows you to receive events from Slack in real time and send messages as users. It's sometimes referred to as simply the "RTM API".  It is the basis for all Slack clients. It's also commonly used with the bot user integration to create helper bots for your team.

Read [here](https://api.slack.com/bot-users) about Bot Users, you need to [create a new bot user](https://my.slack.com/services/new/bot) first. This will give you an API Token. Keep this private! I added mine to .bashrc to keep it out of version control. I retrieve it like this:

	slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

Secondly you need to pip install slackclient, I also used [some other modules](https://github.com/pybites/slackbot/blob/master/requirements.txt).

I took the [starterbot code](https://github.com/pybites/slackbot/blob/master/starterbot.py) I found in this excellent article: [How to Build Your First Slack Bot with Python](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html). This made it a lot easier because it catered for all the initial setup, listening for mentions of the bot, intercepting targeted messages.

I wrote a bunch of scripts which repond to [different commands](https://github.com/pybites/slackbot/tree/master/commands), some also as part of our [100DaysOfCode challenge](http://pybit.es/special-100days.html). I put them in the commands subdirectory. This structure makes it easy to add more commands over time.

In the [main bot script](https://github.com/pybites/slackbot/blob/master/pybitesbot.py) I import all the commands: 

	from commands.mood import get_mood  # just a silly one
	from commands.special import celebration
	from commands.articles import get_num_posts
	from commands.challenge import create_tweet
	from commands.weather import get_weather  # bot reports more sun and later sunset Spain vs Australia (sorry Julian haha)

	# and put them in a COMMANDS dict
	cmd_names = ('mood', 'celebration', 'num_posts', '100day_tweet', 'weather')
	cmd_functions = (get_mood, celebration, get_num_posts, create_tweet, get_weather)
	COMMANDS = dict(zip(cmd_names, cmd_functions))

I then overwrote the (provided) handle_command function to have the bot respond to various commands. 

	def handle_command(cmd, channel):
		
		cmd = cmd.split()
		cmd, args = cmd[0], cmd[1:]

		if cmd in COMMANDS:
			if args:
				response = COMMANDS[cmd](*args)
			else:
				response = COMMANDS[cmd]()
		else:
			response = ('Not sure what you mean? '
				'I can help you with these commands:\n'
				'{}'.format('\n'.join(cmd_names)))

		slack_client.api_call("chat.postMessage", channel=channel,
							text=response, as_user=True)

Lastly under main this starts the loop:

	if slack_client.rtm_connect():
		...

And that's it for the code. On my server I run the bot with nohup to keep it running: 

	nohup python3 pybitesbot.py &

And there you go ... as you can see we had some fun with it the other day :)

![bot smart ass I]({filename}/images/slack_response1.png)

![bot smart ass II]({filename}/images/slack_response2.png)

---

Although this tutorial showed a simple deterministic bot, this really inspired me to think about ways we can make our pybitesbot smarter and help us automate tasks. Or what if we open up a Slack for our community and we have a bot helping people with common Python questions? That would be really cool! 

I will do a part 2 when we have more progress in this space ...

The full code of the bot is [here](https://github.com/pybites/slackbot). We encourage you to fork it and start building your own cool bot (and tell us about it in the comments below). 

---

Keep Calm and Code in Python!

-- Bob


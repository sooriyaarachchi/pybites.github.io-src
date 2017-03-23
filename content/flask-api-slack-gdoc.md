Title: Simple API Part 2 - Building a Deep Work Logger with Flask, Slack and Google Docs
Date: 2017-03-10 18:00
Category: Tools
Tags: Flask, Slack, Google docs, Heroku, APIs, pygsheets, git, commands, productivity, learning
Slug: flask-api-part2
Authors: Bob
Summary: After [Simple API - part 1](http://pybit.es/simple-flask-api.html) a more practical app in this part 2 tutorial: a Deep Work logger integrating Google docs and Slack, including deployment of the app to Heroku.
cover: images/featured/pb-article.png

After [Simple API - part 1](http://pybit.es/simple-flask-api.html) a more practical app in this part 2 tutorial: a Deep Work logger integrating Google docs and Slack, including deployment of the app to Heroku.

Sometimes you come across an article you think: "I definitely need to play with this!", enter [Google Spreadsheets and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).

I decided to make a Flask app to log the amount of deep work. Why? Read [the book](http://amzn.to/2ngahen), in short: it is a powerful success habit.

## Design 

So we have the API = Flask, the back-end = Google Docs. What about the interface? 

I wanted something for both laptop and mobile = Slack. Enter the [Slack API / Slash Commands](https://api.slack.com/slash-commands). I defined this super basic interface: 

	/dw <time> (<activity>)
	- /dw is the slack command
	- time can be an int (hour) or more specifically hh:mm
	- activity is optional, if not provided it defaults to the name of the channel 

## Step by step

Here is roughly what I did. I document it here so you can start building something similar to scratch your own itch. The code so far is [here](https://github.com/pybites/deepwork/).

* To be able to write to a Google Doc follow [Google Spreadsheets and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) to create an app via the Google API and obtain the client_secret.json file.

* pip install flask and pygsheets, implement GET and POST, again more details [here](https://github.com/pybites/deepwork/blob/master/api.py). I used Flask's [HTTP Basic Auth snippet](http://flask.pocoo.org/snippets/8/) to protect the GET. For the POST I verify the Slack token. As [good practice](https://12factor.net/config) I stored user/pw in (OS) env variables. I defined some helpers in [backend.py](https://github.com/pybites/deepwork/blob/master/backend.py). 

* Deploy the app to Heroku (Free plan), I was so glad [I took notes](http://bobbelderbos.com/2016/12/learning-flask-building-quote-app/) some time ago (section "Deployment to Heroku"). I captured the steps as good as I could [here](https://github.com/pybites/deepwork/blob/master/heroku.md) (I will adjust next time I deploy an app to Heroku).

* Deploying an app is a challenge in itself. For example how do you get the client_secret.json file in Heroku? I had to go with [this (not ideal) workaround](http://stackoverflow.com/questions/7908667/how-to-deploy-heroku-app-with-secret-yaml-configuration-file-without-committing).

		# put client_secret.json in .gitignore on master
		# commit it to secret-branch you keep between localhost and Heroku (not Github)
		...
		$ git push heroku secret-branch:master

* [Create a Slack app](https://api.slack.com/apps?new_app=1), then a [Slash Command](https://my.slack.com/services/new/slash-commands) where I defined: 

	* Command: /dw
	* URL = API endpoint on Heroku
	* Method = POST
	* Token = generated, I put that in env variable SLACK_DW_CMD_TOKEN above
	* You can set an Autocomplete help text which is useful to your team
	* This is the payload Slack sends to your API for consumption: 

			token=xyz
			team_id=T0001
			team_domain=example
			channel_id=C123
			channel_name=deepwork
			user_id=U123
			user_name=bbelderbos  -> cool: the app can be used by the whole team on Slack
			command=/dw
			text=your_entered_text
			response_url=https://hooks.slack.com/commands/1234/5678

		See the parsing of it in the *[post_entry](https://github.com/pybites/deepwork/blob/master/api.py)* method.

## The app in action

![the complete flow]({filename}/images/slackapi.png)

## Lessons learned

* Scratch your own itch. This was a nice exercise to integrate with apps I often use. It taught me a lot because I got stuck so had to debug. 

* For example Slack does not seem to use JSON so in my Flask I had to change request.json to request.form, using [ngrok](https://ngrok.com) speeded up the debugging.

* I lost quite some time struggling with gspread (used in the mentioned Twilio article) which was way too slow (2 min for a POST request?!), using [pygsheets](https://github.com/nithinmurali/pygsheets) response times went down to 1-2 seconds or less which made Slack, Heroku and me happy. Lesson: fail fast and small, compare different libraries, and obviously read article comments first before trying!

---

Keep Calm and Code in Python!

-- Bob

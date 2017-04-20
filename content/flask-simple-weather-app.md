Title: Simple Flask app to compare the weather of 2 cities 
Date: 2017-04-20 9:40
Category: Flask
Tags: Flask, weather, API, OpenWeatherMap, learning, Heroku, pytz, deploy, Jinja, CSS
Slug: flask-simple-weather-app
Authors: Bob
Summary: In this post I show you how to build a simple Flask app to compare the weather of 2 cities using the [OpenWeatherMap API](https://openweathermap.org). Maybe this aids you in solving [this week's challenge](http://pybit.es/codechallenge15.html). 
cover: images/featured/pb-article.png


Some nice things coming out of our [100DaysOfCode Challenge](http://pybit.es/special-100days.html). You seemed to like [this one](https://twitter.com/pybites/status/851896144594583552) so I decided to do an article on it.

In this post I show you how to build a simple Flask app to compare the weather of 2 cities using the [OpenWeatherMap API](https://openweathermap.org). Maybe this aids you in solving [this week's challenge](http://pybit.es/codechallenge15.html). 

![Our simple Flask app]({filename}/images/weather-app.png)

## Step by step

The full code is [here](https://github.com/pybites/weather_compare). We deployed the app [here](http://weathercompare.herokuapp.com/).

* First install dependencies we put in [requirements.txt](https://github.com/pybites/weather_compare/blob/master/requirements.txt).

		$ python -m venv venv && source venv/bin/activate
		$ pip install -r requirements.txt

* Get an API key from [OpenWeatherMap API](https://openweathermap.org/current) and store it in your environment
		
		$ vi .bashrc
		...
		export WEATHER_API=xyz

* Project code:

	* CSS goes into the static directory, our template into templates. [It contains](https://github.com/pybites/weather_compare/blob/master/templates/weather.html) a POST form to submit 2 cities and a table for the results of the query. The nice and simple design are thanks to [PureCSS](https://purecss.io/).

	* The [weather.py](https://github.com/pybites/weather_compare/blob/master/weather.py) gets the API_KEY from the OS env, sets up some other constants and defines two helpers: 
	
		1. get_local_time() -> tries to be as specific regarding timezone as possible, looking for both city and country. I had a good play with the pytz package here.

		2. query_api() queries the OpenWeatherMap API via requests

		3. With these helpers the [main app](https://github.com/pybites/weather_compare/blob/master/app.py) becomes pretty lean (just 32 LOC). I only use the root (/) path for both view and POST. If POST, I get the 2 cities from the form with request.form.get, I query the API for both cities appending the results to data. If data does not have 2 items we set the error variable. All the data gets passed to the weather html template with this: 

				return render_template("weather.html",
									data=data,
									error=error,
									time=get_local_time)

			Note that we can pass in a function as well: get_local_time() which we use [in the template](https://github.com/pybites/weather_compare/blob/master/templates/weather.html):
	
				<td>{{ time(d['sys']['sunrise'], d['sys']['country'], d['name']) }}</td>

## Deploy to Heroku

* I then [deployed the app](http://weathercompare.herokuapp.com/) and luckily took some notes. Prerequisite is installing [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

		(with your virtualenv enabled)

		$ pip install gunicorn

		$ pip freeze > requirements.txt
		$ echo "web: gunicorn <APP_FILE_NAME>:app" > Procfile
		$ echo "python-3.5.2" > runtime.txt
		$ git add . && git commit -m 'prep files heroku'

		$ heroku login
		Enter your Heroku credentials.
		Email: <your-email>
		Password (typing will be hidden):
		Logged in as <your-email>

		$ heroku create weathercompare
		Creating ⬢ weathercompare... done
		https://weathercompare.herokuapp.com/ | https://git.heroku.com/weathercompare.git

		$ heroku git:remote -a weathercompare
		set git remote heroku to https://git.heroku.com/weathercompare.git

		$ git remote -v
		heroku    https://git.heroku.com/weathercompare.git (fetch)
		heroku    https://git.heroku.com/weathercompare.git (push)

		$ heroku config:set WEATHER_API=XYZ
		Setting WEATHER_API and restarting ⬢ weathercompare... done, v3
		WEATHER_API: XYZ

		$ heroku ps:scale web=1

		$ git push heroku master
		Counting objects: 15, done.
		Delta compression using up to 4 threads.
		Compressing objects: 100% (9/9), done.
		Writing objects: 100% (15/15), 2.55 KiB | 0 bytes/s, done.
		Total 15 (delta 1), reused 0 (delta 0)
		remote: Compressing source files... done.
		remote: Building source:
		remote:
		remote: -----> Python app detected
		remote: -----> Installing python-3.5.2
		remote: -----> Installing pip
		remote: -----> Installing requirements with pip
		...
		...
		...
		remote: -----> Launching...
		remote:        Released v4
		remote:        https://weathercompare.herokuapp.com/ deployed to Heroku
		remote:
		remote: Verifying deploy... done.
		To https://git.heroku.com/weathercompare.git
		* [new branch]      master -> master

		# made a change? e.g. I added the CSS later, no problem, just deploy again

		$ git push heroku
		...
		remote: Building source:
		remote:
		remote: -----> Python app detected
		remote: -----> Installing requirements with pip
		remote:
		remote: -----> Discovering process types
		remote:        Procfile declares types -> web
		remote:
		remote: -----> Compressing...
		remote:        Done: 57.5M
		remote: -----> Launching...
		remote:        Released v7
		remote:        https://weathercompare.herokuapp.com/ deployed to Heroku
		remote:
		remote: Verifying deploy... done.
		To https://git.heroku.com/weathercompare.git
		c9771bb..77abb53  master -> master

---

I hope this inspired you to build your own mini Flask app using an API and putting it on Heroku. I hope I have convinced you this is pretty awesome stuff, not too hard to grasp, yet powerful if you further exploit its features. 

Leave a comment below if you want to share what you've built and/or join our [Flask Code Challenge](http://pybit.es/codechallenge15.html) of this week.

---

Keep Calm and Code in Python!

-- Bob

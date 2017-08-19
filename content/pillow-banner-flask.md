Title: Making a Banner Generator With Pillow and Flask
Date: 2017-08-19 13:00
Category: Tools
Tags: Pillow, Flask, banners, PyBites, promo, Heroku, codechallenges
Slug: pillow-banner-flask
Authors: Bob
Summary: In this article I will take [last week's banner.py Pillow script](https://pybit.es/pillow-banner-image.html) and integrate it into a Flask app. 
cover: images/featured/pb-article.png

In this article I will take [last week's banner.py Pillow script](https://pybit.es/pillow-banner-image.html) and integrate it into a Flask app.

I ended up creating our *PyBites Banner Generator*. Want to try it? The app is [on Heroku](https://pybites-banners.herokuapp.com/). Want to fork it? For example to use it with your own brand logos? The code is on [Github](https://github.com/pybites/pillow-flask).

## How it works

Give your banner a name, a background URL and text. We use PyBites logos upon login. Logged out state has a Python logo but I probably make this a free field so you can input any URL. Leaving "Use Second Image as Background" unchecked aligns the second image to the right:

![home logged out]({filename}/images/pyb-banner-generator1.png)

This results in:

![logged out banner]({filename}/images/pyb-banner-generator2.png)

Upon login it also caches the form input parameters to easily recreate the banners:

![home logged in]({filename}/images/pyb-banner-generator3.png)

So the same banner would turn into a PyBites one:

![banner with pybites article logo]({filename}/images/pyb-banner-generator4.png)

And the banner's form data can be retrieved again by clicking its name in the right "Cached Banners" list.

Let's make a Twitter digest banner. Ticking "Use Second Image as Background" turns it into background image:

![another banner with background]({filename}/images/pyb-banner-generator5.png)

Result:

![banner of pybites twitter digest]({filename}/images/pyb-banner-generator6.png)

## What's under the hood?

Here are the pieces that make up this app:

### Pillow

[Last week's article](https://pybit.es/pillow-banner-image.html) detailed the Pillow script `banner.py` which is in [the banner package](https://github.com/pybites/pillow-flask/tree/master/banner). The `generate_banner` takes a `img_banner` named tuple, instantiates a `Banner` object, and creates and saves the image. 

Since last time I added a `add_background` method which you saw in the 3rd example above. I also made `add_text` smarter about aligning text: if background is ticked it uses the extra free space to the right and if the text is less than 2 lines long (using Python's [textwrap](https://docs.python.org/3.6/library/textwrap.html)), it adds more top padding to it.

### Flask-WTF 

[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) integrates Flask and WTForms making working with forms a joy. 

In [forms.py](https://github.com/pybites/pillow-flask/blob/master/forms.py) I subclass wtforms's Form, read in the logos for the dropdown and added some validations using wtform's `validators`.

The form is diplayed in `imageform.html` and the `_formhelpers.html` helper in the [templates dir](https://github.com/pybites/pillow-flask/tree/master/templates) which I used from [this wtforms pattern](http://flask.pocoo.org/docs/0.12/patterns/wtforms/).

### Flask-SQLAlchemy

We have covered [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) [before](https://pybit.es/tag/flask-sqlalchemy.html). I use it here to store the image parameters in an SQLite DB when logged in. Why not the images? Heroku has an [ephemeral filesystem](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem) so they would be lost after a dyno restart (which happens often because I am using the *hobby* version). For the same reason Heroku provides [production grade PostgreSQL databases as a service](https://devcenter.heroku.com/articles/sqlite3), nice.

The SQLAlchemy model code is in [model.py](https://github.com/pybites/pillow-flask/blob/master/model.py) including code under main to recreate the DB. Obviously I need to a tool like [Alembic](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/) to properly handle future migrations.

### Flask

The core logic is in [app.py](https://github.com/pybites/pillow-flask/blob/master/app.py). It started simple with [57 lOC](https://github.com/pybites/pillow-flask/commit/be189a730488c5b7ce9e99ee2990c75fb274421b#diff-3f41e546893dc64b71aaacad12cad815), growing to 139 LOC as of this writing. Not bad considering that it does form handling, image generation, caching and handling a simple login session.

Some interesting things:

* `login_required` decorator (RealPython's Flask material). This login simply verifies against env variables. For multiple users make a User model / table. Logged in state is saved in the [session variable](https://pybit.es/flask-sessions.html) and use [Flask-Login](https://flask-login.readthedocs.io/en/latest/).

* `_store_banner` shows how easy it is to interface with SQLAlchemy.

* The `_get_form` helper swaps out the default logos (currently just one Python logo) with PyBites logos when logged in. Flask-WTF made this effortless.

* The `index` route is still a bit too long = a good candidate for [refactoring](https://pybit.es/codechallenge30.html). It retrieves cached image objects (parameters) from the DB, generates a banner upon POST request and sends it to the browser. 

	The way to send a banner to the browser is via Flask's `send_file`. This was a bit tricky. Although I set `cache_timeout=1` the browser would stubbornly show previous banners, probably due to its own caching policy. I ended up giving the output file name a unique string with `str(time.time())`, so the browser sees it as a brand new file each time. Tricking the browser for fun and profit ;)

* Form and cached banners are passed to the `imageform.html` template for rendering. 

* Use of logging and namedtuples.

## Resources and Pillow/Flask Challenge

I hope this inspires you that you can do cool stuff with Pillow and Flask. Yeah I know what you ar thinking: "but it's 100 days of Django" and yes that's true. Yet for this case I think Flask was the right choice. Julian shared some more thoughts about when to use one or the other, you can check it out [here](https://pybit.es/learning-flask-django.html).

You can read more about the Pillow code in Part 1 of this tutorial [here](https://pybit.es/pillow-banner-image.html).

This project was part of [Code Challenge 31 - Image Manipulation With Pillow](https://pybit.es/codechallenge31.html) - if you want to play with Pillow and potentially Flask and Heroku, follow the instructions there and start coding and PR your code to [our challenges repo](https://github.com/pybites/challenges).

If you deploy your app to Heroku, checkout Julian's [nice tutorial on the subject](https://pybit.es/deploy-flask-heroku.html).

Want to learn more Flask? We are starting to have some resources, check out [our Flask category](https://pybit.es/category/flask.html).

---

Keep Calm and Code in Python!

-- Bob

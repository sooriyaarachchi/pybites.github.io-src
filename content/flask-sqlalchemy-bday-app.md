Title: Building a Simple Birthday App with Flask-SQLAlchemy
Date: 2017-05-11 11:00
Category: Flask
Tags: Flask-SQLAlchemy, SQLAlchemy, Flask, Facebook, birthday, calendar, icalendar, datetime
Slug: flask-sqlalchemy-bday-app
Authors: Bob
Summary: In this article I teach you how to get started with Flask-SQLAlchemy. I will set up a model, create the DB, retrieve birthdays from FB and import them into the DB. Lastly I will query the birthdays by date range. 
cover: images/featured/pb-article.png

One of my favorite Flask extensions is [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/). It makes working with a database a breeze. For some time I wanted to detach my birthday management from Facebook. So I started a simple Flask app. Work so far [here](https://github.com/pybites/bday-app).

## FB birthday data

I am almost sure you could use the FB API before to pull all your friends and birthdays. [Not anymore](http://stackoverflow.com/questions/27924140/fetch-friends-birthday-using-facebook-graph-api-v2-0) :(

Luckily [I found a way](https://github.com/pybites/bday-app/blob/master/README.md) to export them and parse them into a useful format - see [bdays.py](https://github.com/pybites/bday-app/blob/master/bdays.py).

## Starting Flask-SQLAlchemy 

Back to the article subject: how do we get this data into a DB? Flask-SQLAlchemy to the rescue:

* First I defined a simple model in [model.py](https://github.com/pybites/bday-app/blob/master/model.py): 

		...

		class Birthday(db.Model):
			id = db.Column(db.Integer, primary_key=True)
			name = db.Column(db.String(120))
			bday = db.Column(db.DateTime)
			notify = db.Column(db.Boolean)

			def __init__(self, name, bday, notify=False):
				self.name = name
				self.bday = bday
				self.notify = notify

			def __repr__(self):
				return '<Birthday %r %r %r>' % (self.name, self.bday, self.notify)

	It's best to store dates as db.DateTime objects so we can easily query them (see further down).

* If model.py is run as standalone script (not imported) it recreates the DB:

		db.drop_all()
		db.create_all()

	I use the bdays.py ics parsing code to populate the table with all birthdays. You can even strip out the names (which was useful to share printscreens here):

		for bd in sorted(get_birthdays('cal.ics'), key=lambda x: (x.bday.month, x.bday.day)):

			# no real names
			if TEST_MODE:
				name = get_random_name()
			else:
				name = bd.name
		
			# import all bdays with THIS_YEAR to make it easier to query later
			bday = bd.bday.replace(year=THIS_YEAR)
			bd_obj = Birthday(name, bday)
			db.session.add(bd_obj)

		db.session.commit()

* The app is still very bare-bones. It has an index/home route, to get the birthdays of the next 14 days, and a route to get birthdays for each month. See [app.py](https://github.com/pybites/bday-app/blob/master/app.py). Here's why you want to work with datetime objects, it makes querying dates easier:

	* Upcoming n days:

			@app.route('/')
			...
			start = datetime.now()
			end = start + timedelta(days=UPCOMING_DAYS)
			bdays = Birthday.query.filter(Birthday.bday <= end).filter(Birthday.bday >= start)

	* How to get all birthdays of month n ([SO help](http://stackoverflow.com/questions/36155332/how-to-get-the-first-day-and-last-day-of-current-month-in-python)). I use THIS_YEAR (2017) to store all birthdays with the same year (calendar ics had them from May '17 to May '18). The SQLAlchemy query is the same:

			@app.route('/<int:month>')
			...
			_, num_days = calendar.monthrange(THIS_YEAR, month)
			start = date(THIS_YEAR, month, 1)
			end = date(THIS_YEAR, month, num_days)
			bdays = Birthday.query.filter(Birthday.bday <= end).filter(Birthday.bday >= start)

## Resulting App

![bday app upcoming]({filename}/images/bday-app1.png)

![bday app for a particular month]({filename}/images/bday-app2.png)

You can use the calendar module to get the month name for a month int:

	month_name = calendar.month_name[month]

See [app.py](https://github.com/pybites/bday-app/blob/master/app.py).

## TODO

This is it for starters. In part 2 I will make the app more functional: 

* Implement notifications: email me one day before a birthday.

* Allow setting of notify == True for individual friends so I only get the notifications I want.

* Full CRUD: add/update/delete friends and/or re-import new ics download.

* Second (relational) table/ model to add the notifications sent and a "complete" (boolean) column to be update when I sent Happy Birthday wishes to friend.

## Resources

* Flask-SQLAlchemy [docs](http://flask-sqlalchemy.pocoo.org/2.1/) get you up2speed fast.

* See our [code challenge 15 review](http://pybit.es/codechallenge15_review.html) for more example apps using Flask-SQLAlchemy.

* For examples of standard SQLAlchemy (outside Flask) see our [code challenge 17 review](http://pybit.es/codechallenge17_review.html) has some examples.

* To learn SQLAlchemy start with the [Object Relational Tutorial](http://sqlalchemy.readthedocs.io/en/latest/orm/tutorial.html).

---

Keep Calm and Code in Python!

-- Bob

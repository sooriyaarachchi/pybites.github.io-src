Title: Code Challenge 33 - Build a Django Tracker, Weather or Review App
Date: 2017-08-22 13:00
Category: Challenge
Tags: codechallenges, Django, 100DaysOfDjango, tracker, review, weather, apps, projects, 100DaysOfCode, Heroku
Slug: codechallenge33
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python programming. To keep it [#100DaysOfDjango](https://pybit.es/tag/100daysofdjango.html), this week we let you get some more practice with this awesome web framework. Last time we had an open Django challenge, for this one we have you choose between 3 specific apps. 
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, a new week, a new 'bite' of Python programming. To keep it [#100DaysOfDjango](https://pybit.es/tag/100daysofdjango.html), this week we let you get some more practice with this awesome web framework. Last time we had an open Django challenge, for this one we have you choose between 3 specific apps. 

## The Challenge

### Basic

* Build an app to keep track of something:

	* Pomodori (25 min segments) of reading, walking, deep work, etc. 
	* Overtime ([Flask example](https://github.com/pybites/100DaysOfCode/blob/master/089/app.py))
	* BMI ([Flask example](https://github.com/pybites/100DaysOfCode/blob/master/056/app.py)) 
	
	One requirement: data needs to be stored in a DB and be editable (basic CRUD).

### Don't be shy

* Convert PyBites' [Weather Compare App](http://weathercompare.herokuapp.com/) ([article](https://pybit.es/flask-simple-weather-app.html)) into a Django app and enhance it with the following features:

	* Keep a log of cities queried. 
	* Have a user [signup](https://github.com/pybites/django-registration) asking for the geo and show (and email) the daily weather.
	* Show historic weather info, maybe you could even integrate plots [like we did with Flask](https://pybit.es/codechallenge28.html)

### Die hard

* Make a books or movie review app:

	* Long time ago I (Bob) created [fbreadinglist](http://fbreadinglist.com/) and [sharemovi.es](http://sharemovi.es/). Both PHP and far from perfect, but good candidates to learn Django. You do need a bit of front-end skills to pull this off however, but who doesn't these days, right? ;)
	* The FB login is optional, if you want to try it out check out [this article](https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html). Otherwise you could use [django-registration](https://django-registration.readthedocs.io/en/2.2/), see our [step-by-step guide](https://pybit.es/django-registration-app.html).

* Books and movie review apps are just not your thing? Sure, we understand. What about something cooler? Our second option for the main course is *a code review tool for PyBites*:

	* Create a Django app where one can submit code challenge solutions.
	* Have different roles: participants (can submit code), reviewer (can review code), admin (can promote users to reviewer and assign code reviews).
	* Github API integration would be really cool, but don't let that distract you. This is about Django.

### Bonus:

Share your great work with the world [deploying it to Heroku](https://devcenter.heroku.com/articles/deploying-python).

## Get credit!

__Take notice__: the coolest working apps get a place under the __#100DaysOfDjango__ project on [our projects page](https://pybit.es/pages/projects.html)!

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our start-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

### Feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or [reach out](http://pybit.es/pages/about.html) directly.

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

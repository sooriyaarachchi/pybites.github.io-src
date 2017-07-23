Title: Code Challenge 29 - Create a Simple Django App
Date: 2017-07-25 09:00
Category: Challenges
Tags: codechallenges, Django, 100DaysOfDjango
Slug: codechallenge29
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! We are 2 weeks into learning Django ([our second 100 Days project](https://pybit.es/pages/projects.html)) so we thought it's about time to dedicate a code challenge to it. So this week is all about coding (and deploying) a Django app. Have fun!
cover: images/featured/pb-challenge.png
status: draft

> A smooth sea never made a skilled sailor. - Franklin D. Roosevelt

Hi Pythonistas, a new week, a new 'bite' of Python coding! We are 2 weeks into learning Django ([our second 100 Days project](https://pybit.es/pages/projects.html)) so we thought it's about time to dedicate a code challenge to it. So this week is all about coding (and deploying) a Django app. Have fun!

## The challenge

Similar to [our first Flask challenge](https://pybit.es/codechallenge15.html) we ask you to build a simple app with the following requirements:

### Basic

- Separate content from presentation (MVC or in Django's case [MTV = model - template - view](https://docs.djangoproject.com/en/1.11/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)).
- Data gets stored and queried using [Django's ORM](https://docs.djangoproject.com/en/1.11/topics/db/) (which uses SQLite by default, but feel free to use another DB).

### Don't be shy

- Data can be added, edited and deleted (CRUD)

### Die hard

- Add a login. Note that Django comes with batteries included so you might be able to leverage the existing User model (`from django.contrib.auth.models import User`) - [this article](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html) might be helpful. 
- If you want to go overboard, add a registration system: signup form + confirmation link validation email + password reset function. [Simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com) has tutorials on this too. Or maybe you can leverage [a plugin](https://django-registration.readthedocs.io/en/2.2/)?

### Bonus

- Deploy your app to [Heroku](https://www.heroku.com/), [Python Anywhere](https://www.pythonanywhere.com) or a service of your choice.

## Resources

* [Django docs](https://docs.djangoproject.com/en/1.11/) - Django has high quality documentation, use it :)
* [Writing your first Django app (polls) tutorials](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) - we found these helpful getting started.
* [Full Stack Python Django reference page](https://www.fullstackpython.com/django.html).
* [First Steps Learning Django: PyPlanet Article Sharer App](https://pybit.es/learning-django.html) - article how we built our first app.
* For deployment use the provider's latest docs. Last week we learned some [Heroku](https://pybit.es/deploy-flask-heroku.html) and [Python Anywhere](https://pybit.es/django-python-anywhere.html) ourselves.

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

## Feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or [reach out](http://pybit.es/pages/about.html) directly.

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

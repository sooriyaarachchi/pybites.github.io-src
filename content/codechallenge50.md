Title: Code Challenge 50 - Use Celery to Offload an Expensive Task
Date: 2018-04-02 00:35
Category: Challenge
Tags: Celery, Flask, broker, async, Easter
Slug: codechallenge50
Authors: PyBites
Summary: Hi Pythonistas, back-to-back with our Planet Python challenge 49 here is our special Easter Challenge #50 where you will use Celery to offload a simplified Easter ecard mailer app. 
cover: images/featured/pb-challenge.png

> It's not that I'm so smart, it's just that I stay with problems longer. - A. Einstein

Hi Pythonistas, back-to-back with our Planet Python challenge 49 here is our special Easter Challenge #50 where you will use Celery to offload a simplified Easter ecard mailer app. 

## The Challenge

Go to [Challenge 50 on our platform](https://codechalleng.es/challenges/50/) and pull/update the Community branch. cd into the 50 directories, [create your virtual env](https://pybit.es/the-beauty-of-virtualenv.html) and `pip install` the requirements (Flask and Celery).

The app let's your enter a banner URL, a comma separated list of emails and optional message:

![simple flask app for celery]({filename}/images/celery-flask-app1.png)

![simple flask app for celery]({filename}/images/celery-flask-app2.png)

The `_emails_users` simulates some processing time by sleeping 1 second - in real life this could be an intentional short pause so as to not hit a server or API too often. For the end users though, the page just appears slow and could result in them navigating away while the emailing is still taking place! Time to add some asynchronous processing so the user can keep navigating the site!

Can you offload the emailing to a Celery task so the user does not have to wait for it to end or to prevent an impatient user from navigating away? Change the Flask app as you want, it's just some bootstrap code to get started ... You could also add an option to the form to send the card at a later date ...

Set up a [message broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/) of your choice and [start playing with Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html). For a Flask + Celery basic example check [here](http://flask.pocoo.org/docs/0.12/patterns/celery/). 

### Bonus 

Bonus points if you can display progress of the emailing on the page. Secondly try to deploy it to a cloud service provider and make the emailing work. You could try [Heroku + Sendgrid](https://devcenter.heroku.com/articles/sendgrid) for example.

### Credit

PR your work [on our platform](https://codechalleng.es/challenges/50/) and get our special [PyBites Easter Badge](https://codechalleng.es/badge/easter) added to your dashboard.

We are moving the review posts to a _featured view_ on our platform (audience > 1800 users and growing), PR and standby ... 

## PyBites Community

A few more things before we take off:

* Do you want to discuss this challenge and share your Pythonic journey with other passionate Pythonistas? Confirm your email on our platform then request access to our Slack via [settings](https://codechalleng.es/settings/).

* PyBites is here to challenge you because becoming a better Pythonista requires practice, a lot of it. For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or ping us on our Slack.

* And of course Happy Easter!

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!

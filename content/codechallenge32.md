Title: Code Challenge 32 - Test a Simple Django App With Selenium
Date: 2017-08-15 13:00
Category: Challenges
Tags: codechallenges, Django, 100DaysOfDjango, Selenium, Testing, 
Slug: codechallenge32
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python goodness. As [anticipated](https://github.com/pybites/challenges/issues/91) this week we dedicate a challenge to Selenium testing. We think this is a cool skill to add to your web dev + testing repertoire.
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, a new week, a new 'bite' of Python goodness. As [anticipated](https://github.com/pybites/challenges/issues/91) this week we dedicate a challenge to Selenium testing. We think this is a cool skill to add to your web dev + testing repertoire.

## The challenge

Our first intuition was to let you pull a Django app, but this might lead to config confusion. So let's test [our first Django app](https://pybit.es/learning-django.html). 

The [main page](pybites.pythonanywhere.com) is actually our [100DaysOfDjango home](https://pybit.es/tag/100daysofdjango.html) where we want to add more apps over time.

We ask you to help PyBites dev to deliver tests for this app using Selenium:

1. Go to the [http://pybites.pythonanywhere.com/](pybites.pythonanywhere.com). The header should say *PyBites 100 Days of Django*. The navbar has Login and Home links. The first link in main is *PyPlanet Article Sharer App*.

	![test the home page]({filename}/images/selenium-challenge1.png)

2. Click on *PyPlanet Article Sharer App* and test the page contains a `table` with a `th` (table header) containing the word *Title*. This app watches the PyPlanet feed so the titles change every day. What we can test though is if the table contains 100 entries (`tr`).

	![home page]({filename}/images/selenium-challenge2.png)

3. Go to an article and check there is only a *Go back* button. Check if the header link at the top is the same as the link you clicked on, in this example: *Martin Fitzpatrick: KropBot: Multiplayer Internet-controlled robot*. The *Go back* should redirect back to [http://pybites.pythonanywhere.com/pyplanet/](the app's home).

	![home page]({filename}/images/selenium-challenge3.png)

4. Using Selenium click the login link and login with user: guest / password: changeme - then click the *Login* button:

	![home page]({filename}/images/selenium-challenge4.png)

5. Check you are redirected back to [100Days home](http://pybites.pythonanywhere.com/) and if navigation should say *Welcome back, guest!* and contains Logout and Home links:

	![home page]({filename}/images/selenium-challenge5.png)

6. Going back to the article link (3.), check that you now have a *Tweet this* as well alongside the *Go back* button. If you want to check the *Tweet this* button, it is basically a link and our articles should have *New PyBites Article* prepended.

	![home page]({filename}/images/selenium-challenge6.png)

7. Finally logout with Selenium and check for *See you!* and *You have been successfully logged out.*, *logout* in the URL, and navbar links are Login and Home again.

	![home page]({filename}/images/selenium-challenge7.png)

By the way, if you don't like this app or want to test a Flask (or framework ...) app, be our guest. Just mention it in your submission.

### Bonus

If you like to test even more you need superuser rights. Nobody stops you though from [cloning the repo](https://github.com/pybites/pyplanet-django) and get it working locally. Apart from practicing getting a Django app running you could then additionally test:

1. Create a Django superuser and use it to login. Click the *Mark Skipped* button on an article and check if it marks the entry as orange back at the main app page/table view. Going back the button is deactivated and button text changed to *Already skipped*

2. (still logged in) click the *Mark Shared* button on another article and check if it marks the entry green back at the main app page/table view. Going back the button is deactivated and button text changed to *Already shared*

3. For both 1. and 2. the blue *Tweet this* button disappeared.

Again [here](https://pybit.es/learning-django.html) is how the app looks with superuser rights.

### Resources

* [Selenium with Python](http://selenium-python.readthedocs.io/)

* [Headless Selenium Testing With Python and PhantomJS](https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/)

* [Test-Driven Development With Python aka Obey the Testing Goat!](http://www.obeythetestinggoat.com/) - [chapter 1](http://www.obeythetestinggoat.com/book/chapter_01.html) kicks off with a Selenium functional test.

* [Using Headless Chrome with Selenium](https://blog.miguelgrinberg.com/post/using-headless-chrome-with-selenium)

## Get credit!

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

### Feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or [reach out](http://pybit.es/pages/about.html) directly.

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

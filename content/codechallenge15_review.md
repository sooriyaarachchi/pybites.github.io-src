Title: Code Challenge 15 - Create a Simple Flask App - Review
Date: 2017-04-22 17:20
Category: Challenges
Tags: codechallenges, learning, Flask, task manager, reading planner, meal history
Slug: codechallenge15_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge15.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Create a Simple Flask App](http://pybit.es/codechallenge15.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Our solution and learning

This was one of the best challenges so far. We have 3 cool apps to show today.

### Julian

This has to have been one of the most satisfying projects of my life. Why? Because, for the first time I successfully coded up an application with a front end, a back end *and* persistent storage!

![julian's meal tracker]({filename}/images/meal-tracker.png)

- The first thing you'll notice is that the page looks like it's straight out of the early 90's. (My CSS/Bootstrap game isn't very strong yet so settle down). I figured it was more important to get the app side working first. Styling can and will be improved later.

- This is a very simple program that asks you for the last thing you ate and drank and tracks it in a database. You can then print out the "meal history" (ie, dump of the db) on another web page.

- Everything is run within an *app.py* file. I can definitely go back and refactor this code to be more Pythonic. For example, I control the connection to the sqlite db using a *with* statement. You can see this statement occur three times in the program which is way too much repetition for my liking!

- The most difficult thing to get right was the passing of the data from the form back to the Python script for storage. The difficulty was more in wrapping my head around how this worked as I wasn't 100% across the whole HTTP GET and POST methods.

- Point of learning: In my *def index()* function, the first load of the web page causes the return value to be passed to the page straight away. The entire if statement isn't processed **until the POST request is made by submitting the form**. (Figuring this out was like reaching enlightenment).

- I spent an entire evening this week learning sqlite3 just for this challenge. Totally worth it. If you don't know it already, do it. It's a wonderful way of storing data! It's also super handy being able to view the .db file in the SQLite DB browser to sanity check your app is doing what it's supposed to.

- I used a *lot* of different resources to learn this.(Shameless plug alert!): I used our existing [PyBites Articles on Flask](http://pybit.es/tag/flask.html) for the most part but also [this great video on Flask](https://www.youtube.com/watch?v=DIcpEg77gdE) by the Miguel Grinberg.

- **TODO**: I can't wait to continue work on this app. The next step will be refactoring and finishing some UX features (eg: a return button on the second page) and then to get this running on Heroku or AWS.

The code for this project is [here](https://github.com/pybites/challenges/tree/solutions/15/meal).

### Bob

I scratched my own itch building a reading planner using [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) and copied the PureCSS from [my previous app](http://pybit.es/flask-simple-weather-app.html): 

![bob's reading planner]({filename}/images/reading-planner.png)

This was a great exercise using SQLAlchemy and made me more confident to rewrite [My Reading List](http://fbreadinglist.com/) (PHP) using an ORM, be it Flask or Django.

The code for this project is [here](https://github.com/pybites/challenges/tree/solutions/15/reading_planner).

I think this was one of the best challenges so far and I am happy to see that our code challenges trigger people to really practice and learn, building awesome stuff. Which brings us on:

## Community 

We had a really nice PR from [clamytoe (Martin)](https://github.com/clamytoe) who built a "no frills task manager that's really intuitive and simple to use." - under the covers it uses Flask-SQLAlchemy and some very nice styling using Bootstrap. Here is us using his nice app:

![martin's task manager]({filename}/images/task-manager.png)

The code for this project is [here](https://github.com/pybites/challenges/tree/community/15/clamytoe). 

---

We hope you are enjoying these challenges, learning along the way. Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...

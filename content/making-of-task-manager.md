Title: The making of my Task Manager App for the PyBites Code Challenge
Date: 2017-05-02 13:00
Category: Learning
Tags: blog, challenges, Flask, Bootstrap, HTML, CSS, Jinja2, Flask-SQLAlchemy, sql, guest, learning
Slug: guest-making-of-task-manager
Authors: Martin
Summary: As a relatively newcomer to the Python scene I've come to realize that the best way to learn is to actually participate in coding challenges. This has helped to push me out of my comfort zone.
cover: images/featured/pb-guest.png

As a relatively newcomer to the Python scene I've come to realize that the best way to learn is to actually participate in coding challenges. This has helped to push me out of my comfort zone. If you're in the same boat as me, I hope that this writeup will motivate you to do the same.

![Clamytoe's Task Manager]({filename}/images/ctm.png)

## Backstory
To be honest, I was already working on a command line version of a task manger. I basically wanted a way to track my achievements throughout the year so that I could readily have them available when it came time for my "self review". I forget what I did this morning, so having this would be a tremendous asset. I figured I could just convert my code to work with Flask, easy right? Boy was I wrong!

If you're interested in learning how I approached this challenge, read on.


## Flask
The first thing I did was to head on over to [Flask](http://flask.pocoo.org/)'s website and check out their [documentation](http://flask.pocoo.org/docs/0.12/). I specifically found their [Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/) guide to be an invaluable resource and I went back to it many times. I've been trying to keep up with developments with HTML5, CSS3, and JavaScript, so I knew that the easiest route would be to build this app on top of [Bootstrap](http://getbootstrap.com/), so that's where I headed to next.


## Bootstrap
The first thing I did was to make my way to their [Getting Started](http://getbootstrap.com/getting-started/) page. Out of all their choices on implementing their framework, I opted to go with the CDN option to avoid having to upload too many files to [GitHub](https://github.com/). Unfortunately, my Internet connection at home is very limited, so going this route would mean having to deal with slow response times, but it would be worth it for everyone else.

I headed straight for their [Examples](http://getbootstrap.com/getting-started/#examples) page to find me a template that was close enough to what I was looking for. Modifying a template would definitely speedup the development of this app. If you're new to Bootstrap, like I was, their [Components](http://getbootstrap.com/components/) page was another one of those resources that made this a whole lot easier. I chose to go with their [Static top navbar](http://getbootstrap.com/examples/navbar-static-top/) template.


## HTML & CSS
The next thing I did was to get the template up and running locally. I copied the code to my template and replaced the Bootstrap calls with the ones for the CDN. Where other files were being called, I just downloaded those and stuck them in the static folder of my project. I started with a simple "Hello World!" page just to have something loaded.

From there I started to customize the form that I would need and to add the table to display the results. Being a bit rusty, I headed over to [W3Schools](https://www.w3schools.com/) and went over their tutorials on [Forms](https://www.w3schools.com/html/html_forms.asp), [Tables](https://www.w3schools.com/html/html_tables.asp), and [CSS](https://www.w3schools.com/css/default.asp) formating. To my surprise, they also had a section on [Bootstrap](https://www.w3schools.com/bootstrap/default.asp), but I found the examples on Bootstrap's page more useful.


## Template
Now that I had my page up and running, it was time to get things rolling! I should have headed over to [Jinja](http://jinja.pocoo.org/)'s page and checked out their
[documentation](http://jinja.pocoo.org/docs/2.9/), but all I went off of was the basic examples on Flask's site. My goal was to make this a one page application, so the examples there were all I needed.

Creating the template was pretty straight forward. I had it mocked up and coded without much trouble. The hardest part was working within the confines of Bootstrap and trying to get it to do what I wanted. Once I was happy with that, it was time to actually start writing some Python code!


## Flask-SQLAlchemy
With my CLI task list, I had used [slqlite3](https://docs.python.org/2/library/sqlite3.html), but I wasn't too happy with all of the calls that I had to make each time that I wanted to modify or pull data from the database. On top of that, I had to actually write out the [SQL](https://www.w3schools.com/sql/default.asp) commands as well. I had heard that [SQLAlchemy](https://www.sqlalchemy.org/) was the tool to use, so I figured that this would be the perfect time to get acquainted with it.

Unfortunately, their docs were pretty daunting. [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) to the rescue! Like all of the other great tools that I've talked about thus far, their [documentation](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/) made this a breeze. I spent a lot of time going over those pages. When I couldn't find what I was looking for, [Stack Overflow](http://stackoverflow.com/) and [Stack Exchange](http://stackexchange.com/) via [StartPage](https://www.startpage.com/eng/?) searches came through for me. I found a lot of differing "opinions" on the proper way of doing things, but none would actually work for me. A bit of trial and error and actually dropping into the Python interpreter were key.

I recently discovered [pdir2](https://pypi.python.org/pypi/pdir2), which has been great for helping with discovering what actual commands I can use with the modules. Python's default `dir()` works as well, but I find the formatting and coloring of `pdir()` a lot easier to consume. I didn't add it to the *requirements.txt* because it's not needed for running the application. Another great tool that needs to be mentioned is the [PyCharm IDE](https://www.jetbrains.com/pycharm/). Its code completion came in really handy while working with SQLAlchemy.


## Setbacks
I did run into some trouble trying to get Python `datetime` objects through SQLAlchemy, so I ended up discarding my accomplishment task tracking app idea and just going with a simple Todo Task Manager: 

![Original UI]({filename}/images/old-ui.png)

Even though I had to "dumb it down" a bit, I still tried to make it as easy as possible to use. With it you can do the following:

* Create separate Projects
* Add tasks to each Project
* Easily navigate between Projects
* Remembers which Project you used last
* One button click task status changes
  * from Open to Close
  * from Close to Open
* Remove all tasks from a Project
* Remove a single task at a time
* Remove Projects along with any tasks assigned to it
* Able to add tasks that are initially marked as Close

Later on, if I have the motivation and time, I'd like to add the ability to select all tasks and perform operations on them with a single button click.


## Conclusion
Overall it was a great experience and I learned a lot from it. I'd recommend anyone looking to learn more about Python to take the time and participate [in PyBites code challenges](http://pybit.es/pages/challenges.html). It's one thing to read about how to do something and another one altogether having to actually implement it.

## PyBites addition

Martin submitted this cool project for our [Code Challenge 15 - Create a Simple Flask App](http://pybit.es/codechallenge15.html) which we reviewed [here](http://pybit.es/codechallenge15_review.html). 

---

Keep Calm and Code in Python!

-- [Martin](pages/guests.html#martinuribe)

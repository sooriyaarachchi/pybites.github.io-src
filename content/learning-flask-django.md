Title: Learning Flask v Learning Django
Date: 2017-08-16 13:00
Category: Learning
Tags: Flask, python, beginner, learning, Django
Slug: learning-flask-django
Authors: Julian
Summary: An article on my experience learning Flask and Django.
cover: images/featured/pb-article.png

I’ve been on a web framework kick lately with learning Flask. Now, for our latest project around learning Django I’ve had to slow down with Flask and pick up Django.

Surprisingly (or not surprisingly in my case), it’s been a bit of a struggle!

Below are 4 things I’ve noticed so far. Hopefully this helps set some expectations for anyone looking to start down this road as well.


##1. Starting Out

The Django Documentation is pretty well written and fleshed out. Not much is left to the imagination which is what you want when learning something new.

There’s an intentional and well thought out [tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) for creating your first Django app. This should be your first stop as it’s quite thorough. It seriously made me feel like Django was a polished and professional product.

Flask on the other hand feels just like reading the documentation for any third party Python module. The [Flaskr Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/introduction/) is pretty cool, don’t get me wrong. I just find the Django tutorial to be way more polished.

Both tutorials and documentation guides assume familiarity with Python and databases though. If you’re completely new to this stuff, you’ll most certainly need to do some additional reading.


<br>
##2. The Road to Hello World

Things start to get complicated when it comes to creating your first web app (Hello World!). I found Flask to be *way* easier than Django.

Flask makes you start from scratch. It reminded me of typing up my first site back in the day. A completely blank canvas, nothing but notepad (don’t judge!) and code.
It may sound out of place in this day and age but it really helped me learn the framework more effectively.

At a minimum there’s one file required to run your first app. 5 lines and you’re done:

~~~~
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
~~~~

It’s easily explainable and understandable. As you add code to it, it’s easy to see what effect the code changes you’re making are having. It’s raw coding and I love it. This is also why Flask is a micro framework.

<br>
Django on the other hand… I had no idea what the heck was going on from the start. Right off the bat, you know that it’s a feature packed, scalable framework.

It’s not as simple as creating a single file and running it. You need to do some setting up!

The first thing is to create a project using the command `django-admin startproject <sitename>`. This will create the following folder structure:

~~~~
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
~~~~

As soon as I saw this I knew things weren’t going to be as simple as with Flask.

Hello World takes some time to get around to. Rather than waste your time writing it out here I’ll direct you instead to this [guide](http://dfpp.readthedocs.io/en/latest/chapter_01.html). Needless to say, it’s not as straightforward as I would have liked!


<br>
##3. Batteries Included

Flask is barebones. Other than a web server, it really doesn’t include a lot. Rather, it has a heap of [Extensions](http://flask.pocoo.org/extensions/) you can install to provide additional functionality. It’s sometimes frustrating that some of these aren’t included by default but as Flask is a micro framework I can understand.

Django however comes with Batteries included (Bob’s favourite way of describing it!). By default you have a bunch of apps installed ready for you to use with your own app. Here’s an excerpt from the `settings.py` file that gets created when you generate your site:

~~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
~~~~

Super useful! In fact, we used `django.contrib.auth` (an authentication system) for our [PyBites Django Notifier App](https://github.com/pybites/django-registration)!


<br>
##4. The Right Framework for the Right Job

Compared with Flask I’ve barely scratched the surface of Django. I do however see why it’s so incredibly popular.

Django is jam packed with functionality and from the start is built to scale, regardless of how big or small your application is.

Unfortunately, this is actually the main detractor from using it for me. The setup involved is off-putting when all I want to do is write up a quick and dirty web app.

That’s where Flask comes into its own. I can have an idea and have it running as a web app in minutes.

It looks like it comes down to choosing the right framework for the right job. When it comes to building larger, scalable apps, I can see why Django is the preferred choice. Heck, I don’t even want to imagine how much harder it would have been to write our [Notifier App](https://github.com/pybites/django-registration) in Flask!

For now I think I’ll stick with Flask for quick and dirty apps and Django for larger, intricate and complex apps.

<br>
##Conclusion

As we like to say here at PyBites: [Learn by Doing](https://pybit.es/learn-by-doing.html)! Even though it’s probably overkill, I’m going to create a small app in Django. I might actually take a Flask app and see how easy it is to run it in Django, there’s an idea!

I digress. Learning Flask and learning Django are two totally different experiences. I think it’s important to set your expectations before you jump in. They’ll both require existing Python knowledge and they both have their learning curves.

Flask starts off slow and ramps up the difficulty as you move to build more advanced apps whereas Django starts off complex and seems to plateau (or at least I hope it does!). Either way, unless you’re a seasoned pro, there will be a time investment!

I’m probably being a bit harsh on Django though. I’m sure with enough practice I’ll be able to whip up apps with it in no time!

The only way to learn them though is to:

Keep Calm and Code in Python!

-- Julian

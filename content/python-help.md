Title: Discover Python Help Options
Date: 2017-02-02 21:45
Category: Tips
Tags: python, tips, tricks, code, pybites, help
Slug: python-help
Authors: Julian
Summary: Discover some of the numerous Python Help functions.
cover: images/featured/python-help.png

When it comes to Python I'm pretty much self taught so it came as no surprise to me when I discovered that Python had help functions. I was blown away to say the least!

There are 3 help related options I'm going to discuss: help(), dir() and pydoc.

##help()

I face palmed over not finding out about help() sooner. Just like on any operating system, help exists to assist with commands. In Python you simply put whatever object you want within the help function and you'll be presented with a very "man page-esque" looking help page. For example, let's say we wanted to find out more about the *len* function: 

~~~~
>>> help(len)

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
(END)

~~~~

The help page will detail the syntax for running the object as well as an explanation as to what it does. Some objects return much more detail than others based on their complexity. Try running **help(range)** in IDLE to see an example of the detail help() can provide. It's pretty awesome!


##dir()

It constantly baffled me as to how programmers like Bob seemed to just *know* the attributes to use with a specific object. I may never know the answer but I'm
definitely one step closer thanks to dir().

dir() is just as wonderful as help(). It allows you to query an object and return its attributes. That is to say, if you've ever wondered what to use with *len* (eg: len.<attribute/module>) then use dir(len) to get a list. Check out what happens if we use dir() on *range*:

~~~~
>>> dir(range)
['__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
>>>
~~~~

We now know we can use the *count* function with range: range.count.


##help() and dir() Together

The best part is that both help() and dir() compliment each other perfectly.

Using the previous example of *range* we found that we can use the *count* function with it. The question is how?

Use help() of course!

~~~~
>>> help(range.count)
Help on method_descriptor:

count(...)
    rangeobject.count(value) -> integer -- return number of occurrences of value
(END)
~~~~

How awesome is that?!

Modules that aren't in stdlib respond to help() and dir() as well:

~~~~
>>> import tweepy
>>> help(tweepy)
Help on package tweepy:

NAME
    tweepy - Tweepy Twitter API library

PACKAGE CONTENTS
    api
    auth
    binder
    cache
    cursor
    error
    models
    parsers
    streaming
    utils

FUNCTIONS
    debug(enable=True, level=1)

DATA
    __license__ = 'MIT'
    api = <tweepy.api.API object>
<snip>

>>> dir(tweepy)
['API', 'AppAuthHandler', 'Cache', 'Category', 'Cursor', 'DirectMessage', 'FileCache', 'Friendship', 'MemoryCache', 'ModelFactory', 'OAuthHandler', 'RateLimitError', 'SavedSearch', 'SearchResults', 'Status', 'Stream', 'StreamListener', 'TweepError', 'User', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'api', 'auth', 'binder', 'cache', 'cursor', 'debug', 'error', 'models', 'parsers', 'streaming', 'utils']
~~~~


##pydoc

Pydoc is different to help() and dir() in that you don't actually run it in IDLE or within a script. It's a command line tool that gets installed with Python.

That said, Pydoc is actually quite similar to help(). It displays a help page (again, man page similarities!) of the Python object you want to query but does so on the command line. No need to start up IDLE.

~~~~
(venv) juliansequeira$ pydoc datetime
Help on module datetime:

NAME
    datetime - Fast implementation of the datetime type.

FILE
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/datetime.so

MODULE DOCS
    http://docs.python.org/library/datetime
<snip>
~~~~

The text displayed is made up of the docstrings within the object which means you can create your own if you make your own module etc.

In typical Python fashion though, Pydoc takes it up a notch. It actually has the ability to display documentation for your installed modules/packages using the built in Python web server!

~~~~
pydoc -p 8000
~~~~

When you point your browser to localhost:8000 you'll get a (relatively) nice web page with links to your Python package documentation.


##Conclusion

Help is everywhere! I'm almost annoyed that it took me a year to discover this stuff. Better late than never I guess!

It's so much nicer being able to get the syntax and attribute help that I need from within IDLE rather than having to Google it and sort through pages of stack overflow articles.

Let me know if there are any other cool help modules or functions out there. I'd love to know!

Keep Calm and Code in Python!

-- Julian

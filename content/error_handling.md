Title: Errors should never pass silently
Date: 2017-01-18 23:59
Category: Best practices
Tags: exceptions, Zen of Python, error handling, cleancode
Slug: error_handling
Authors: Bob
Summary: Some important anti-patterns regarding error handling and how to solve them making your code more Pythonic and easier to maintain.
cover: images/featured/error-handling.png

	>>> import this
	The Zen of Python, by Tim Peters

	Explicit is better than implicit.
	...
	Errors should never pass silently.

### Anti-Patterns

There is this great read: [The Little Book of Python Anti-Patterns](http://docs.quantifiedcode.com/python-code-patterns/). For the more experienced Pythonistas most is well known, yet it is a good refresher and you probably still find something new.

Today a bit about error handling. In [Learning from Python mistakes](http://pybit.es/py-mistakes.html) we already mentioned not to use pass in except. It is actually the worst anti-pattern (listen to Andreas Dewes, the author of the book, [here](https://talkpython.fm/episodes/show/18/python-anti-patterns-and-other-mistakes))

### The problem with except: pass

Why is it so bad? See [SO](http://stackoverflow.com/questions/21553327/why-is-except-pass-a-bad-programming-practice) for a detailed explanation:

> The worst offender though is the combination of both. This means that we are willingly catching any error although we are absolutely not prepared for it and we also don’t do anything about it.

So this violates the two of the Zen's aphorisms or guiding principles.

You always want to catch errors explicitly:

	>>> try:
	...     1/0
	... except ZeroDivisionError:
	...     print('cannot divide by 0')
	... 
	cannot divide by 0

You can use else and finally as well with a try/except as shown in this little toy example:

	>>> a, b, c = 1, 2, 0
	>>> try:
	...     a/b
	... except ZeroDivisionError:
	...     print('cannot divide by 0')
	... else:
	...     print('division was ok')
	... finally:
	...     print('this always runs')
	... 
	0.5
	division was ok
	this always runs
	>>> try:
	...     b/c
	... except ZeroDivisionError:
	...     print('cannot divide by 0')
	... else:
	...     print('division was ok')
	... finally:
	...     print('this always runs')
	... 
	cannot divide by 0
	this always runs

### Asking for permission instead of forgiveness

It becomes even more important because [the Python community uses an EAFP (easier to ask for forgiveness than permission) coding style](http://docs.quantifiedcode.com/python-code-patterns/readability/asking_for_permission_instead_of_forgiveness_when_working_with_files.html).

I have done this a lot:

	if os.path.exists("file.txt"):

But the Pythonic way to do it is:

	try:
		os.unlink("file.txt")
	except OSError:
		# handle the error

So exceptions again.

### Customer exceptions

Another great way to make your code more readable and taking exceptions to the next level is to write your own. Sounds scary? It is actually pretty easy:

	class NameTooShortError(ValueError):
		pass

	def validate(name):
	    if len(name) < 10:
			raise NameTooShortError(name)

[snippet source](https://dbader.org/blog/python-custom-exceptions)

Another example from [tweepy](https://github.com/tweepy/tweepy/blob/master/tweepy/error.py):

	class TweepError(Exception):
		"""Tweepy exception"""

		def __init__(self, reason, response=None, api_code=None):
			self.reason = six.text_type(reason)
			self.response = response
			self.api_code = api_code
			Exception.__init__(self, reason)

		def __str__(self):
			return self.reason

Which I used in our [Twitter bot](https://github.com/pybites/blog_code/blob/master/twitter_bot/tweetbot.py):

    def post_tweet(self, status):
        try:
            self.api.update_status(status)
            logging.debug('posted status {} to twitter'.format(status))
        except TweepError as err:
            logging.error('tweepy update_status error: {}'.format(err))

### Reference

Recommended reading: 

* [Zen of Python](https://www.python.org/dev/peps/pep-0020/)

* [The Little Book of Python Anti-Patterns](http://docs.quantifiedcode.com/python-code-patterns/)

* [Python Tutorial - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

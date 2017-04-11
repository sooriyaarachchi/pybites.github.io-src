Title: How to Write a Decorator with an Optional Argument?
Date: 2017-04-11 9:00
Category: Tips
Tags: decorators, arguments, tricks, tips, cookbook
Slug: decorator-optional-argument
Authors: Bob
Summary: When playing with decorators ([this week's challenge](http://pybit.es/codechallenge14.html)) I got stuck: how do you write a decorator that takes an optional argument? [Python cookbook 3rd ed](http://www.amazon.com/dp/1449340377/?tag=pyb0f-20) edition to the rescue. In this post how I failed my way to the right solution.
cover: images/featured/pb-article.png

When playing with decorators ([this week's challenge](http://pybit.es/codechallenge14.html)) I got stuck: how do you write a decorator that takes an optional argument? [Python cookbook 3rd ed](http://www.amazon.com/dp/1449340377/?tag=pyb0f-20) edition to the rescue. In this post how I failed my way to the right solution.

The code for this article is [here](https://github.com/pybites/blog_code/tree/master/decorator_opt_arg).

## First attempt

To add an argument to a decorator I ended up having three levels of functions (see [here](http://stackoverflow.com/questions/5929107/python-decorators-with-parameters) and [here](http://www.artima.com/weblogs/viewpost.jsp?thread=240845)):

	from functools import wraps
	import time

	def sleep(seconds=None):
		def real_decorator(func):
			@wraps(func)
			def wrapper(*args, **kwargs):
				print('Sleeping for {} seconds'.format(seconds))
				time.sleep(seconds if seconds else 1)
				return func(*args, **kwargs)
			return wrapper
		return real_decorator

This works fine if we have an argument:

	if __name__ == '__main__':

		@sleep(1)
		def hello():
			print('hello world')

		for _ in range(3):
			hello()


	$ python decorators.py
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world

But when I call it without an argument (which I thought would work because I set it as optional argument) it fails:

	if __name__ == '__main__':

		@sleep
		def hello():
			print('hello world')

		for _ in range(3):
			hello()

	$ python decorators.py
	Traceback (most recent call last):
	File "decorators.py", line 36, in <module>
		hello()
	TypeError: real_decorator() missing 1 required positional argument: 'func'

## Can we use a class?

My intuition was that the above syntax was pretty complex so I went with the class decorator syntax (a nice exercise too):

	from functools import wraps
	import time

	class sleep:

		def __init__(self, seconds=None):
			self.seconds = seconds if seconds else 1

		def __call__(self, func):
			wraps(func)(self)
			def wrapped_f(*args):
				print('Sleeping for {} seconds'.format(self.seconds))
				time.sleep(self.seconds)
				func(*args)
			return wrapped_f

Again this works fine when I give it an argument:

	if __name__ == '__main__':

		@sleep(1)
		def hello():
			print('hello world')

		for _ in range(3):
			hello()


	$ python decorators_cl.py
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world

But leaving the arg off it fails:

	if __name__ == '__main__':

		@sleep
		def hello():
			print('hello world')

		for _ in range(3):
			hello()


	$ python decorators_cl.py
	Traceback (most recent call last):
	File "decorators_cl.py", line 25, in <module>
		hello()
	TypeError: __call__() missing 1 required positional argument: 'func'

## Allow for optional arguments

Luckily I had [Python cookbook 3rd ed](http://www.amazon.com/dp/1449340377/?tag=pyb0f-20) nearby. What I love about this book, apart from its technical depth, is that it offers short and concise recipes that you can start using right away. This really covered a need I had when I was writing my decorators: the ability to have them behave in certain ways.

Here is the cookbook's solution modified for my sleep decorator:

	from functools import wraps, partial
	import time

	def sleep(func=None, *, seconds=None, msg=None):
		if func is None:
			return partial(sleep, seconds=seconds, msg=msg)

		seconds = seconds if seconds else 1
		msg = msg if msg else 'Sleeping for {} seconds'.format(seconds)

		@wraps(func)
		def wrapper(*args, **kwargs):
			print(msg)
			time.sleep(seconds)
			return func(*args, **kwargs)
		return wrapper

The code looks like magic and I am still wrapping my head around it. 

The key part though is the use of partial():

> The partial() is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature - [docs](https://docs.python.org/3.6/library/functools.html#functools.partial).

I should probably write another article on this useful feature ...

## It works :)

	if __name__ == '__main__':

		def call_n_times(func, n=3):
			for _ in range(n):
				func()

		@sleep  # works now!
		def hello():
			print('hello world')

		print('\nWithout args\n---')
		call_n_times(hello)


		@sleep(seconds=2)
		def hello():
			print('hello world')

		print('\nWith one opt arg: seconds\n---')
		call_n_times(hello)


		@sleep(seconds=1, msg='I work so hard, resting a bit')
		def hello():
			print('hello world')

		print('\nWith two opt args: seconds and msg\n---')
		call_n_times(hello)


	$ python decorators_opt_arg.py

	Without args
	---
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world
	Sleeping for 1 seconds
	hello world

	With one opt arg: seconds
	---
	Sleeping for 2 seconds
	hello world
	Sleeping for 2 seconds
	hello world
	Sleeping for 2 seconds
	hello world

	With two opt args: seconds and msg
	---
	I work so hard, resting a bit
	hello world
	I work so hard, resting a bit
	hello world
	I work so hard, resting a bit
	hello world

## Next

As mentioned our [code challenge of this week](http://pybit.es/codechallenge14.html) is all about decorators. Maybe you can use what you learned in this article to write more versatile decorators.

---

Keep Calm and Code in Python!

-- Bob

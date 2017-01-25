Title: Everything is an Object, Python OOP primer
Date: 2017-01-24 00:01
Category: Concepts
Tags: tutorial, oop, objectoriented, programming, inheritance, polymorphism, ABC, encapsulation, property
Slug: oop-primer
Authors: Bob
Summary: I created [a notebook](https://github.com/pybites/blog_code/blob/master/notebooks/oop_fun.ipynb) on OOP (object oriented programming) in Python. 
cover: images/featured/oop-primer.png

> Everything in Python is an object, and almost everything has attributes and methods. All functions have a built-in attribute \_\_doc\_\_, which returns the doc string defined in the function's source code. The sys module is an object which has (among other things) an attribute called path. And so forth. - [Dive into Python](http://www.diveintopython.net/getting_to_know_python/everything_is_an_object.html)

I created [a notebook](https://github.com/pybites/blog_code/blob/master/notebooks/oop_fun.ipynb) on OOP (object oriented programming) in Python. Highlights:

* Definition example class, class vs instance variables:

		class Blog(object):
			"""Good practice (py3) is to explicitly inherit from object"""

			# class variable = shared among instances
			num_blogs = 0

			def __init__(self, name, bio):
				"""The constructor, gets called implicitly when instantiating a new object (next cell)"""
				self.name = name
				self.bio = bio
				Blog.num_blogs += 1  # we access a class variable like this (or use a class method)
			
			def get_articles(self, rss):
				"""Get all articles from RSS"""
				print('Articles {}: ...'.format(rss))

			def post_article(self, title):
				"""Add a new article"""
				print('Posted new article: {}'.format(title))
			
			def __str__(self):
				"""Informal or nicely printable string representation of an object"""
				return '{}: {}'.format(self.name, self.bio)

* Instantiate class = make an object

		name = 'PyBites'
		bio = 'Python code challenges, tutorials and news, one bite a day'
		blog = Blog(name, bio)

* Call a method:

		blog.get_articles('http://pybit.es/feeds/all.rss.xml')
		# Articles http://pybit.es/feeds/all.rss.xml: ...

* ABC's lets you force derived classes to implement certain behaviors / methods (tip from Dan Bader)

		from abc import ABCMeta, abstractmethod

		class Developer(metaclass=ABCMeta):
			
			@abstractmethod
			def get_post_days(self):
				"""Classes that inherit from Developer need to implement this method"""
				pass

	Julian inherits from Developer so has to implement get_post_days() method otherwise you get a TypeError.

		class Julian(Developer):
			
			def get_post_days(self):
				return 'Tue Wed'.split()

		class Bob(Developer):
			
				def get_post_days(self):
						return 'Wed Thurs'.split()

		class PyBites(Developer):
			
			def get_post_days(self):
				return 'Mon Fri Sat'.split()

		julian = Julian()
		bob = Bob()
		pybites = PyBites()

* Inheritance and calling the parent constructor:

		class PyBitesBlog(Blog):
			"""PyBitesBlog inherits from parent class Blog"""
			
			def __init__(self, *args):
				"""We get a variable-length argument list of developers"""
				self.name = self.__class__.__name__  # how to get name of class 'PyBitesBlog' as string
				self.bio = 'Python code challenges, tutorials and news, one bite a day'
				self.developers = args
				# pass name and bio to the parent class
				# py2 requires longer syntax: super(PyBitesBlog, self).__init__
				super().__init__(self.name, self.bio)

* Loop over developer objects, calling their individually defined get_post_days() methods:

			...
			def schedule(self):
				"""Loop over all developer objects calling their get_post_days method"""
				for dev in self.developers:
					print('{}: {}'.format(dev, ', '.join(dev.get_post_days())))

* Overriding \_\_str\_\_ from Blog:
					
			...
			def __str__(self):
				"""Use the parent __str__ adding something extra"""
				return super().__str__() + '\nAuthors: ' + ', '.join([str(dev) for dev in self.developers])


		pyblog = PyBitesBlog(julian, bob, pybites)

		print(pyblog)  # again call object's __str__
		# PyBitesBlog: Python code challenges, tutorials and news, one bite a day
		# Authors: Julian, Bob, PyBites


* Polymorphism in action: 

		pyblog.schedule()
		# Julian: Tue, Wed
		# Bob: Wed, Thurs
		# PyBites: Mon, Fri, Sat

	Here we call get_post_days() on every developer (instance), each one giving a different result. Other examples from stdlib are len (= \_\_len\_\_()) and + (= \_\_add\_\_()): they just do what you expect them to do for each type (as long as compatible):

		s = 'a string'
		t = (0, 1)
		d = dict(zip([1,2,3], ['a','b','c']))

		for var in (s, t, d): 
			print('len of {} (type {}) = {}'.format(var, type(var), len(var)))
		# len of a string (type <class 'str'>) = 8
		# len of (0, 1) (type <class 'tuple'>) = 2
		# len of {1: 'a', 2: 'b', 3: 'c'} (type <class 'dict'>) = 3

* Notes on encapsulation: 

	> What it doesn't have is access control such as private and protected attributes. However, in Python, there is an attribute naming convention to denote private attributes by prefixing the attribute with one or two underscores. - [Stackoverflow](http://stackoverflow.com/questions/26216563/how-to-do-encapsulation-in-python)

	If you want getter / setter behavior look at the [@property decorator](http://stackabuse.com/python-properties/).
	

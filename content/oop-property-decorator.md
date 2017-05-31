Title: OOP Beyond the Basics: Using Properties for Encapsulation, Computation and Refactoring
Date: 2017-05-31 12:00
Category: Concepts
Tags: oop, property, decorators, encapsulation, computation, dunder, refactoring, pytest, 2vs3, getter, setter
Slug: property-decorator
Authors: Bob
Summary: In this article I share my learning of the property decorator coding a simple Account class. I think it's an unmissable tool in your (Python) OOP toolkit.
cover: images/featured/pb-article.png

In this article I share my learning of the property decorator coding a simple Account class. I think it's an unmissable tool in your (Python) OOP toolkit.

##What is a property?

I found this good definition in [Powerful Python](http://www.amazon.com/dp/0692878971/?tag=pyb0f-20), a highly recommended beyond-the-basics Python book:

> In object-oriented programming, a property is a special sort of object attribute. It’s almost a cross between a method and an attribute. The idea is that you can, when designing the class, create "attributes" whose reading, writing, and so on can be managed by special methods. In Python, you do this with a decorator named property. 

##A simple Account class

Lets define a simple account class (full code is [here](https://github.com/pybites/100DaysOfCode/blob/master/063/account.py)):

	class Account:

		def __init__(self, owner, start_balance=0):
			self.owner = owner.title()
			self.start_balance = start_balance
			self._transactions = []

		# first property use case: computed attributes

		@property
		def balance(self):
			tt = sum(t.amount for t in self._transactions)
			return self._start_balance + tt

		# second property use case: encapsulation

		@property
		def start_balance(self):
			return self._start_balance

		@start_balance.setter
		def start_balance(self, balance):
			if not isinstance(balance, int):
				raise TypeError('Start balance needs to be int')
			if balance < 0:
				raise ValueError('Start balance cannot be negative')
			self._start_balance = balance

		@start_balance.deleter
		def start_balance(self):
			raise AttributeError('Cannot delete start_balance attr')

		# ... more stuff to manage transactions, not related to properties ...


	if __name__ == '__main__':
		acc = Account('Bob', 100)
		acc += 25  # using __iadd__ 
		acc -= 100 # using __isub__
		acc += 50
		acc -= 10
		print(acc)  # spending too much! :)


Here you see two cool features of properties:

### 1. Encapsulation

I cannot assign a string nor negative value to start_balance (tests that show this are [here](https://github.com/pybites/100DaysOfCode/blob/master/063/test_account.py)):

	>>> from account import Account

	>>> Account('bob', 'spam')
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "/Users/bbelderb/Documents/code/pybites_100days/063/account.py", line 11, in __init__
		self.start_balance = start_balance
	File "/Users/bbelderb/Documents/code/pybites_100days/063/account.py", line 30, in start_balance
		raise TypeError('Start balance needs to be int')
	TypeError: Start balance needs to be int

	>>> Account('bob', -10)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "/Users/bbelderb/Documents/code/pybites_100days/063/account.py", line 11, in __init__
		self.start_balance = start_balance
	File "/Users/bbelderb/Documents/code/pybites_100days/063/account.py", line 32, in start_balance
		raise ValueError('Start balance cannot be negative')
	ValueError: Start balance cannot be negative

	>>> Account('bob', 10)
	<account.Account object at 0x102a81d68>

A useful insight I picked up from Powerful Python is to use the setter also in the constructor by NOT using the underscore. Here you see why:

NOT:

	def __init__(self, owner, start_balance=0):
		self.owner = owner.title()
		self._start_balance = start_balance

Which can lead to this!

	>>> from account import Account
	>>> a = Account('bob', 'spam')
	>>>

Use: 

	def __init__(self, owner, start_balance=0):
		self.owner = owner.title()
		self.start_balance = start_balance

Which also throws 'TypeError: Start balance needs to be int' when constructing the object with the wrong type.

### 2. Computation 

As stated in [Python cookbook 3rd ed](http://www.amazon.com/dp/1449340377/?tag=pyb0f-20): 

> Properties can also be a way to define computed attributes. These are attributes that are not actually stored, but computed on demand.

	>>> acc = Account('bob', 100)
	>>> acc += 25
	>>> acc -= 100
	>>> acc += 50
	>>> acc -= 10
	>>> acc.balance
	65
	>>> acc += 135
	>>> acc.balance
	200

acc.balance corresponds to this code which is calculated on the fly: 

	@property
	def balance(self):
		tt = sum(t.amount for t in self._transactions)
		return self._start_balance + tt

Yes you can also implement this as:

	>>> acc.get_balance()
	65

... but this is much nicer:

	>>> acc.balance
	65

Also if the computation requires an external resource (DB, network) you probably want to do it on demand.

## Python 2.x

The [2.x docs property section](https://docs.python.org/2/library/functions.html#property) states: 

> Return a property attribute for new-style classes (classes that derive from object).

In Python 2.x to use 'new-style classes' you have to inherit explicitly from object (class Foo(object): pass). In Python 3.x this is done implicitly (class Foo: pass), see [here](https://stackoverflow.com/questions/15374857/should-all-python-classes-extend-object).

## Conclusion

In Python there are no private variables and writing getters and setters for all of them is not the way to go.

The Pythonic way to do getters and setters is using the @property decorator. 

As succinctly summarized [here](http://blaag.haard.se/What-s-the-point-of-properties-in-Python/):

> You can start out by writing the simplest implementation imaginable, and if you later need to change the implementation you can still do so without changing the interface.

By the way if you need a lot of them and they do similar type checking check out recipe 9.21 of [Python cookbook 3rd ed](http://www.amazon.com/dp/1449340377/?tag=pyb0f-20): Avoiding Repetitive Property Methods.

## Other use cases

Another common use case is caching. See [Python 3 Object-Oriented Programming - Second Edition](http://www.amazon.com/dp/1784398780/?tag=pyb0f-20) - [caching a web request](https://github.com/mono0926/Python-3-Object-Oriented-Programming/blob/master/1261_05_Code/1261_05_15_cache_getter.py) or [SO](https://stackoverflow.com/questions/4037481/caching-attributes-of-classes-in-python). 

Another cool use case in this context is refactoring, see [this wiki](https://wiki.python.org/moin/ComputedAttributesUsingPropertyObjects) for an example of refactoring Widget colors to support colors specified as #rrggbb strings alongside (R,G,B) tuples (TODO: try to use this technique on one of my own classes ...)

What have you used properties for? Let us know in the comments below ... 

Maybe we can do a Code Challenge around this one? :)

---

Keep Calm and Code in Python!

-- Bob

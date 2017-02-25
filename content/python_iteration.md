Title: Python Iteration
Date: 2017-01-19 19:00
Category: Concepts
Tags: python, tips, tricks, iteration, resources
Slug: python_iteration
Authors: Julian
Summary: Iteration in Python is incredibly simple compared to C and other languages. It's easy... maybe a little TOO easy...
cover: images/featured/pb-article.png

When I first started writing Python code I realised I was bringing across some bad habits and very non-Pythonic coding styles.

For loops in particular took me by surprise.


##For Loop in C

It's worth showing how I/we wrote for loops prior to reaching Pylightenment (ha!):

~~~~
demo_list = [];

for(int i = 0; i < 10; i++){
    printf(demo_list[i]);
}
~~~~

Forgive any syntax errors in the above, my C is a little rusty.
The concept however, is that we have a counter, *i*, that will allow the loop to print out the contents of *demo_list* (if it had contents) 10 times.

I always found this tricky because you had to get your counter values right. There was always so much room to mess up by being off by one. Furthermore, you'd have to know how many items are in *demo_list* in order to list out the entire list. Getting around this would then add further complication and possibly more lines of code.


##For Loop in Python

On the other hand, Python doesn't use a counter whatsoever. It simply iterates over the entire object until finished. Here's the same code in Python:

~~~~
for item in demo_list:
    print(item)
~~~~

It's simple and actually logical when reading it. It's also human readable!

This is precisely why I love it. I no longer need to worry about a counter. No matter how large *demo_list* gets, I'll be able to iterate over it until the end.


##Iterable Objects

I was pretty surprised to see just how many objects were iterable. I originally figured it was just lists, dicts and tuples that could be iterated over but that's not the case. You're able to iterate over all of the following:

- Strings! (str)
- bytes
- tuples
- dicts
- set
- io.TextIOWrapper
- models.query.QuerySet
- numpy.ndarray

This list was taken from an incredibly detailed and interesting [training video](https://www.youtube.com/watch?v=o5gByn3RKFI) by Luciano Ramalho.


##The Iteration Protocol

This is how a for loop works internally, it cathces the StopIteration for you:

	>>> name = 'Julian'
	>>> name.__iter__
	<method-wrapper '__iter__' of str object at 0x102a85848>
	>>> it = name.__iter__()
	>>> next(it)
	'J'
	>>> next(it)
	'u'
	>>> next(it)
	'l'
	>>> next(it)
	'i'
	>>> next(it)
	'a'
	>>> next(it)
	'n'
	>>> next(it)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	StopIteration

The \_\_iter\_\_ method is what makes an object iterable. You can use that in your own classes, for example:

	class Challenge(object):
		number = 0
		
		def __init__(self, name, users):
			self.name = name
			self.users = users
			Challenge.number += 1
		
		def __str__(self):
			num = str(Challenge.number).zfill(2)
			return 'Challenge {}: {}'.format(num, self.name)
		
		def __iter__(self):
			"""Make the object iterable"""
			for usr in self.users:
				yield usr

	# now use it:
	users = 'tim', 'bob', 'victor', 'julian', 'henk'
	ch01 = Challenge('wordvalue', users)
	print(ch01)
	Challenge 01: wordvalue
	for usr in ch01:
		print(usr)
	tim
	bob
	victor
	julian
	henk

	users2 = 'tim', 'bob', 'sam', 'julian', 'maria' 
	ch02 = Challenge('wordvalue part II', users2)

	print(ch02)
	Challenge 02: wordvalue part II

	for usr in ch02:
		print(usr)
	tim
	bob
	sam
	julian
	maria

##Iteration Fun - Parallel Assignment

The simplicity and flexibility of Python iteration makes it pretty satisfying and fun to use.

One of my favourites is Parallel Assignment:

~~~~
awesomeness_levels = [('Bob', 8), ('Julian', 11), ('PyBites', 3)]

for name, level in awesomeness_levels:
    print(name + ': ' + str(level))

Bob: 8
Julian: 11
PyBites: 3

# I turned it up to eleven!
~~~~

I love that in a minimal amount of code I'm able to iterate over the entire list but also assign a variable to each item.

##Iteration Fun II - One iterable providing multiple arguments

Another cool example is function argument unpacking (min 15 of the video) which allows you to do something like:

~~~~
>>> import itertools
>>> names = ('Bob', 'Julian', 'PyBites')
>>> for pair in itertools.combinations(names, 2):
...     print('{} teams up with {}'.format(*pair))  # unpacks pair tuple in the 2 {} format placeholders
... 
Bob teams up with Julian
Bob teams up with PyBites
Julian teams up with PyBites
~~~~

##Conclusion

There's a **lot** to cover when it comes to iteration and also a lot that you could be doing in a non-Pythonic way.

I'd wholeheartedly recommend watching the [aforementioned video](https://www.youtube.com/watch?v=o5gByn3RKFI) by Luciano Ramalho.

For best practices when it comes to loops, check out the *The Little Book of Anti-Patterns* section on [unpythonic loops](http://docs.quantifiedcode.com/python-code-patterns/readability/using_an_unpythonic_loop.html).

Keep Calm and Code in Python!

-- Julian

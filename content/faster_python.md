Title: 5 tips to speed up your Python code
Date: 2017-02-21 9:00
Category: Best practices
Tags: performance, data structures, pythonic, generators, map, builtin, algorithms, regex, patterns
Slug: faster-python
Authors: Bob
Summary: In this post I will give you 5 tips to speed up your code.
cover: images/featured/faster-python.png

This article is about native Python, not [compilers](https://en.wikipedia.org/wiki/List_of_compilers#Python_compilers) nor [concurrency](https://docs.python.org/3/library/concurrency.html).

First off: optimizing usually is not your primary concern, writing readable code is. 

> Premature optimization is the root of all evil. (Donald Knuth)

However a lot of the tips I investigated below go hand-in-hand with writing good, Pythonic code. 

Here are 5 important things to keep in mind in order to write efficient Python code.

## 1. Know the basic data structures

As already mentioned [here](http://pybit.es/collections-deque.html) dicts and sets use hash tables so have O(1) lookup performance. Good reference: [TimeComplexity](https://wiki.python.org/moin/TimeComplexity) for the main data types.

Update: in the first iteration of this article I did a 'value in set(list)' but this is actually expensive because you have to do the list-to-set cast. The suggested set(a) & set(b) instead of double-for-loop has this same problem. Thanks for pointing this out [on Reddit](https://redd.it/5vapzt).

## 2. Reduce memory footprint

	msg = 'line1\n'
	msg += 'line2\n'
	msg += 'line3\n'

This is inefficient because a new string gets created upon each pass. Use a list and join it together:

	msg = ['line1', 'line2', 'line3']
	'\n'.join(msg)

Similarly avoid the + operator on strings:

	# slow
	msg = 'hello ' + my_var + ' world'

	# faster
	msg = 'hello %s world' % my_var  

	# even better (more pythonic)
	msg = 'hello {} world'.format(my_var)

Other memory saving techniques:

* probably best known are generators which result in the lazy (on demand) generation of values, which translates to lower memory usage. Good news is that in Python 3 range, d.items() etc return generators (in Python 2 use xrange, d.iteritems() respectively). Another good reason to switch to Python 3 :)

* list.sort() is in place vs sorted() which makes a copy. Honestly I have mostly used latter, but it might matter if your data set grows.

* [\_\_slots\_\_](https://docs.python.org/2/reference/datamodel.html): 'the \_\_slots\_\_ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because \_\_dict\_\_ is not created for each instance', so this is really useful if you have a lot of instances (here is a [real-world example](http://tech.oyster.com/save-ram-with-python-slots/)).

## 3. Use builtin functions and libraries

Builtin functions like sum, max, any, map, etc are implemented in C. They are very efficient and well tested. Use them!

Example borrowed from this [great wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips):

	newlist = []
	for word in oldlist:
		newlist.append(word.upper())

Better:

	newlist = map(str.upper, oldlist)  # wiki cites map as a for loop moved into C code

Maybe more readable = list comprehension (still faster than the classic for loop):

Guido's [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) is a great read:

> If you feel the need for speed, go for built-in functions - you can't beat a loop written in C. Check the library manual for a built-in function that does what you want.

Another example of using builtins is the [collections](https://docs.python.org/2/library/collections.html) module which offers Pythonic and efficient data structures (deque, defaultdict, Counter, etc)

defaultdict is a good example:

	>>> s = 'mississippi'
	>>> d = defaultdict(int)
	>>> for k in s:
	...     d[k] += 1

No need to see if key is in dict, faster, less code. As Jack Diederich says in [this great talk](https://www.youtube.com/watch?v=o9pEzgHorH0):

> I hate code and I want as little of it as possible in our product.

## 4. Move calculations outside the loop

If you have a big iterator and you need to do some regex matching, for example match a date:

	for i in big_it:
		m = re.search(r'\d{2}-\d{2}-\d{4}', i)
		if m:
			...

Better to compile the regex once and use that 'cached' version in the loop:

	date_regex = re.compile(r'\d{2}-\d{2}-\d{4}')

	for i in big_it:
		m = date_regex.search(i)
		if m:
			...

More generically evaluate as much as possible outside the loop!

Another trick is to asign a function (calculation) to a local variable:

> Python accesses local variables much more efficiently than global variables. ([source]([PerformanceTips wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)))

	myfunc = myObj.func
	fcor i in range(n):
		myfunc(i) # faster than myObj.func(i)

## 5. Keep your code base small

Common sense but still: be conscious what you put in the module vs main level (latter being below the \_\_main\_\_ statement). When you import a module potentially a lot of code runs and can slow down your program! 

Reduce the amounts of if/elif/and/or. An interesting example I learned from [this great talk](https://www.youtube.com/watch?v=YjHsOrOOSuI): the ask forgiveness code style actually runs faster because it eliminates the need for the if check:

	if os.path.isfile(some_file):
		...

	# better (and more pythonic)
	try:
		with open(some_file) as f:
			...

Overall more Pythonic is easier to read but also faster. Another example (same talk): 'if variable:' is faster than the un-idiomatic 'if variable == True:' 

---

## How to spot performance issues?

Humans are pretty bad at guessing, I can tell ... once I wanted to optimize a Python script I built that did heavy text parsing but took a bit of time. Profiling the code it was caused by a different part than I had intuitively thought!

You can use the [profile module](https://docs.python.org/3.6/library/profile.html):

	python -m profile script [args ...]
	# add -o to save the output

To time code, see [this SO thread](http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python).

---

## Resources

* Again Guido's [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) is a great read.

* Reference: [Performance tips wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips).

* [TimeComplexity reference](https://wiki.python.org/moin/TimeComplexity).

* Mentioned talk [Writing faster Python](https://www.youtube.com/watch?v=YjHsOrOOSuI) by Sebastian Witowski.

* Book on the subject: [High Performance Python: Practical Performant Programming for Humans](https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1449361595/ref=sr_1_1?ie=UTF8&qid=1487234279&sr=8-1&keywords=high+performance+python).

---

What are your favorite tricks to speed up your Python code?

---

Keep Calm and Code in Python!

-- Bob

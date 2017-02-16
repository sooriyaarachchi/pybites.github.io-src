Title: 10 tips to speed up your Python
Date: 2017-02-21 9:00
Category: Learning
Tags: performance, data structures, pythonic, generators, map
Slug: faster-python
Authors: Bob
Summary: In this post I will give you 10 tips to speed up your code.
cover: images/featured/faster-python.png
Status: draft

## Use hashable objects for lookup

As already mentioned [here](http://pybit.es/collections-deque.html#collections-deque) dicts and sets use hash tables so have O(1) performance.

This is easy to use even if you happen to have lists:

	if value in set(list)

## Don't str append

	msg = 'line1\n'
	msg += 'line2\n'
	msg += 'line3\n'

This is inefficient because a new string gets created upon each pass. Use a list and join it together

	msg = ['line1', 'line2', 'line3']
	'\n'.join(msg)

Similarly avoid the + operator on strings

	# slow
	msg = 'hello ' + my_var + ' world'

	# fast
	msg = 'hello %s world' % my_var  # or use format()
 

## Use builtin functions and libraries 

Builtin functions like map are implemented in C code.

Example barrowed from this [great wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips) (bit old, but a lot still holds true):

	newlist = []
	for word in oldlist:
		newlist.append(word.upper())

Better:

	newlist = map(str.upper, oldlist)  # wiki calls 'map a for moved into C code'

Maybe more readable = list comprehension: 

	newlist = [s.upper() for s in oldlist]

But loads whole list in memory, so if size is an issue use a generator (lazy loading):

	iterator = (s.upper() for s in oldlist)

Good news is that in Python 3 range, d.items() etc return generators (still in Python2? ...)

Guido's [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) is a great read:

> If you feel the need for speed, go for built-in functions - you can't beat a loop written in C. Check the library manual for a built-in function that does what you want. 

## Collections

Another example of using builtins is the [collections](https://docs.python.org/2/library/collections.html) module which offers Pythonic and efficient data structures (deque, Counter)

defaultdict is a really good example: 

	>>> s = 'mississippi'
	>>> d = defaultdict(int)
	>>> for k in s:
	...     d[k] += 1

No need to see if key is in dict, faster, less code. As Jack Diederich says in [this great talk](https://www.youtube.com/watch?v=o9pEzgHorH0):

> I hate code and I want as little of it as possible in our product.

## Use set operations where possible

I found this nice example [here](https://www.monitis.com/blog/7-ways-to-improve-your-python-performance/):

	for x in a:
		for y in b:
			if x == y:
				yield (x,y)
 
Try this instead:
 
	return set(a) & set(b)

Added benefit: 1 instead of 4 lines of code.

## Use re.compile

If you have a big iterator and you need to do some regex matching, for example match a date ...

	for i in big_it:
		m = re.search(r'\d{2}-\d{2}-\d{4}', i)
		if m:
			...

Better to compile the regex once and use that 'cached' version in the loop:

	REGEX_DATE = re.compile(r'\d{2}-\d{2}-\d{4}')

	for i in big_it:
		m = REGEX_DATE.search(i)
		if m:
			...

More generically evaluate as much as possible outside the loop!

## Local vars

From the same [PerformanceTips wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips) mentioned earlier: "Python accesses local variables much more efficiently than global variables.", so:

	myfunc = myObj.func
	fcor i in range(n):
		myfunc(i) # faster than myObj.func(i)

## Imports

Common sense but stil. Be conscious what you put in the module vs main level (latter being below \_\_main\_\_ statement). When you import a module potentially a lot of code runs and can slow down your program. Keep imports at the top of your program (don't import in a method), and just import what you need.

## How to spot performance issues?

Profile your code, at the most basic level: 

	python -m profile script [args ...]
	# add -o to save the output

But remember: 

> Premature optimization is the root of all evil. (Donald Knuth)

## \_\_slots\_\_

If you have a large amount of instances you can [use \_\_slots\_\_](https://docs.python.org/2/reference/datamodel.html):

The default can be overridden by defining \_\_slots\_\_ in a new-style class definition. The \_\_slots\_\_ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because \_\_dict\_\_ is not created for each instance.

[Real-world story](http://tech.oyster.com/save-ram-with-python-slots/).

## Further reading

Again [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) sums up a lot of this in a nice and concise way. For a book on the subject, checkout [High Performance Python: Practical Performant Programming for Humans](https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1449361595/ref=sr_1_1?ie=UTF8&qid=1487234279&sr=8-1&keywords=high+performance+python).

---

Keep Calm and Code in Python!

-- Bob

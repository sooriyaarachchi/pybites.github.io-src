Title: 10 tips to speed up your Python code
Date: 2017-02-21 9:00
Category: Best practices
Tags: performance, data structures, pythonic, generators, map, Numba, algorithms
Slug: faster-python
Authors: Bob
Summary: In this post I will give you 10 tips to speed up your code.
cover: images/featured/faster-python.png
status: draft

First off: optimizing usually is not your primary concern, writing readable code is. However a lot of the tips I investigated below go hand-in-hand with writing good, Pythonic code.

> Premature optimization is the root of all evil. (Donald Knuth)

With that said, lets dive in:

## 1. Use hashable objects for lookup

As already mentioned [here](http://pybit.es/collections-deque.html#collections-deque) dicts and sets use hash tables so have O(1) performance.

This is easy to use even if you happen to have lists:

	if value in set(list):
		...

Overall a good understanding of basic algorithms / data structures pays off.

## 2. Don't str append

	msg = 'line1\n'
	msg += 'line2\n'
	msg += 'line3\n'

This is inefficient because a new string gets created upon each pass. Use a list and join it together:

	msg = ['line1', 'line2', 'line3']
	'\n'.join(msg)

Similarly avoid the + operator on strings:

	# slow
	msg = 'hello ' + my_var + ' world'

	# fast
	msg = 'hello %s world' % my_var  # or use format()

## 3. Use builtin functions and libraries

Builtin functions like map are implemented in C code.

Example borrowed from this [great wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips):

	newlist = []
	for word in oldlist:
		newlist.append(word.upper())

Better:

	newlist = map(str.upper, oldlist)  # wiki calls 'map a for moved into C code'

Maybe more readable = list comprehension (still faster than the classic for loop):

	newlist = [s.upper() for s in oldlist]

But loads whole list in memory, so if size is an issue use a generator (lazy loading):

	iterator = (s.upper() for s in oldlist)

Good news is that in Python 3 range, d.items() etc return generators (still in Python2? ...)

Guido's [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) is a great read:

> If you feel the need for speed, go for built-in functions - you can't beat a loop written in C. Check the library manual for a built-in function that does what you want.

Another example of using builtins is the [collections](https://docs.python.org/2/library/collections.html) module which offers Pythonic and efficient data structures (deque, defaultdict, Counter, etc)

defaultdict is a really good example:

	>>> s = 'mississippi'
	>>> d = defaultdict(int)
	>>> for k in s:
	...     d[k] += 1

No need to see if key is in dict, faster, less code. As Jack Diederich says in [this great talk](https://www.youtube.com/watch?v=o9pEzgHorH0):

> I hate code and I want as little of it as possible in our product.

## 4. Use set operations where possible

I found this nice example [here](https://www.monitis.com/blog/7-ways-to-improve-your-python-performance/):

	for x in a:
		for y in b:
			if x == y:
				yield (x,y)

Try this instead which is faster:

	return set(a) & set(b)

Added benefit: 1 instead of 4 lines of code.

## 5. Use re.compile

If you have a big iterator and you need to do some regex matching, for example match a date:

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

## 6. Local vars

From the same [PerformanceTips wiki](https://wiki.python.org/moin/PythonSpeed/PerformanceTips) mentioned earlier: "Python accesses local variables much more efficiently than global variables.", for example:

	myfunc = myObj.func
	fcor i in range(n):
		myfunc(i) # faster than myObj.func(i)

## 7. Imports

Common sense but still: be conscious what you put in the module vs main level (latter being below \_\_main\_\_ statement). When you import a module potentially a lot of code runs and can slow down your program. Keep imports at the top of your program (don't import in a method), and just import what you need.

## 8. Ask for forgiveness

Using try/except usually leads to more readable code and is [considered more Pythonic](http://pybit.es/error_handling.html). It turns out it is also faster because it does not have to compute the if as I learned from this [great EuroPython talk](https://www.youtube.com/watch?v=YjHsOrOOSuI):

	if os.path.isfile(some_file):
		...

	try:
		with open(some_file) as f:
			...

Overall more Pythonic is easier to read but also faster. Another example is 'if variable:' being faster than the un-idiomatic 'if variable == True:' !

## 9. Avoid redundant copies

Honestly I like sorted() which can take an optional key argument. And I have never had to use sort() over sorted(). However to explain the difference when it matters: list.sort() sorts in place, sorted(list) creates a new list, hence is slower.

So as most of these techniques it depends on context. Another example is [\_\_slots\_\_](https://docs.python.org/2/reference/datamodel.html): 'the \_\_slots\_\_ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because \_\_dict\_\_ is not created for each instance', so this is really useful if you have a lot of instances (here is a [real-world example](http://tech.oyster.com/save-ram-with-python-slots/)).

## 10. Use a compiler

For example: [Cython](http://cython.org):

> Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language

Or [Numba](http://numba.pydata.org):

> Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, runtime, or statically

Here is [a talk on Numba](https://www.youtube.com/watch?v=eYIPEDnp5C4).

---

## How to spot performance issues?

Humans are pretty bad at guessing, use the [profile module](https://docs.python.org/3.6/library/profile.html) instead:

	python -m profile script [args ...]
	# add -o to save the output

And you can use the [timeit module](https://docs.python.org/3/library/timeit.html) (or simply time.clock()) to time blocks of code.

## Further reading (watching)

* Again [Python Patterns - An Optimization Anecdote](https://www.python.org/doc/essays/list2str/) sums up a lot of this in a nice and concise way.

* Mentioned [Writing faster Python](https://www.youtube.com/watch?v=YjHsOrOOSuI) by Sebastian Witowski.

* Book on the subject: [High Performance Python: Practical Performant Programming for Humans](https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1449361595/ref=sr_1_1?ie=UTF8&qid=1487234279&sr=8-1&keywords=high+performance+python).

---

Keep Calm and Code in Python!

-- Bob

Title: Read the stdlib: deque
Date: 2016-12-21 00:05
Category: Data types
Tags: collections, data structures, performance, stdlib, deque
Slug: collections-deque
Authors: Pybites
Summary: Use collections.deque to rotate letters in string (or elements in list). It has a native method which performs faster too.

## Deque

From the [stdlib docs](https://docs.python.org/2/library/collections.html#collections.deque):

> Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Coincidence: I was brainstorming how to rotate letters and independently I found the solution reading about deque later in the evening (see further down).

## Rotate without deque

One solution I found on Google / Stackoverflow shows a reasonable way to go:

	>>> def rotate(strg,n):
	...     return strg[n:] + strg[:n]
	... 
	>>> assert(rotate('hello', 2) == 'llohe')
	>>> assert(rotate('hello', -2) == 'lohel')

## Deque 2 birds: better performance and native rotate method

But using a list is not the most efficient way - see [TimeComplexity](https://wiki.python.org/moin/TimeComplexity) [1]

> Internally, a list is represented as an array; the largest costs come from growing beyond the current allocation size (because everything must move), or from inserting or deleting somewhere near the beginning (because everything after that must move). If you need to add/remove at both ends, consider using a collections.deque instead.

That led me to the collections.deque doc quotes at the start. Not only is it more efficient - O(1) vs O(n) - it also has a method that just does the rotation I wanted, so no need to define your own. 

Only note that that the pos/neg are the other way around this time:

> Rotate the deque n steps to the right. If n is negative, rotate to the left.

	>>> s = 'hello'
	>>> d = deque(s)
	>>> d
	deque(['h', 'e', 'l', 'l', 'o'])
	# 2 to left
	>>> d.rotate(-2)
	>>> d
	deque(['l', 'l', 'o', 'h', 'e'])
	# reset
	>>> d.rotate(2)
	>>> d
	deque(['h', 'e', 'l', 'l', 'o'])
	# 2 to right
	>>> d.rotate(2)
	>>> d
	deque(['l', 'o', 'h', 'e', 'l'])

## Reminder to self

Read code, read (stdlib) docs, and ask silly questions. "how do I ...?" makes you a better programmer. Even if you don't need it for anything specific you will find new ways, learn new tricks and those will make you better/faster when it does count.

---

[1] Here we also see the more expensive (and commonly used/needed) lookup 'x in s' for list = O(n) vs faster set/dict = O(1), see [hash table](https://en.wikipedia.org/wiki/Hash_table)

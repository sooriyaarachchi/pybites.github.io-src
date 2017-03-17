Title: Beautiful, idiomatic Python
Date: 2017-01-10 9:00
Category: Best practices
Tags: pythonic, cleancode, collections, 2vs3, namedtuples, decorators, contextmanagers
Slug: beautiful-python
Authors: Bob
Summary: [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go) is a must-watch to write more Pythonic code. In this post some highlights. 
cover: images/featured/pb-article.png

<div class="container">
<iframe src="https://www.youtube.com/embed/OSGv2VnC0go" frameborder="0" allowfullscreen class="video"></iframe>
</div>

## Resources

The slidedeck is [here](https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1).
Thanks Jeff Paine for this awesome [set of notes](https://gist.github.com/JeffPaine/6213790).

## When you see this, do that instead

A quick digest below. Note that Python3 takes some of these features to the next level, so switching from 2 to 3 is a good idea :)

* Use enumerate to loop over collections and indices, use reversed(collections) to loop backwards.

* Use the zip built-in to loop over two collections: zip(collection1, collection2). To make a dict from two collections: dict(zip(names, colors)). Use izip if the collections are not of the same length. 

* Use the sorted key argument to customize sort order of a collection, so to sort by dict value you can use: sorted(d.items(), key=lambda a: a[1])

* Use iter() if you need to call a function until a sentinel value, see a good example [here](http://amir.rachum.com/blog/2013/11/10/python-tips-iterate-with-a-sentinel-value/).

* The for / else construct can be useful to know if a loop made it to the end (that is no break was hit).

* Dicts: don't mutate a dictionary when looping over it! In Python3 dictionaries have [view objects](https://docs.python.org/3/library/stdtypes.html#dict-views): "The objects returned by dict.keys(), dict.values() and dict.items() are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.". For Python2 use iteritems() which returns an iterator (faster).

* Use collections.defaultdict to prevent initializing keys manually.

* Use ChainMap to link (concatenate) dictionaries together.

* Keyword arguments can make a function more readable, same goes for the light-weight namedtuple (collections module).

* Unpacking: bob, julian = 'bob julian'.split(), or a variable swap is as easy as a, b = b, a (no temp variable).

* Use ''.join(collection) instread of concatenating a string in a loop (more efficient).

* Use [deque](http://pybit.es/collections-deque.html) if you need a stack / queue ('linked list') instead of a regular list ('array'). When you do somecollection.insert(0, 'value'), it is time to change to a deque structure and use somecollection.appendleft('value').

* Use decorators to factor-out administrative logic, for example @cache, @timeit, etc. (use functools.lru_cache for caching starting 3.2).

* Use the with statement (context manager) to open and (automatically) close files. Another use case is threading locks or more generically when you need to factor-out "temporary contexts".

* Generator expressions are faster, you can use them (instead of list comprehensions) in sum() / max() / min() to gain performance. Hard to beat this for compactness: sum(i**2 for i in range(10))

Title: Book that makes algorithms accessible
Date: 2017-01-03 9:00
Category: Algorithms
Tags: algorithms, data structures, performance, collections
Slug: grokking_algorithms
Authors: Bob
Summary: I finished reading Grokking Algorithms, it's a very accessible resource for learning algorithms / data structures, highly recommended.
cover: images/featured/grokking-algorithms.png

[Grokking algorithms](https://www.manning.com/books/grokking-algorithms) is a unique gem. I discovered it on [episode 82 of Talk Python](https://talkpython.fm/episodes/show/82/grokking-algorithms-in-python). Knowing algorithms is fundamental for programming and problem solving. This book makes presents the key algorithms in an accessible way using great examples and over [hundreds of illustrations](https://github.com/egonSchiele/grokking_algorithms/tree/master/images) with [code samples in Python](https://github.com/egonSchiele/grokking_algorithms). Specially for self-taught programmers (like myself) this approach is awesome. After reading it I noted that I more easily grasp related books and I am now more confident picking up more advanced algorithms (which will be needed for Machine learning).

## Visual learning

This is a great summarizing video about some basic algorithms and how visually this stuff is presented:

<iframe src="https://www.youtube.com/embed/oo_sb4luiPo" frameborder="0" allowfullscreen class="video"></iframe>

## Performance 

The examples in the book are easy to follow. For example to explain the performance between an array (Python's list) and linked list (Python's [deque](http://pybit.es/collections-deque.html)) we are taken to the movies. What if you are 5 and a 6th friend joined? Possibly you have to relocate all 6 to find new seats if you are an array. Not so with a linked list, because the new friend can just sit 'anywhere' ( = linked to). This visualization stayed with me and I much better understand why inserts on arrays are slower.

And it does matter when your data set grows. [Expert Python](https://www.amazon.com/Expert-Python-Programming-Michal-Jaworski/dp/1785886851/ref=sr_1_1?ie=UTF8&qid=1483428099&sr=8-1&keywords=expert+python) provides a nice snippet in chapter 12 that shows the performance of array (list) vs linked list (deque):

	$ python3 -m timeit \
	> -s 'sequence=list(range(10000))' \
	> 'sequence.insert(0, 0); sequence.pop(0)'
	100000 loops, best of 3: 9.12 usec per loop

	$ python3 -m timeit \
	> -s 'from collections import deque; 
	> sequence=deque(range(10000))' \
	> 'sequence.appendleft(0); sequence.popleft()'
	10000000 loops, best of 3: 0.204 usec per loop

See Python's [TimeComplexity wiki](https://wiki.python.org/moin/TimeComplexity) for performance details on stdlib collections.

## Cool use cases

Some cool stuff you can do with basic algorithms: 

* Hashtable lookups (dict, set) are O(1) so they are ideal for building search engines. On the mentioned episode of Talk Python Michael Kennedy mentions he made the search for his show using dicts because of this performance advantage.

* Recusion provides elegant solutions. The book shows an example of finding a key in boxes, the recursive solution is much shorter and cleaner. 

* Always wondered how Netflix recommends those cool movies to you? They are probably using the [k-nearest neighbors algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) (k-nn) 

* Graphs: what is the shortest path on Facebook between you and Brad Pitt? Similarly what' the shortest path from NY to LA? You can use [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm).


## Conclusion

The explanation of Big O, array vs list and hash tables (Maggie!) are worth the price alone, but there is much more. If you are new to algorithms or need a refresher this is a great book.

---

Keep Calm and Code in Python!

-- Bob

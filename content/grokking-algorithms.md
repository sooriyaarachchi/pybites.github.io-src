Title: A great book that makes algorithms accessible
Date: 2017-01-03 9:00
Category: Books
Tags: algorithms, data structures, performance, collections
Slug: grokking_algorithms
Authors: Bob
Summary: I finished reading Grokking Algorithms, it's a very accessible resource for learning algorithms / data structures, highly recommended.
cover: images/featured/pb-article.png

[Grokking algorithms](http://amzn.to/2nFlsPg) is a unique gem. I discovered it on [episode 82 of Talk Python](https://talkpython.fm/episodes/show/82/grokking-algorithms-in-python). Knowing algorithms is fundamental for programming and problem solving. This book presents the key algorithms in an accessible way using great examples and [hundreds of illustrations](https://github.com/egonSchiele/grokking_algorithms/tree/master/images) with [code samples in Python](https://github.com/egonSchiele/grokking_algorithms). Specially for self-taught programmers (like myself) this approach is awesome. After reading it I noted that I more easily grasp related topics in other books and I am now more confident picking up more advanced algorithms (which will be needed when learning ML).

## Visual learning

This is a great summarizing video about some basic algorithms and the way the book teaches them:

<div class="container">
<iframe src="https://www.youtube.com/embed/oo_sb4luiPo" frameborder="0" allowfullscreen class="video"></iframe>
</div>

## Performance 

The examples in the book are easy to follow. For example to explain the performance between an array (Python's list) and linked list (Python's [deque](http://pybit.es/collections-deque.html)) we are taken to the movies. What if you are 5 and a 6th friend joined? Possibly you have to relocate all 6 to find new seats if you are an array. Not so with a linked list, because the new friend can just sit 'anywhere' ( = linked to). This visualization stayed with me and I much better understand why inserts on arrays are slower.

And it does matter when your data set grows. [Expert Python](http://amzn.to/2lxLQ91) provides a nice snippet in chapter 12 that shows the performance of array (list) vs linked list (deque):

	$ python3 -m timeit \
	> -s 'sequence=list(range(10000))' \
	> 'sequence.insert(0, 0); sequence.pop(0)'
	100000 loops, best of 3: 9.12 usec per loop

	$ python3 -m timeit \
	> -s 'from collections import deque; 
	> sequence=deque(range(10000))' \
	> 'sequence.appendleft(0); sequence.popleft()'
	10000000 loops, best of 3: 0.204 usec per loop

Another good example is binary search. Compared to selection sort the number of steps needed to search a (sorted) list goes from 4 billion down to 32. That demonstrates an important concept of Big O, quoting the book: "algorithm times are measured in terms of growth of an algorithm." Fascinating! 

See Python's [TimeComplexity wiki](https://wiki.python.org/moin/TimeComplexity) for performance details on all stdlib collections.

## Cool use cases

Some cool stuff you can do with basic algorithms: 

* Hashtable lookups (dict, set) are O(1) so they are ideal for building search engines. On the mentioned episode of Talk Python Michael Kennedy explained he made the search for his show using dicts because of this.

* Recusion provides elegant solutions. The book shows an example of finding a key in boxes, the recursive solution is much shorter and cleaner. And recursion at its simplest really comes down to [just a few lines of code](https://github.com/egonSchiele/grokking_algorithms/blob/master/03_recursion/python/01_countdown.py):

		def countdown(i):
		print i
		# base case
		if i <= 0:
			return
		# recursive case
		else:
			countdown(i-1)

		countdown(5)

	For example to do a manual os.walk it only takes this: 

		def get_files_in_dir(dirname="."):
			for file_name in os.listdir(dirname):
				abs_path = os.path.join(dirname, file_name)
				if os.path.isdir(abs_path):
					yield from get_files_in_dir(abs_path)
				else:
					yield abs_path

* Wondered how Netflix recommends those cool movies to you? They are probably using the [k-nearest neighbors algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) (k-nn) 

* Graphs: what is the shortest path on Facebook between you and Brad Pitt? Similarly what is the shortest path from NY to LA? You can use [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm).

* Dynamic programming is useful when you’re trying to optimize something given a constraint. The book starts out with the 'knapsack problem': maximizing the value of a set of goods to steal, being constrained by the size of the knapsack. 

	Then it shows a simple implementation of suggesting similar words based on misspelled words (like Google). This is a bit more complex to grasp but very powerful. This chapter, as all the others, shows a lot of practical / real life use cases.

## Conclusion

The explanation of Big O, array vs list and hash tables (meet Maggie!) are worth the price alone, but there is much more. If you are new to algorithms or need a refresher this is un unmissable book.

---

Keep Calm and Code in Python!

-- Bob

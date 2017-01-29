Title: Python Tricks book review
Date: 2017-01-31 09:00
Category: Books
Tags: review, tricks, tips, pythonic, oop, ABCs, dicts, cleancode
Slug: pytricks-review
Authors: Bob
Summary: A review of Dan Bader's [Python tricks book](https://dbader.org/products/python-tricks-book/).
Status: draft
cover: images/featured/pytricks-review.png

A review of Dan Bader's [Python tricks book](https://dbader.org/products/python-tricks-book/):

> Discover Python’s Best Practices with Simple Examples and Start Writing Beautiful & Pythonic Code

### Take your Python to the next level

I found out about this book through Dan's Python Tricks I get via email / Twitter. The book defines:

> Python Trick: A short Python code snippet meant as a teaching tool. A Python Trick either teaches an aspect of Python with a simple illustration, or serves as a mo- tivating example to dig deeper and develop an intuitive understanding.

I really enjoyed reading Dan's book. He explains important Python aspects with clear examples (using two twin cats to explain "is" vs "==" for example). It is not just code samples, it discusses relevant implementation details comprehensibly.

Since [this talk by Raymond Hettinger](https://www.youtube.com/watch?v=wf-BqAjZb8M) I am more conscious about writing Pythonic code. This book cares too. Most tricks show the "one-- and preferably only one --obvious way to do it" (import this), for example how to merge dicts, use try/except ([EAFP style](https://docs.python.org/3/glossary.html)) but prefer dict.get() as being even more precise. The beginner gets into Pythonic mode, the expert might still pick up new stuff. Another good book in this context is [Effective Python: 59 Specific Ways to Write Better Python](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134034287/ref=sr_1_1?ie=UTF8&qid=1485688050&sr=8-1&keywords=effective+python).

### Few things I learned (refreshed) 

* Language features section: the "is" vs "==" I mentioned, dictionary internals, deep vs shallow copy. The article on 4 ways of string formatting is awesome. I like Dan’s Python String Formatting Rule of Thumb:

	> If your format strings are user-supplied, use Template Strings to avoid security issues. Otherwise, use Literal String Interpolation if you’re on Python 3.6+, and "New Style" String Formatting if you’re not.

* Cleaner Python section (my favorite part of the book): use your own exceptions (which we used [here](http://pybit.es/error_handling.html)), ABC's (we used [here](http://pybit.es/oop-primer.html)), the key func of sorted() (we used [here](http://pybit.es/codechallenge01_review.html)), which is shown with both lambda and operator.getitem syntax, refactoring an ugly switch statement.

* Pythonic syntactic sugar section: * and ** (splat) function arg unpacking (very Pythonic), various (stdlib) ways to merge dicts. 

### Now is better than never (import this)

And more so because you can still get it for just 9 bucks, eventually it will cost 29.

Keep in mind this is a work in progress. I did find the initial version of 60 pages a bit short, but recently I got an update of 25+ pages so the final version will be longer. 

What really matters though is that this book makes you write better Python code! Actually I think the recent tricks I added to my pyhabits, custom exceptions and use ABC's (how I found his blog in the first place), are worth the price alone. 

Thanks Dan for sharing your great work.

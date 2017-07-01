Title: From Script to Project part 2. - Packaging Your Code in Python
Date: 2017-07-01 10:45
Category: Learning
Tags: packaging, modules, init, imports, refactoring, karma, Twitter
Slug: python-packaging
Authors: Bob
Summary: This week's article is about packaging your Python code. Sounds daunting? Actually it is pretty simple.
cover: images/featured/pb-article.png

> Namespaces are one honking great idea -- let's do more of those!

This week's article is about packaging your Python code. Sounds daunting? Actually it is pretty simple.

Last week we introduced [Karma Bot](https://github.com/pybites/karmabot) in part 1 of this series. I will use it to show you how I ended up organizing the code. Then I will show a simpler script refactored into a package.

Packaging your code makes it easier for others to use. It also adds more structure to your code which leads to more maintainable code. Finally it namespaces your code, *one honking great idea*.

At the very basic level you create a package by putting one or more modules (.py files) inside a folder together with a \_\_init\_\_.py file. This file turns the folder into a package. Your code should ideally not go in that file. It is used for imports and setup.

## Example 1 - Karma bot

At this moment karmabot has two packages:

	$ ls bot
	__init__.py    karma.py    slack.py    

	$ ls utils
	__init__.py    get_botid.py

And `main.py` in the top level directory is the driving script:

	$ ls
	...
	main.py
	...

There is not one best way to structure your code. A better grouping could be adding `slack.py` and `get_botid.py` to a *slack* package. Work in progress.

At least this is far better than the first version where I had all code in one big file. Unfortunately this was before my first commit so cannot retrieve it. That's why I have another example lined up ... 

## Example 2 - Twitter Archive Stats

This is a smaller script so better to demo. Take a minute to look at the [original script](https://github.com/pybites/100DaysOfCode/blob/master/086/twitter_archive.py).

> This code is part of our [100 Days of PyBites, 100 Days of Code](https://pybit.es/special-100days.html) (days 086 and 093) which we are about to finish. Stay tuned for a review article next week!

As you see all the code is lumped together in one file. There is also way too much going on under `if __name__ == '__main__'`. This is not code we can re-use. Most scripts start like this. If you don't step back every now and then though, it becomes a mess.

> A great book on refactoring I read this year is Martin Fowler's [Refactoring](https://martinfowler.com/books/refactoring.html). Read it. You will write better code!

Packaging to the rescue! Here are the steps:

- First. Don't write any code yet. Think about the various things this script tries to accomplish. What are the main responsibilities? In this case it:

	1. parses the data from `tweets.csv`, the exported Twitter archive,
	2. parses the obtained data from 1., counting certain metrics,
	3. prints the results to stdout.

- So it does 3 things. As it is a small script one package is fine. I created a folder called "archive" with:

	- a module (Python script file) for each functionality,
	- an \_\_init\_\_.py file that turns it into a package.

- Then I started moving code around. This actually led to additional refactoring! For example the `for row in data:` block was reduced from 25 to 15 lines using the [extract method](https://refactoring.com/catalog/extractMethod.html). The additional helper methods also made it more readable.

> Refactoring your code is a positive side effect of packaging!

- One note on imports. Starting off with:

		$ ls
		archive    main.py

	Adding the init file to the archive package, in `main.py` I could import like this:

			from archive.report import print_header, print_results
			...

	It's common to make this shorter by bringing the imports into the package namespace:

		$ more archive/__init__.py
		from .tweets import parse_csv
		from .stats import calc_stats
		from .report import print_header, print_results

	Now I can just import from archive, reducing 3 import statements to only 1: 

		from archive import parse_csv, calc_stats, print_header, print_results

	See also the article [Be Pythonic: \_\_init\_\_.py](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html).

## Reference

Next thing you want to do is add a `setup.py` etc to make your code distributable. You could use a tool like [cookiecutter]((https://github.com/audreyr/cookiecutter)) for this. We will explore this further in part 5. First we dive into testing and documentation in part 3 and 4.

In closing here are some links for further inspection:

- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [A Simple Guide for Python Packaging](https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5)
- [Cookiecutter - a cli utility that creates projects from cookiecutters](https://github.com/audreyr/cookiecutter)

---

Keep Calm and Code in Python!

-- Bob

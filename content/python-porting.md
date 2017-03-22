Title: Best Practices for Compatible Python 2 and 3 Code
Date: 2017-03-22 12:42
Category: Tools
Tags: 2vs3, tox, six, python-modernize, porting, future, 2to3, coverage, futurize, caniusepython3, pip, Requests, Werkzeug
Slug: python-porting
Authors: Bob
Summary: [95% of most popular Python packages support Python 3](http://py3readiness.org/). Maybe you are lucky and get to start fresh using Python 3. However as of last year [Python 2.7 still reigns supreme in pip installs](http://www.randalolson.com/2016/09/03/python-2-7-still-reigns-supreme-in-pip-installs/) and at a lot of places 2.x is the only version you get to work in. I think writing Python 2 and 3 compatible code is an important skill, so lets check what it entails.
cover: images/featured/pb-article.png

[95% of most popular Python packages support Python 3](http://py3readiness.org/). Maybe you are lucky and get to start fresh using Python 3. However as of last year [Python 2.7 still reigns supreme in pip installs](http://www.randalolson.com/2016/09/03/python-2-7-still-reigns-supreme-in-pip-installs/) and a lot of places 2.x is the only version you get to work in. I think writing Python 2 and 3 compatible code is an important skill, so lets check what it entails.

> Python 2.x is legacy, Python 3.x is the present and future of the language - [Python2orPython3 wiki](https://wiki.python.org/moin/Python2orPython3)

## Summary Best Practices

The best place to start is the HOWTO: [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html) which nicely summarizes the important:

* Only care about Python 2.7 ("Python 2.6 is no longer freely supported and thus is not receiving bugfixes."). If you have to care about older Python 2.x versions use [six](https://pypi.python.org/pypi/six).

* Have good test coverage (pip install [coverage](https://pypi.python.org/pypi/coverage)), You can use [tox](https://pypi.python.org/pypi/tox) to test against multiple Python versions.

* Learn the differences between 2 and 3, see [this nice Cheat Sheet](http://python-future.org/compatible_idioms.html). Another nice article is: [The key differences between Python 2.7.x and Python 3.x with examples](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

* Use existing tools: [Futurize](http://python-future.org/automatic_conversion.html), [Python-Modernize](https://python-modernize.readthedocs.io/en/latest/), [caniusepython3](https://pypi.python.org/pypi/caniusepython3). One word of caution about code translation tools: they might lead to less idiomatic or unnecessary code. In [Picking a Python Version: A Manifesto](http://www.oreilly.com/programming/free/from-future-import-python.csp) we see [2to3](https://docs.python.org/2/library/2to3.html) converting a range to list(range), you probably want a range to be 'lazy'. On the other hand, in the same example a map gets converted to a list comprehension which is more readable. The point is to always manually check any automatic conversions.

* To test text versus binary, handled differently between 2 and 3, you can use [mypy](http://mypy-lang.org), an optional static type checker. String handling differences in 2 vs 3 probably warrant another article ...

## The future and syntax

* You can use [\_\_future\_\_ imports](http://python-future.org/imports.html) in Python 2 to provide forward-compatibility, for example:

		from __future__ import (absolute_import, division,
								print_function, unicode_literals)

	Most well-known is the print statement in 2 becoming a function in 3. To use 3's input (instead of 2's raw_input), range (instead of 2's xrange), you can use builtins:

		from builtins import (bytes, str, open, super, range, zip, round, input, int, pow, object)

	> python-future is the missing compatibility layer between Python 2 and Python 3. It allows you to use a single, clean Python 3.x-compatible codebase to support both Python 2 and Python 3 with minimal overhead.

	See [this overview](http://python-future.org/overview.html) for more info.

* Use try/except on your imports (the HOWTO prefers this over version detection code):

		try:
			import configparser
		except ImportError:
			import ConfigParser as configparser

		try:
			import simplejson as json
		except (ImportError, SyntaxError):
			import json


* Write exceptions in a compatible way:

		# don't:
		except Exception, e:
		# do:
		except Exception as e:
		# or just:
		except Exception:
		# don't:
		raise ValueError, 'Invalid value'
		# do:
		raise ValueError('Invalid value')

* Things like from \_\_future\_\_ and try/except imports can be wrapped in a compat.py module , see [Requests](https://github.com/kennethreitz/requests/blob/master/requests/compat.py) or [Werkzeug](https://github.com/pallets/werkzeug/blob/master/werkzeug/_compat.py) for example. I actually learned about this technique in the 'Reading Great Code' chapter of [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/). Armin Ronacher's [Porting to Python 3 Redux](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/) provides some more examples of what you can add to your compat module, including decorators for differences in string handling, dictionaries and iterators.

* The mentioned [Cheat Sheet](http://python-future.org/compatible_idioms.html) sums up all compatible idioms nicely.

## Why it matters

It might take extra lines of code and be less idiomatic, but if on 2.x you probably have to migrate at some point. Python 2.7 [will not be maintained past 2020](https://pythonclock.org/).

Also if you release a package, doing a bit of extra effort might increase the amount of users of your software. [Randy Olson's pip install analysis](http://www.randalolson.com/2016/09/03/python-2-7-still-reigns-supreme-in-pip-installs/) made me think.

This article only scratched the surface. Now is a good time to become familiar with Python porting. I learned some tricks writing this article, hopefully it gets you started too. The amount of resources available is impressive. One final site / book: [Supporting Python3](http://python3porting.com). 

Good luck and let us know in the comments what imcompatible code you had to deal with, we like to hear your story ...

---

Keep Calm and Code in Python!

-- Bob

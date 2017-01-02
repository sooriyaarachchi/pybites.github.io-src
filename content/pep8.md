Title: 5 min guide to PEP8
Date: 2017-01-02 9:00
Category: Best practices
Tags: pep8, cleancode, guidelines, coding style, best practices
Slug: pep8
Authors: Bob
Summary: Today a post on PEP8, the Style Guide for Python Code
cover: images/featured/pep8-5min.png

> One of Guido's key insights is that code is read much more often than it is written - PEP8

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler

After Julian's two recent style posts on [indentation](http://pybit.es/indentation_tips.html) and [naming convention](http://pybit.es/naming_conventions.html) a nice follow-up is [PEP8](https://www.python.org/dev/peps/pep-0008/), the Style Guide for Python Code. Also a comment on Twitter caught my eye stating that even book authors do not always follow PEP8!

## Why bother?

I think everybody writing code in Python should become familiar with PEP8 and use its guidelines rather sooner than later.

It leads to more readable code which saves brain cycles and better maintainable code (= fewer bug).

Of course there can be exceptions to the rule, PEP8 states: "do not break backwards compatibility just to comply with this PEP!" - Raymond Hettinger did a great talk on this: [Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

## Summary of the guidelines

A read that is aimed for '5 min' cannot have all, so I just summarize what I think is important, read the full spec for details:

* Use 4 spaces per indentation level. Use spaces, not tabs. See [our post](http://pybit.es/indentation_tips.html) for more on this, including recommended .vimrc settings.

* Limit all lines to a maximum of 79 characters. Usually I have a script.py and test_script.py open, vertically alligned (vi -O file1 file2), keeping lines short makes this very convenient.

* Imports I) be as specific as possible with your imports: 

		# don't do: 
		from time import *
		(unless needed, then use the __all__ mechanism to prevent exporting globals)
		# do:
		from time import time
		# or:
		import time
		# then prepends each method with module name: 
		time.time()

* Imports II) absolute imports are recommended:

		from mypkg.sibling import example	
		# over
		from .sibling import example

* Imports III) split imports in stdlib - third party - application/library specific. For example our [twitter bot](https://github.com/pybites/blog_code/blob/master/twitter_bot/tweetbot.py) followed this convention:

		# stdlib
		import datetime
		import logging
		import time

		# pip installed
		import feedparser
		import tweepy

		# app modules
		from config import ...
		...

* Watch your [use of whitespace](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements): this takes practice, but becomes habit/ automatic over time.

* Comments that contradict the code are worse than no comments, so keep them up2date. Use inline comments sparingly. Of course good code is mostly self-documenting.

* Use docstrings, they are a great aid for auto-documenting your project with tools like [Sphinx](http://www.sphinx-doc.org/en/1.5.1/). Here is the [recommended syntax](https://www.python.org/dev/peps/pep-0257/): 

		"""Multi-line docstrings consist of a summary line just like a one-line docstring

		Followed by a blank line, followed by a more elaborate description. 
		"""

* Naming:

	- Non-public methods and instance variables start with a leading underscore: _helper_method(), although not enforced by the compiler, the reader knows this is an internal method, not to be called from outside of the class.

	- If you need to use a Python keyword append an underscore: str_ = 'bob'

	- You probably want to avoid single-char variables all together, but if you use them never use these easily confused chars: 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye).
	
	- Use CapWords for class names.

	- Use short, all-lowercase names for modules.

	- Constants are all uppercase, in our Twitter bot example: CONSUMER_KEY, CONSUMER_SECRET, etc.

* [Programming Recommendations](https://www.python.org/dev/peps/pep-0008/#programming-recommendations) has some great tips: use ''.join(list) instead of string concatenation which is slow, use str.startswith/endswith instead of slicing (or more generically don't re-invent the wheel), boolean checks don't need == True/False, etc. 

	Interesting is the part on exceptions: two common mis-uses are putting too much in the try block, or catching exceptions that are too generic, so train yourself to use specific exceptions: 'except SomeError' instead of the catch-all 'except'.

## Tools to check for compliant PEP8 

You can use [pep8](https://pypi.python.org/pypi/pep8)

	$ pip install pep8

Our [digest.py](https://github.com/pybites/blog_code/blob/master/pybites_digest/digest.py) seemed compliant but let's make some edits to see this checker in action. I changed spaces from 4 to 2 in a method, mis-aligned a multi-line statement, and removed a whitespace before '='. Of course pep8 complains: 

	$ pep8 digest.py 
	digest.py:24:3: E111 indentation is not a multiple of four
	digest.py:25:3: E111 indentation is not a multiple of four
	digest.py:26:3: E111 indentation is not a multiple of four
	digest.py:50:18: E225 missing whitespace around operator
	digest.py:54:80: E501 line too long (83 > 79 characters)

Another tool is [flake8](https://pypi.python.org/pypi/flake8) which is "a wrapper around these tools: PyFlakes, pycodestyle and Ned Batchelder’s McCabe script". It also has a nice [integration in Vim](https://github.com/nvie/vim-flake8): it runs the checks and presents them in a split window with line numbers, pretty convenient! 

![flake 8 inside vim]({filename}/images/flake8_vim.png)

Btw I got this split window pressing ,f which I find easier on a Mac than F7, you can create a shortcut like this in your .vimrc:

	autocmd FileType python map <buffer> ,f :call Flake8()<CR>

## Wrapping it up

Following PEP8 leads to code that is more easy to read an maintain. PEP8 is required reading for any Python developer. Read the full doc and start using it in your code. Using a linter tool is the best way to train yourself. Just google for plugins / integration with your favorite editor.

Any feedback, questions or experiences, use the comments below.

---

Keep Calm and Code in Python!

-- Bob

Title: Python Testing With Pytest
Date: 2017-09-25 14:53
Category: Books
Tags: pytest, testing, books, tox, Jenkins, fixtures, unittest, q&a
Slug: pytest-book
Authors: Bob
Summary: Review of [Brian Okken](https://twitter.com/brianokken)'s new [pytest book](http://www.amazon.com/dp/1680502409/?tag=pyb0f-20).
cover: images/featured/pb-article.png

Review of [Brian Okken](https://twitter.com/brianokken)'s new [pytest book](http://www.amazon.com/dp/1680502409/?tag=pyb0f-20).

## Nice, a book about pytest

Writing reliable software requires testing and pytest is a great aid in being more productive at it.

Brian did a great job exploring this awesome framework. Getting started was easy, yet I was amazed at all the powerful features the framework has to offer like fixtures, a robust plugin system and a large amount of configuration options.

Let's do some Q & A ...

### What you might be wondering

* Q: I am a Python developer, is this book for me?

	A: yes, testing is important and pytest makes it easier yet supporting complex testing. If you can use it at work or your open source projects cool, but even if you can't, it's still fascinating to read about this testing framework.


* Q: what's the extra value of the book over the pytest docs?

	A: pytest has great docs! This is a book to read end-to-end though, a more didactic resource as opposed to a reference manual. It makes pytest accessible through a simple *Tasks* CRUD/DB app. The code samples are clean (pep8) and easy to follow.

* Q: what is the time investment?

	A: The book is short and concise. You can read it in two evenings: evening #1 = ch1-3 - now you can write tests with pytest / evening #2 = ch4-7 - more advanced stuff and integrations. Secondary topics are in the appendices keeping the main text lean.

* Q: what are wins of pytest over the builtin unittest framework?

	A: less verbose (assert vs. self.assertEqual etc.) / classes are not required, rich cli interface, informative test failures, a more convenient way to write setup/teardown functions with fixtures, parameterised tests, better test runner (marker- and name-based test selection).

* Q: what did you learn from this book?

	A: it taught me a lot of what makes pytest great. Take out your notebook because you will learn a lot of practical tips. Fixtures are well explained. Some other cool things: using pdb with pytest, smart test selection with markers / parameterization / cli -k arg (works like grep), builtin fixtures like capsys (capture stdout), cache test results for the next run (session), and integrate with Jenkins CI.

* Q: why is *[fixtures](https://docs.pytest.org/en/latest/fixture.html)* a killer feature?

	A: to quote the book: "pytest fixtures ... are the reason why many people switch to and stay with pytest. ... one of the great reasons to use fixtures: to focus the test on what you’re actually testing, not on what you had to do to get ready for the test." and to quote the docs: "pytest fixtures: explicit, modular, scalable".

* Q: does it teach TDD?

	A: no, it would have been nice, but thanks to the book's focus on pytest it covers a lot in relatively few pages.

* Q: Does the book go into testing environments / installation/ tools?

	A: yes, in chapter 7 it dicsusses tools like coverage, Jenkins, mock and tox, making it more well rounded / real world. It also quickly demos cookiecutter and explains how to install packages and package your own code. It that sense the book is for all levels of experience.

![pytest book cover]({filename}/images/pytest-book-poster.png)

Get it from [The Pragmatic Bookshelf](https://pragprog.com/book/bopytest/python-testing-with-pytest) or [Amazon](http://www.amazon.com/dp/1680502409/?tag=pyb0f-20).

## Conclusion

This is a book you want to own. Testing is important and using pytest you're doing yourself a favor.

The book is concise and can be read in 2 evenings. I have to yet fully explore pytest's docs but this book is a great teaching resource, using a simple / practical CRUD/DB app to teach pytest.

The book offers a nice digest of more advanced pytest features and the config/plugins/testing tools sections makes for an optimal use of the framework. Recommended.

But as with all books, mastering comes with practice. Stay tuned for next week's code challenge #38 where we will let you experiment more with pytest ...

---

Keep Calm and Code in Python!

-- Bob

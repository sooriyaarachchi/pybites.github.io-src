Title: Code Challenge 14 - Write DRY Code With Decorators - Review
Date: 2017-04-15 01:00
Category: Challenges
Tags: codechallenges, learning, decorators, design patterns, DRY
Slug: codechallenge14_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge14.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Write DRY Code With Decorators](http://pybit.es/codechallenge14.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Our solution and learning

Getting our hands on decorators we enriched our Python toolkit!  This one was also a lot of fun. See our solution [here](https://github.com/pybites/challenges/blob/solutions/14/decorator-pb.py). We did a simple timeit one and a more complex mute_exception one. For the latter we needed this week's article: [How to Write a Decorator with an Optional Argument?](http://pybit.es/decorator-optional-argument.html). 

Some other things we learned: 

* Know the stdlib. Part of what makes these decorators useful is knowing about time, random, the @wraps decorator, partial, the awesome logging module, etc.

* As we sensed using optional arguments made the mute_exception more versatile. You can run it in various ways: 

        @mute_exception                                    # works: no args provided = takes defaults (no reraise, returns None)
        @mute_exception(reraise=True)                      # works: raises the ZeroDivisionError = crash
        @mute_exception(reraise=False, default_return=0)   # works: does not reraise ZeroDivisionError and returns 0 in that case 

* We used f-strings! We are on Python 3.6 now so we just could no longer resist the temptation :)

* Our [Flake 8 Check Vim shortcut](http://pybit.es/vim-tricks.html) pays off: the code is more readable.

* Keep reading other blogs and books. We based these decorators on [How to Create an Exception Logging Decorator](https://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/) and the almighty [Python Cookbook, Third edition](https://www.amazon.com/dp/1449340377/?tag=pyb0f-20).

## Output 2 stacked decorators

When you run our solution it will print (fake) timings and mute/log the ZeroDivisionError exception:

	$ python decorator-pb.py

	div of args: (1, 4) took 0.755037784576416
	div 1/4 = 0.25

	div of args: (2, 5) took 0.763498067855835
	div 2/5 = 0.4

	div of args: (3, 0) took 0.09057903289794922
	div 3/0 = 0

The program did not crash by the divide by 0, logging the exception:

	$ tail decorators.log
	...
	...
	00:58:36 root         DEBUG    div called for args (1, 4)
	00:58:36 root         DEBUG    div called for args (2, 5)
	00:58:37 root         DEBUG    div called for args (3, 0)
	00:58:37 root         ERROR    div raised exception ZeroDivisionError for args: (3, 0)

## Community 

But there is more ... we got a [nice PR](https://github.com/pybites/challenges/blob/community/14/decorator-clamytoe.py) with two other cool decorators: 

* boxit - a decorator to draw a box around text
* hashit - a decorator to securely hash passwords (using passlib)

## Next Up

As you might have noticed ([here](http://pybit.es/beginning-flask.html) and [here](https://twitter.com/pybites/status/851896144594583552)) we are learning Flask so we thought it would be a great topic for our next challenge coming Monday. Stay tuned ...

We hope you are enjoying these challenges, learning along the way. Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...

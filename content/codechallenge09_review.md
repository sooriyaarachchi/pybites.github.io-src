Title: Code Challenge 09 - With Statement / Context Manager - review
Date: 2017-03-11 09:00
Category: Challenges
Tags: codechallenges, code review, learning, with, contextmanagers, ssh
Slug: codechallenge09_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge09.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge09.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Learning

### Julian

Admittedly, when Bob and I discussed this challenge, I was a little intimidated. I'd never actually dealt with any of these concepts before! That said, I'm so glad we put this one out there!

If it wasn't for the challenge, I wouldn't have learned nearly as much as I did.

Given my current job role, I decided that it'd be fun to try and wrap a context manager around SSH functionality. This was a perfect choice given you need to specifically call .close() to close off the SSH session. If not, it just stays open indefinitely (or until timeout).

All up, I had to solidify my understanding of generators, context managers and ssh within Python.
In a venv, I installed the [paramiko SSH package](http://www.paramiko.org/) and went from there.

After figuring out how to get the SSH connection going, I then spent the time bundling it all up within the context manager. [Dan Bader's post](https://dbader.org/blog/python-context-managers-and-with-statement); the [pep-0343 doc](https://www.python.org/dev/peps/pep-0343/) and a few Googled questions on Stack Overflow helped sort me out.

See the full code [here](https://github.com/pybites/challenges/blob/solutions/09/with_ssh.py). Not only does it work, but I'm also now using at home with my NAS!

### Bob

This was a nice challenge. I got inspired by the DB rollback example of [PEP 343](https://www.python.org/dev/peps/pep-0343/). I wanted to see if I could use some existing code. 

That's why I did some refactoring on my [Simple Flask API](http://pybit.es/simple-flask-api.html) test code. Just as an exercise, in real life I actually like the setUp/tearDown sandwich unittest already provides. 

What I really liked was that I got to think about different ways to implement this: [class](https://github.com/pybites/challenges/blob/solutions/09/with_testdb_class.py) vs [contextmanager](https://github.com/pybites/challenges/blob/solutions/09/with_testdb.py). All this experimentation led to some good learning, Julian experienced the same working on his solution.

And I got to use pytest :)

	(venv) [bbelderb@macbook 09 (solutions)]$ pytest with_tes*
	=== test session starts ===
	...

	with_testdb.py ..
	with_testdb_class.py ..

	=== 4 passed in 0.01 seconds ===

## Feedback

What was your solution? Feel free to share in the comments below.

We hope you enjoy these challenges. Please provide us feedback if we can improve anything ...

If you have an interesting challenge you want us to feature, don't hesitate to reach out to us.

See you next week ...

Title: Code Challenge 24 - Use Dunder / Special Methods to Enrich a Class
Date: 2017-06-20 09:50
Category: Challenges
Tags: codechallenges, dunders, special methods, magic methods, classes, polymorphism, operator overloading, guest
Slug: codechallenge24
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! We wrote an article for Dan Bader's Python blog: [Enriching Your Python Classes With Dunder (Magic, Special) Methods](https://dbader.org/blog/python-dunder-methods). We hope you like it. To put dunders into practice we dedicate this week's code challenge to it.
cover: images/featured/pb-challenge.png

> A smooth sea never made a skilled sailor. - Franklin D. Roosevelt

Hi Pythonistas, a new week, a new 'bite' of Python coding! We wrote an article for Dan Bader's Python blog: [Enriching Your Python Classes With Dunder (Magic, Special) Methods](https://dbader.org/blog/python-dunder-methods). We hope you like it. To put dunders into practice we dedicate this week's code challenge to it.

## What Are Dunder Methods?

To quote from our guest post:

> In Python, special methods are a set of predefined methods you can use to enrich your classes. They are easy to recognize because they start and end with double underscores, for example `__init__` or `__str__`. .... This elegant design is known as the Python data model and lets developers tap into rich language features like sequences, iteration, operator overloading, attribute access, etc.

## The challenge

* Basic: take an existing class you wrote or write one from scratch (other than Account), implementing at least construction, object representation and iteration using special methods.

* Intermediate to Advanced: implement one or more of the other language features discussed in the article: operator overloading, method invocation, context management. And/or look at the [data model documentation](https://docs.python.org/3/reference/datamodel.html) and try to implement one or more dunders not discussed in the article: attribute access, metaclasses or coroutines for example. 

* Bonus: write some tests to verify the dunders you have implemented behave as expected.

---

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

### New PR template

Note that when you do a PR you should see a short template asking for some meta data. We implemented that [as part of code challenge 23](https://pybit.es/codechallenge23_review.html) to track our challenges and over time enrich our [Challenges page](https://pybit.es/pages/challenges.html).

## Feedback

If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

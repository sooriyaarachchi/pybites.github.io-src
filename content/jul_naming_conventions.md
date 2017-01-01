Title: Python Naming Conventions
Date: 2017-01-01 11:14
Category: Learning
Tags: learning, python, beginners, tips, cleancode, best-practices
Slug: naming_conventions
Authors: Julian
Summary: Naming conventions can be tricky in Py. It's good to make sure we're all on the same page.
cover: images/featured/python_naming_conventions.png

As I mentioned in my [Automate the Boring Stuff review](http://pybit.es/automate_the_boring_stuff_review.html), I was led astray with regards to naming my functions and variables. That is, the book was telling me to use camelCase rather than the approved underscore method.

After writing that article I decided to do some digging and I totally feel this needs a dedicated post!

## The Consensus

A lot of people are divided on this topic! Doing a quick Google search found people who believe it doesn't matter what you use and those that would fight for their chosen method.

The one thing everyone agrees on however is that you need to remain consistent. If you decide to use camelCase in your code, then do so for the entirety of your project, **don't mix**.


## Quick Example

After Bob informed me that camelCase *wasn't* the way to go, I went through and renamed all of my functions and variables using the underscore method. Here's a quick snippet in case you don't know what this all looks like:

**camelCase**
~~~~
happyNewYearEveryone():
    partyTime()
~~~~

**Underscore Method**
~~~~
happy_new_year_everyone():
    party_time()
~~~~


## Sticking with PEP8

I did wonder where this guidance was coming from though. How did Bob know this was exactly how it should be?

That was when I discovered the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) on python.org. If you have any doubts as to how your code should be laid out, reference this baby and you'll be on your way. 

What does it say about naming conventions? Quite a bit actually! For the pupose of this post there, here's what it says about Function names (also applicable to Methods and Instance Variables):


> Function names should be lowercase, with words separated by underscores as necessary to improve readability.

If you check out the page for yourself you'll see further explanations on other naming convention options within Py.


## Conclusion

Given the existence of the PEP8 standards, I don't think we really have a choice nor do I think there's any debate about how we should be naming variables and the like.

Going forward I'll definitely be using these rules when working on my code. If I don't, feel free to correct me!

Imagine a world where we all code to the same rules. Mmmm.

Keep Calm and Code in Python!

-- Julian

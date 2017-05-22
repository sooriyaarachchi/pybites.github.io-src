Title: Code Challenge 20 - Object Oriented Programming Fun
Date: 2017-05-22 15:10
Category: Challenges
Tags: codechallenges, OOP, object oriented, inheritance, encapsulation, polymorphism, dunder, games, ABCs
Slug: codechallenge20
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we will let you experiment with Object Oriented Programming, an important skill and fundamental building block of (everthing-is-an-object) Python. Enjoy!
cover: images/featured/pb-challenge.png

> There is nothing like a challenge to bring out the best in man. - Sean Connery

Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we will let you experiment with Object Oriented Programming, an important skill and fundamental building block of (everthing-is-an-object) Python. Enjoy!

##The Challenge

If you are new to OOP you might want to checkout [a primer tutorial](http://pybit.es/oop-primer.html) first.

Requirements:

* Define a class with a constructor (\_\_init\_\_ = object setup code, e.g. defining instance variables) and at least two methods. To relive PyCon you could have a generic Session class, but use any concept you like (Employee, Car, Person, Animal, Account, Notebook, etc). 

* Define a subclass that inherits from the parent class. For example you could let (Lightning)Talk, KeyNote and Workshop be subclasses (inherit from) Session. Other examples: Employee - Manager / Developer, Car - Toyota, Account - SavingsAccount ... you get the idea.

* Define another class for use in the initial (sub)class. So for the PyCon Session example you could pull in a bunch of Person (Developer) objects that joined it. This [Python OOP book]() has an example of a Notebook class to which Note objects are getting added. Or you have a Blog with Posts, Tags, Categories, Comments, that seems a straightforward one. The possibilities are endless. 

* Another option that could be a good fit for OOP is developing a simple game with different Characters (Monsters, Heros, Princesses) and Places they go, each class (blueprint) defining its own state (attributes) and behaviors (methods).

* We hope you follow along so far. For the more experienced coders among us, get bonus credits if you can:

	* apart from Inheritance implement Polymorphism and Encapsulation.

	* use one or more class and/or static methods. You could have a class variable keep track of the number of instances of the class for example.

	* investigate and use Abstract base classes (= ABCs, see also our [OOP primer]())

	* implement special (aka "dunder" aka "magic") methods which we covered [here](http://pybit.es/python-data-model.html), at least \_\_str\_\_ and \_\_repr\_\_ 

        To get an idea of the difference between these two and a list of dunder methods on a typical Python object run this:

            >>> from datetime import datetime as dt 
            >>> d = dt.now()
            >>> str(d) 
            '2017-05-22 12:16:08.816364'
            >>> repr(d) 
            'datetime.datetime(2017, 5, 22, 12, 16, 8, 816364)'
            >>> help(d) 

	* use multiple inheritance and play with \_\_mro\_\_ to figure out what the inheritance order is.

---

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking. 

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

## Feedback

If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

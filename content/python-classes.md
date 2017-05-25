Title: How to Write a Python Class
Date: 2017-05-25 20:37
Category: Learning
Tags: learning, code, programming, python, classes, beginners
Slug: python-classes
Authors: Julian
Summary: In this post I cover learning Python classes by walking through one of our 100 days of code submissions.
cover: images/featured/pb-article.png

Another week, another scary Python construct to tackle. Classes! I’m so glad we’re covering Object Oriented Programming in [this week’s code challenge](http://pybit.es/codechallenge20.html). Thanks to this challenge, I wrote my first class! In this post I explain what a Python class is (in my own words of course!) and break down my code to help  with the learning.

<br>
##What is a Python Class?

It’s hard to explain. Pretty much, a class is a way of “generically” representing some sort of object. (Confusing right?) Let me try with an example.

What’s something we’re all familiar with… Angry Birds! (At least, you should be if you’ve ever owned an iPhone!).

Let’s go with the Pigs. In Angry Birds there are a heap of different types of Pigs to kill. Some are large, some are small. Some have hats that give them extra health and some have helmets that make them almost indestructible. What’s one thing they all have in common? They’re all Pigs!

If you were to be writing the code for Angry Birds, you wouldn’t manually code up each Pig, you’d create a *Pig Class* that you could call every time you wanted to create a Pig. When you create the Pig Class, you would specify the *attributes* that a Pig could be created with, e.g., how much health the pig gets. 

I’m being simplistic but you get the idea. The base “Pigness” is there. A Pig will *always* have a set amount of health to begin with, you’re just specifying how much it gets when you create it.

I wrote a basic Person Class this week for our [100 Days of Code Challenge](http://pybit.es/special-100days.html). I’ll break it down for you to make this easier.


<br>
##A Person Class

The code for this example is [here](https://github.com/pybites/100DaysOfCode/tree/master/054).

A person is as simple as it gets. We’re all people but we differ immensely. We’re different ages, different heights, weights, sexes, colours and so on. At the end of the day, we’re still people - which makes us a great Class use case!

In the below code, I define a person class:

~~~~
class Person(object):
    def __init__(self, name, age, height, weight, gender, job):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.job = job
~~~~

- The first line is simple. We’re *defining* a class called “Person” and it’s an object.
- __init__ is a dunder method used to say that we’re *creating* the Person object (using the Person class definition).

> Note the difference between *defining* the class and *creating* the object based on the class.

- In the ()s we specify all of the attributes we want the Person object to be created with. Self is pretty self explanatory (pun intended!). It’s referring to itself. That is, the actual Person object that’s being created. (You’ll see in a sec).

- We then assign these attributes to variables because they’ll contain data once a person object is created. `self.name` for example, is then assigned “name” which will actually be a name at object creation.


<br>
##Creating A Person Object

At this point, we’ve defined a Person. A Person will have the attributes: `name`, `age`, `height`, `weight`, `gender`, `job`.

Now let’s create that person!

~~~~
bob = Person("Bob", 30, 180, 80, "Male", "Professional Awesome Programmer Guy")
~~~~

Just like passing variables to a function, we pass the attributes to the Person Class. What we’re doing here is we’re assigning all of these details (in the order specified in the class) to the `bob` object.

Yay! We just used the `Person` class to create `bob`! Creepy right?!

We can then do funky things like:

~~~~
bob.age
30
~~~~

This is where the `self` stuff starts to make sense. Look back at the class creation and substitute the word `self` with `bob`. Get it?


<br>
##Creating Class Functions

If we want, we can also create some functions specific to this class that we can call to do the same thing. Here’s another way of getting `bob`’s job (this is specified in the class):

~~~~
def get_job(self):
    return self.job
~~~~

We then call this as such:

~~~~
bob.get_job()
Professional Awesome Programmer Guy
~~~~

This is the same output as running `bob.job`.


<br>
##Getting Funky with Class Functions

What’s something interesting we could do? This is where I came up with the idea of calculating a person’s BMI (Body Mass Index).

~~~~
def bmi(self):
    return (self.weight / ((self.height / 100) ** 2))
~~~~

BMI is calculated using the equation in the above: weight (kgs) divided by height in metres squared.

Once a Person object has been created, we can then check what their BMI is as per the following:

~~~~
bob.bmi()
24.7
~~~~

Pretty cool right?

<br>
##When Would you use a Class?

I’d say you’d want to use them any time you’re dealing with repetitive data sets.

For example, if you were dealing with data from a movie database you could make a Movie Class because we know that each movie is going to have the same attributes: title, duration, year, director and so on.

You could use them for anything really.

Consider a complaints system at a company. A complaint would be structured the same way every time: ID, Customer Name, Affected Service, Date, Complaint Text.

The best part is that by creating your own class functions you can do all sorts of weird and wonderful things with the data. Imagine a `complaint.email()` function. It could email off the complaint to the correct department if it was deemed legitimate!


<br>
##Conclusion

Classes do take a little getting used to, especially when you start playing with subclasses (Code Challenge 20!) but they’re so great and totally necessary if you’re diving into Object Oriented Programming!

My recommendation is to open up an editor and code up a quick and dirty class right now:

Create a car class with attributes: Manufacturer, Model, Year of Manufacturing, Petrol Type, Mileage, Odometer. Then create some cars and play with their data! Print them to screen, add them to a database, whatever. Just get coding!

Keep Calm and Code in Python!

-- Julian


Title: How to Write a Python Sub Class
Date: 2017-06-17 19:37
Category: Learning
Tags: learning, code, programming, python, classes, beginners
Slug: python-subclasses
Authors: Julian
Summary: In this article I cover Python subclasses and inheritance using a relatable code example scenario.
cover: images/featured/pb-article.png

This is an article on Python Subclasses and inheritance. Before reading on, if you haven’t done so already, I strongly recommend you check out my write up on [Python Classes](https://pybit.es/python-classes.html).

Let’s get cracking!

<br>
##A Python Sub-what?

Let’s say you have a class already set up. In my [previous article on classes](https://pybit.es/python-classes.html), I created what I’m going to refer to as a “single tier” Person class. That is, you use the `Person` class to create a person object. That’s it. (I created Bob using this class. Muahaha!).

What if I wanted some more depth though? Let’s use vehicles as an example. I’ll get really simplistic here.

Vehicle > Car > Mercedes.

See that? Now we’re talking! Multiple levels! `Vehicle` would be the parent class, `Car` would be the **Subclass** and `Mercedes` would be an object we create using the `Car` subclass.

Not only that, but the Mercedes we just created will *inherit* all of the attributes and functions associated with the `Vehicle` parent class *and* those from the `Car` class.

That is, the Mercedes will be deemed a car vehicle in that it has four wheels and a windshield as opposed to a motorbike vehicle which only has two wheels and a tiny windshield. Both the car and the motorbike are vehicles but just two different *types* of vehicles. Get it?


<br>
##A Familiar Example

> Full code [here](https://github.com/pybites/blog_code/tree/master/boss_class_code).

To demonstrate this in code, I wrote up a `Boss` class. Let’s face it, we’ve all had a job at some point in our lives. It’s also more than likely that we’ve copped good and bad bosses and managers along the way.

Imagine if you would, a game with a Boss in it. I can imagine myself coding up a Boss class similar to the below. I’d then use this code to create different types of Bosses:

~~~~
class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face
~~~~

> A full explanation of a class written like this is found in my [Python Classes article](https://pybit.es/python-classes.html).

A boss would have a `name`, an `attitude`, a `behaviour` and a `face` (facial expression!).

<br>
Now, let’s start working on the Boss Subclasses. What kind of Bosses do we want to be able to make? How about a `GoodBoss` and a `BadBoss`?

~~~~
class GoodBoss(Boss):
    def __init__(self,
                name,
                attitude,
                behaviour,
                face):
        super().__init__(name, attitude, behaviour, face)
~~~~

What did I do here? It’s very similar to coding the parent class. Note the differences though:

1. We start by defining the subclass `GoodBoss`. See how it’s got “Boss” between the brackets? That’s because we’re defining a `GoodBoss`, `Boss` object. This will ensure the `GoodBoss` class inherits everything from the `Boss` class.

2. In the init dunder, we have to specify `self` as well as all of the attributes defined in the parent `Boss` class. We can then **add** whatever ‘GoodBoss’ unique attributes we want, such as a “laugh” attribute (good bosses laugh right?). In this case, I’m not adding any, thus the last attribute you see is `face`.

3. The `super()` statement is probably the most confusing. It relates to the inheritance from the base class. 

> I’d be doing you a disservice trying to explain super() in one bullet point so I’m going to direct you to where I read up on it. The 3rd answer in [this Stack Overflow thread](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods) is amazing as is this [Programiz article](https://www.programiz.com/python-programming/methods/built-in/super).

<br>

Phew! Okay. Next up, we can define some GoodBoss specific class functions. These can *only* be used by an object created using the `GoodBoss` class:

~~~~
def nurture_talent(self):
    #A good boss nurtures talent making employees happy!
    print("The employees feel all warm and fuzzy then put their talents to good use.")

def encourage(self):
    #A good boss encourages their employees!
    print("The team cheers, starts shouting awesome slogans then gets back to work.")
~~~~

What does a good boss do? He/She nurtures talent to help employees grow! They also encourage their teams to keep them motivated!

These two class functions simply print out the specified message when called. If this *were* a game, rather than just printing, we could have these functions perform transactions like “increase `employee_happiness` by 20 points, or something similar.

<br>
In the same way, we can define a `BadBoss` subclass. You can find the `BadBoss` subclass code in our code repo [here](https://github.com/pybites/blog_code/tree/master/boss_class_code).


<br>
##Who’s the Boss?!

Time for some fun! I’ll be the good boss, Bob can be the bad boss. (Sorry brother!).
The easiest way to test this out is to import the code into the interactive shell.

I’ve got a file called `boss_class.py`. I’m initiating the python shell from the same folder the script lives in.

~~~~
from boss_class import Boss, GoodBoss, BadBoss
~~~~

<br>
Once imported, we can create a “standard” `Boss`, a `GoodBoss` or a `BadBoss`. Let’s start with the good one!

~~~~
julian = GoodBoss("Julian", "Positive", "Sociable", "Smiling")
~~~~

<br>
We can then use the class functions associated with both the `Boss` class *and* `GoodBoss`  subclass:

~~~~
julian.attitude
‘Positive’

julian.get_behaviour()
‘Sociable’

julian.nurture_talent()
The employees feel all warm and fuzzy then put their talents to good use.
~~~~

I wish I really had that effect on people! Also, this is inheritance in action! We “inherited” the `get_behaviour` function from the `Boss` class! Woohoo!


##Ending on a low

I know we’re on a roll but Bad Bosses always have a way of ruining things:

~~~~
bob = BadBoss("Bob", “Crazy”, "Anti-Social", "Scowl of Hate")

bob.face
'Scowl of Hate'

bob.get_attitude()
‘Crazy’

bob.hoard_praise()
The employees feel cheated and start plotting Bob's demise while he stares at his own reflection.

bob.yell()
Everyone stares while Bob yells. Someone shouts, 'Won't somebody PLEASE think of the children?!’
Bob storms off, everyone comforts the victim and one person offers to arrange an 'accident' for Bob.
~~~~

> Disclaimer: I love Bob (we all know he’s the best thing since sliced bread!). I also love my AWS overlords.


##Conclusion

How cool are classes, subclasses and inheritance?!

Not only has this helped me better plan my code but it’s also allowed me to better appreciate other code. I can only imagine how many classes and subclasses exist in video games (World of Warcraft for example!).

Once you get the hang of them, classes really are quite easy to use. They’re a series of set and forget templates/blueprints for you to call at any time. Oh the possibilities… Yum!

Oh and speaking of templates. I created a framework/blank class and subclass template for Day 77 of our 100 days of code challenge. Check it out [here](https://github.com/pybites/100DaysOfCode/tree/master/077)!

Keep Calm and Code in Python!

-- Julian

(Psst! Did anyone get the [Simpsons Reference](https://www.youtube.com/watch?v=RybNI0KB1bg)?)
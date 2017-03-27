Title: Pythonic String Formatting
Date: 2017-03-02 08:00
Category: Learning
Tags: python, learning, beginners, tips, cleancode, bestpractices, pythonic
Slug: string-formatting
Authors: Julian
Summary: The formatting of strings has been a hot topic in Python and something that I struggled with at the beginning. It's quite interesting to see how it's evolved over time to be what it is today!
cover: images/featured/pb-article.png


Formatting strings was one of the things that really hurt my head when I started learning Python. Everyone did it differently!

After doing Michael Kennedy's [*Write Pythonic Code Like a Seasoned Developer*](http://pybit.es/pythonic-code-course-rewiew.html) course, I was inspired to write about the different ways you could format a string in Python. Mainly because the method we've all deemed **wrong** (or at least, "least Pythonic") is the way I started off doing it!

##The Terribly Unpythonic Method

Okay let's get this out of the way first. Here's how I formatted a string when I first started:

~~~~
>>> country = "Australia"
>>> level = 11
>>>
>>> print("The awesomeness level of " + country + " is " + str(level) + ".")
The awesomeness level of Australia is 11.
~~~~

I'll be honest, I was just glad I could get text to print! It's pretty terrible isn't it? Having to display *level* as a string with *str()* sends shivers down my spine now.


##Using the String Format Operator

When Bob first showed me code that contained the string format operator I could have died. Not because it was awesome but because as a newbie, I had no idea what the heck I was even reading! Using the same variables and types:

~~~~
>>> print("The awesomeness level of %s is %d." % (country, level))
The awesomeness level of Australia is 11.
~~~~

What the heck are % signs doing within a string? And how are they being substituted and not being displayed as is?

It's pretty simple! What the code is doing is substituting the %s and %d for the values specified in the brackets after the string.

That is, %s is substituted with *country* and %d with *level*.

It was great until I realised that the %s was only to be used to specify a string type variable and %d to specify a decimal. (There are more options to choose from of course!).

The reason this is a pain is that you'll need to remember the type of every variable you're going to print and get the order right in your print statement. Not a huge fan.


##Replacement Fields

This is my favourite one. Replacement fields!

Replacement fields expand on the format operator by taking the thinking out of the equation (always a good thing for me!):

~~~~
>>> print("The awesomeness level of {} is {}.".format(country, level))
The awesomeness level of Australia is 11.
~~~~

Similar to the format operator, we put the replacement fields *{}* where we'd like the variable output to be in the string. The difference? We no longer need to remember what the **type** of the variable is! 

It's all taken care of by *.format()* which will display your variable using the appropriate format. So very cool and painless!

Pythonic goodness!


##Python 3.6 f-strings

f-strings were introduced [in Python 3.6](http://pybit.es/3.6_new.html) and are pretty new to me but that doesn't stop them from being awesome! Check this out:

~~~~
>>> f"The awesomeness level of {country} is {level}."
'The awesomeness level of Australia is 11.'
~~~~

How incredible is that? The variables are called in the string output directly within the replacement fields. You no longer need to manually call format()!

Even more Pythonic goodness!


##Conclusion

Being quite new to Python means I'm more likely to use the latest and greatest method of formatting strings which actually makes things more difficult. I now want to go back through my old code and update it with the newer, more Pythonic methods.

![Pythonic string formatting summarized]({filename}/images/pythonic-string-formatting.png)

---

I want to hear more about how other programmers format their output strings. It's a topic that's interested me purely because of the strong opinion out there!

How do you do it?

Keep Calm and Code in Python!

-- Julian

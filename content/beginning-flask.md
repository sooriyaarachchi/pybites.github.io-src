Title: Beginning Flask
Date: 2017-04-13 15:00
Category: Flask
Tags: Flask, python, decorators, tutorial, learning
Slug: beginning-flask
Authors: Julian
Summary: In this post I cover the basics of Flask in language that anyone can understand.
cover: images/featured/pb-article.png

Last week I wrote an [article](http://pybit.es/flask-for-loop.html) showing you how to print the contents of a dict to a table using Flask and HTML.

In the lead up to the post I did quite a lot of browsing, reading and researching to wrap my head around this whole Flask thing. It took me a little longer because not everything out there was in simple, human readable English. A lot of sources assume a high level of Python knowledge and not everything was explained simplistically (lots of big words!).

That’s why I decided to write this article explaining the absolute basics (Hello World!) in a manner I would have liked to seen.


##What is Flask?

Odds are if you’re reading this, you already know what Flask is. I’m going to explain anyway.

Flask is a “web framework” you can use to get your Python code to appear in a web browser (I told you I’d make this simplistic!).

As with most programming languages, when you begin learning Python you’ll be making scripts that are completely command line based. Eventually you’ll wonder how the pros use Python to make web applications. Flask is one way to do this.

There’ll be a Python script that imports the Flask module and when run, *generally* passes data to a HTML file. When the web page is loaded, it runs the Python code associated with that web page.


##What should you know before learning Flask?

I won’t sugar coat it. You’ll have a hard time if you don’t have a sound understanding of HTML and CSS.

Python wise, your app will only be as complex as the code you write so the more you want to do, the more you need to know.

The HTML knowledge needs to be there though. For example, HTML forms can be tricky just on their own. When you add Python and Flask to the mix it can get downright confusing (seriously, me).

You don’t have to know CSS as much I guess but everyone wants their page/app to look good right? Maybe I’m just a little shallow!


##Explaining Hello World

Okay so here’s a simple Hello World Flask script you’ll probably find in every Flask tutorial:

~~~~
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world! Can I get some CSS please?!’

app.run()
~~~~

Alright, what the heck is going on here? Let me break it down

~~~~
from flask import Flask
~~~~

* Simple, we’re importing the **Flask** class from the *flask* module. This is the standard import call for the Flask module. Roll with it!

~~~~
app = Flask(__name__)
~~~~

* Let’s talk about the assignment. All we’re doing here is assigning the Flask class to a variable called app. Simple.

* (__name__) is the bloody confusing part. The Flask class needs to know what value is currently assigned to __name__. Whenever __name__ is used in your code, it’s assigned the name of the module that’s currently active. The Flask class needs this information to be able to execute properly.

~~~~
@app.route('/')
~~~~

* Think of this as the URL of the web page you’re coding. You’ll often hear people say “route” for short when talking Flask. If you wanted to create a page called *birthdays.html*, you’d name the route *@app.route(‘/birthdays’)*.

~~~~
def hello():
~~~~

* Note that there’s no line space between the route and this function. That’s because they’re directly linked.

* All of the code that you add within this function will be executed when the web page is loaded.

* The recommended function naming convention is to give it the same name as the route. This Hello World example is thus against convention. Using the birthdays example, we’d create a function with: *def birthdays():*.

~~~~
return 'Hello world! Can I get some CSS please?!’
~~~~

* This is an important one. **Every Flask function needs to return something**. This is the data that will be returned to the web page.

* This return line will simply print the string *Hello world! Can I get some CSS please?!* to the page.

* In a more complex piece of code, you’d more likely be returning a variable or something similar.

~~~~
app.run()
~~~~

* Pretty self explanatory. This is the code that will run your Flask app.


##Things to Note

* When you run your Python Flask script (same way you’d run any other Python script), Flask kicks off a local web server. It runs on the system you’re executing the code from and, by default, will allow you to browse to the page at 127.0.0.1:5000. You’ll then add the web page URL to the end of the port number, e.g.: 127.0.0.1:5000/birthdays

* When you start executing more complex code, such as my [dict example](http://pybit.es/flask-for-loop.html) from last week, you need to use Flask Templates. These use the “Jinja2” engine (again, roll with it). This is all installed by default when you pip install flask.

* A Flask Template is pretty much just a HTML page that your code talks to. You can make one generic such that every page on your site calls the generic page so the theme is maintained across pages. Alternatively you can code each page individually.

* Being familiar with HTML comes in handy when you start using Templates. Your python, HTML and CSS files need to be stored according to a required Flask folder hierarchy. Check out the [GitHub repo for my code](https://github.com/pybites/blog_code/tree/master/flask_for_loop) last week and you’ll see what I mean. It feels *way* more familiar and less daunting if you’ve organised the files for a website before.


##Why use Flask?

I asked myself this question a few times. Honestly, I’d say use it because it’s so simple and quick to get running. Bob and I were chatting this week about the Flask Template I made to create the HTML table and with little to no effort, he was able to take the template and use it for his new [weather compare app](http://weathercompare.herokuapp.com/) (code [here](https://github.com/pybites/100DaysOfCode/tree/master/013)).

My current hurdle is not Flask itself but trying to tie it in with the HTML side of things. It’s been years since I did any deep HTML coding so I’m pretty rusty. At the time of writing, I’m finding that the Python code is functional but I can’t get the HTML to wrap around it the way I want.


##Examples and Resources

Check out some of these examples and resources. Reading and running other code will help get this stuff to sink in.

* [Display a dict using Flask](http://pybit.es/flask-for-loop.html) - I’m pushing my post again because it really is easy to follow. Check the [repo](https://github.com/pybites/blog_code/tree/master/flask_for_loop) out and try it for yourself. Edit the code and watch the table change. Learn by doing!

* [Bob’s Weather Compare App](https://github.com/pybites/100DaysOfCode/tree/master/013) - Bob made this as part of our [100 days of code challenge](http://pybit.es/special-100days.html). It’s definitely more complex but it’s amazing to see how *little* code you need to actually get something like this out.

* [Flask Web Development with Python Tutorial](https://www.youtube.com/watch?v=ZVGwqnjOKjk&list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs) - This 7-part video series from The New Boston is amazing. Nice and simple. Short bites. PyBites styles!


##Conclusion

Don’t be deterred by the learning curve. If you’re new to this, start simple and stick with it. Just a little bite every day. Start with printing static data then slowly move on to more complex ideas like printing variables and dicts. Just remember, Always Be Coding!

And remember, Keep Calm and Code in Python Flask! (And HTML and CSS I guess!)

— Julian

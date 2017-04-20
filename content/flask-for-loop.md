Title: Flask for Loops - Printing Dict Data
Date: 2017-04-06 20:38
Category: Flask
Tags: Flask, loops, python, decorators, tutorial, learning
Slug: flask-for-loop
Authors: Julian
Summary: In this post I demo how to create an extremely simple Flask app that prints the contents of a Dict to a web page.
cover: images/featured/pb-article.png

Thanks to the [100 Days of Code Challenge](http://pybit.es/special-100days.html), this week I took the plunge and dove into Python Flask.

It’s not the easiest beast to tame but once you wrap your head around it, it’s not so bad!

One of the concepts I struggled with early on was how to return more than “just” a single string to the Flask app web page.


##Python Setup

Check out the full code for this [here](https://github.com/pybites/blog_code/tree/master/flask_for_loop).

* I decided I wanted to print out a dict of birthdays. You can see I’ve created a route to a page called ‘birthdays’. The function associated with this decorator contains the dict we want to display.

~~~~
@app.route("/birthdays")
def birthdays():
	dates = {"Julian": 25, "Bob": 26, "Dan": 47, "Cornelius": 3}
	return render_template("birthdays.html", dates=dates)
~~~~

* Being Flask, we need to have a templates folder in the same directory that the main.py script is being run from.

* In the templates folder we’ll need to have a birthdays.html file for the above route to work with.



##HTML Setup

With the main.py file all set up, we can focus on birthdays.html. (Again, all of this is in the [code Repo](https://github.com/pybites/blog_code/tree/master/flask_for_loop)!).

* The simplest and most pleasing way to display this data would be in a table. 

* The stylesheet (style.css) we’ll be using lives in another folder called ‘static’. This folder lives at the same hierarchical level as the templates folder - go ahead and create it.

* As an example, in style.css we have a CSS class just to give the table a slightly thicker border.

~~~~
.thick-border {
        border: 3px solid black;
        border-collapse: collapse;
}
~~~~

* We can then create the table. The first row will be the table headers.

~~~~
<table class="centered thick-border">
        <tr>
                <th>First name</th>
                <th>Age</th>
        </tr>
</table>
~~~~




##Flask in Action

* With the table set up we can now start populating it with the contents of the *dates* dict from main.py.

* When inserting Python code into the HTML file, we wrap it in {% %} so Flask knows to differentiate it from normal HTML code.

* To print out the contents of the dict, we can use a for loop. The idea of the for loop stays the same, it’s just spread out across multiple lines and wrapped in HTML. First we start with the opening of the for loop.

~~~~
{% for k, v in dates.items() %}
~~~~

* We don’t need to explicitly call *print* to read out the values of *k* and *v*. We just need to choose how they’ll be displayed on the page in HTML.

~~~~
<tr>
	<td>{{ k }}</td>
	<td>{{ v }}</td>
</tr>
~~~~

* You’ll notice the {{ }} around the variables. This is another flag to Flask that these are Python variables and not a bit of HTML code.

* We then have to close off the for loop with one last bit of special Flask code.

~~~~
{% endfor %}
~~~~


##Final Result

* This is what the code for the table should look like.

~~~~
<table class="centered thick-border">
        <tr>
                <th>First name</th>
                <th>Age</th>
        </tr>
        {% for k, v in dates.items() %}
                <tr>
                        <td>{{ k }}</td>
                        <td>{{ v }}</td>
                </tr>
        {% endfor %}
</table>
~~~~

* Here’s what the web page will look like.

![Table populated by Python dict code]({filename}/images/flask-bday-table.png)

* The beauty is that you can add as much data (keys, values) to the dict as you want and the table will always be drawn to match the content. Give it a try!


##Learning Points

* Flask requires that the decorator function you’re using **returns** something. It could be something as simple as: *return ‘This is a string’*. The point is, data needs to be returned. I struggled to understand how I could return each for loop pass over the dict! After continued research and reading, I learned about the HTML templates and how you write put the Python code there instead.

* Unsurprisingly, making something that’s pleasing to the eye requires some knowledge or experience with HTML and CSS. I was pretty dusty!

* In the full example you’ll see how it all meshes together - the static and templates folder and the main.py file living above them. Having experience with web dev makes this environment a lot easier to understand.

* It’s tough but extremely rewarding to move on from static return lines of just “hello world” to displaying data. That is, moving forward, the data printed by the loop could be generated on the fly. That’s exciting!


##Next Steps

* Next up I’d like to make this interactive. Perhaps have the user enter birthdays via a web form themselves and once completed, have the birthdays print to screen in a table.

* The data really should be stored in a database or shelf too, not in a static dict.

* Get my CSS game on and make this baby pretty!


You’ll be seeing more Flask in the coming weeks (I hope!). I’d actually like to wrap this for loop around the data set for [this week’s code challenge](http://pybit.es/codechallenge13.html)… hmm…

Keep Calm and Code in Python!

— Julian

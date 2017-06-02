Title: Flask Sessions
Date: 2017-06-02 21:57
Category: Flask
Tags: Flask, python, beginner, sessions, learning, examples, code
Slug: flask-sessions
Authors: Julian
Summary: In this quick post I discuss Flask Sessions and provide a few use cases.
cover: images/featured/pb-article.png

More Flask?! Yes! More Flask! I apologise for nothing! This is however a quick article for anyone wanting to learn about Flask Session Objects.

One of my most exciting discoveries as of late has been the `session` object. I stumbled upon this useful little thing while making my [Pay Calculator App](https://github.com/pybites/100DaysOfCode/tree/master/060) for our [100 Days of Code Challenge](http://pybit.es/special-100days.html).

Let’s discuss sessions in the usual Julian format.

<br>
##What is a Flask Session Object?

Think of a Flask Session Object as a special variable that persists for the life of the browser session that’s connected to the Flask app.


<br>
##Say What?!

Well, here:

I wanted to make a pay calculator web application that allowed me to calculate how much money I’d be paid based on me entering my hourly wage and how many hours I worked. Simple right?

Well, what if, as part of this app, I want to have another web page that could extrapolate my entire annual salary from just the hourly wage? I don’t want these two functions to exist on the same page.

I also don’t want to ask the user to enter in their salary every time they flick between these two pages/apps, that’d be annoying right? I’d need a variable that could store the hourly wage and keep that data accessible to any of the web apps running from this Flask app.

This is where you’d use a `session` object. You’d assign the user’s hourly wage to the `session` object which you would then make available to use across different web pages in your app.


<br>
##Code Me Up!

The thing that surprised me was how simple it was. Coding wise, you use the object in exactly the same way you’d use a normal variable. It still has to abide by normal global/local rules in your code too.

To assign the hourly wage to a `session` object I did this:

~~~~
session['wage'] = float(request.form.get('wage'))
~~~~

The code on the right is just pulling in the data from the HTML form with the name “wage”. It stores that as a float into a `session` object of the same name (wage).

It’s seriously as simple as that.


<br>
##Super Secret Keys

I know all of this sounds a lot like cookies. It should. Flask `session` objects exist on top of standard cookies. All that’s different is that the cookie is locked down with a secret key.

This does not mean the data is private! The cookie data is visible but **cannot be modified unless you have the secret key**.

This secret key needs to be accessible to your app code. You’d preferably make it an environment variable that isn’t accessible to the outside world. I made mine as complex as possible:

~~~~
app.secret_key = "Test_Secret_Key"
~~~~

`Test_Secret_Key` being the password. Good luck cracking this bad boy!


<br>
##The Pay Calc App Use Case

In my Pay Calculator App, I create the `wage` session object in my index ‘/‘ route:

~~~~
@app.route('/', methods=['GET', 'POST'])
def index():	
    if request.method == 'POST' and 'wage' in request.form:
        session['wage'] = float(request.form.get('wage'))
        return redirect(url_for('pay_calc'))
    return render_template("index.html")
~~~~

What you’ll notice is that `wage` is created and then returned in the `redirect` to the page associated with the `pay_calc` function.

This essentially makes it available to the second page of the app.

I then check for it in the code for the second page:

~~~~
@app.route('/pay', methods=['GET', 'POST'])
def pay_calc():
    pay = ''
    if request.method == 'POST' and 'hours' in request.form and 'wage' in session:
        hours = float(request.form.get('hours'))
        pay = calc_wage(session['wage'], hours)
    return render_template("pay_calc.html",
                            pay=pay)
~~~~

The `if` statement checks to see if the `wage` session object exists. If it doesn’t, the calculation within the `if` won’t take place.


<br>
##Other Use Cases

- You could use this for a personal touch on your site. A user enters their name which allows you to refer to them by their name on relevant screens.

- A to-do list! The entire list is in the `session` object which can be called and loaded on any page the user loads on your site. It’d be a good idea to have data persistence as well in this scenario though!

- Dare I say it? Ordering food online is a great use case for this. Add all selected items to a `session` object to keep track of the user order while they browse. Once the order is complete, the data can be scrapped when the browser session closes.

- Any sort of online calculation service: currency exchange, electricity, insurance, superannuation. These all require temporary data.

- Flight tracking information (I may be stretching it here). A user would enter details of a flight to track and that data would stay live for the duration of the session. There’s no need for it to be stored.

- Even an old school type of browser game like Jetman. The score is retained for the duration of the session but once the browser closes, you start from scratch.


<br>
##Conclusion

I think you get the point! The `session` object is incredibly useful!

I’ll admit, it did take some time to wrap my head around how to get it working at a code level. The concept is simple but writing the code such that it worked took some testing and playing.

If you have any cool use cases or examples of `session` object usage, let us know!

And as always, Keep Calm and Code in Python!

-- Julian

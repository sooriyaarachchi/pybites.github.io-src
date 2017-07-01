Title: Flask Ports
Date: 2017-07-01 20:31
Category: Flask
Tags: Flask, python, beginner, learning, ports, apps
Slug: flask-ports
Authors: Julian
Summary: A quick post on Flask App port mapping
cover: images/featured/pb-article.png

If like me you’re obsessed with Python Flask, you might have asked yourself, “How on Earth do I run multiple Flask apps at the same time?!”.

It’s actually pretty simple!

<br>
##What Happens at Default Settings

Before I get to the solution, I’ll first show you what happens if you leave everything at the default settings as it’s important to know.

For this test I’m running my [Pay Calculator App](https://github.com/pybites/100DaysOfCode/tree/master/060) and my [Timezone List App](https://github.com/pybites/100DaysOfCode/tree/master/083) together.

The app you launch *first* will always take priority. In this case, my Pay Calculator interface shows up on 127.0.0.1:5000. The interesting thing is that when I run the Timezone App, there’s no error. Python still launches a web server on 127.0.0.1:5000.

The catch is that all calls from my browser to localhost (127.0.0.1) are routed to the web server created by the Pay Calc app. If I try and browse to a web page that is *unique* to the Timezone App, I get a 404 error. The page doesn’t exist in the Pay Calc app and therefore the call fails.

As expected, the second I CTRL+C my Pay Calc app, everything springs to life for the Timezone app. Browsing to localhost brings up the Timezone interface and browsing to the aforementioned unique page works.


<br>
##Specify a Port!

The solution? Specify a port number!

In Flask code, it’s the `app.run()` code that kicks everything off. Without that code, there’s no app.

By default, this starts the web server on 127.0.0.1:5000. We can change this!

~~~~
if __name__ == "__main__":
    app.run(port=5001)
~~~~

Believe it or not, it’s as simple as that!

Throw the port number you want to access the web app from to `app.run()` and the web server launches on that port. So simple and easy!


<br>
##Conclusion and Discussion

This is as simple as it gets. There is however something else to discuss.

If you’re trying to run two or more concurrent web apps, it’s likely that you want these apps running in a sort of “production” environment. That is, you want them running all the time, it’s no longer just for a test.

That’s exactly my case. I want a few Flask apps running from my NAS on my local network at home.

The web server bundled in Flask is a development server. It may be fine for my home network but best practice mandates I use a dedicated web server like [nginx](http://nginx.org/en/).

Or another question, should I even use Flask for making production apps? Once I get to this level of production should I be moving to Django?

I’m actually not too sure! I’m definitely keen to hear everyone’s opinion on this. What do you use (if at all) for this sort of thing?

Do you use Flask for small apps and testing and Django for the bigger and badder stuff?

And as always, Keep Calm and Code in Python!

-- Julian

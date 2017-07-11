Title: 200 Days of PyBites, 100 Days of Code and our Next Project
Date: 2017-07-07 13:23
Category: Special
Tags: pybites, 100DaysOfCode, learning, modules, special, milestone, lessons, community, automation, utilities, scripts
Slug: special-100days-of-code
Authors: PyBites
Summary: [We did it!](https://twitter.com/pybites/status/883219041912987648) #100DaysOfCode is done: 5K lines of code, 100 scripts. Just on the day PyBites turns 200 days. In this article we will share our learning on this major project and announce our next 100 days effort ...
cover: images/featured/pb-special.png

> We highly recommend doing 100 Days no matter your level. Being aspiring or experienced programmers, you need deliberate practice. A lot of it. We can now assure you that 100Days makes you practice. And with the public commitment it's also a way to enhance your portfolio. - PyBites

[We did it!](https://twitter.com/pybites/status/883219041912987648) #100DaysOfCode is done: 5K lines of code, 100 scripts. Just on the day PyBites turns 200 days. In this article we will share our learning on this major project and announce our next 100 days effort ...

## The Challenge

[Last 100 days celebration](https://pybit.es/special-100days.html) we rewarded ourselves with a challenge: do the [100 Days of Code Challenge](https://medium.freecodecamp.org/join-the-100daysofcode-556ddb4579e4). Today is *Day 100* and we confirm: *mission accomplished*. With busy schedules it was not always easy, but we delivered. More on this in the Retrospective towards the end. First let us break it down ...

## Stats

Here is our [100DaysOfCode repo](https://github.com/pybites/100DaysOfCode).

[We wrote roughly 5K lines of code](https://github.com/pybites/100DaysOfCode/tree/master/100), divided into 100 scripts, one each day:

![distribution of LOC per script]({filename}/images/100d_histogram.png)

We [auto-tweeted](https://github.com/pybites/100DaysOfCode/tree/master/007) our progress each day which was tracked in our [log file](https://github.com/pybites/100DaysOfCode/blob/master/LOG.md).

Our [most popular tweets](https://github.com/pybites/100DaysOfCode/tree/master/096) were: 

![most popular tweets]({filename}/images/100d_most_popular.png)

## Module Index

We ended up using exactly 100 modules as well (weird coincidence LOL):

	pypi      :  42 (42.0%)
	stdlib    :  38 (38.0%)
	own       :  20 (20.0%)
	------------------------------
	Total: 100

You can see the full index [of used modules](https://github.com/pybites/100DaysOfCode/blob/master/021/index.txt). Here you can pick your module and go directly to the days where we used it. 

Find something useful? You can thank us by starring the repo. 

See any issue or things we can improve? Fork the repo and make a Pull Request. 

_Do notice_ that some scripts are in a pretty basic state. Time was not always on our side. We need a round 2 to do some cleanup. Bear	 with us ...

## Showcase of 10 Utilities 

Here are some scripts we specially liked:

### 1. [Day 086](https://github.com/pybites/100DaysOfCode/tree/master/086) - Twitter Archive Stats

Script to pull some quick stats from a #Twitter Archive CSV

> (log) Using Counter and csv.Dictreader. Simple exercise, yet useful data. You can run it yourself downloading your Twitter Archive in Settings

![Twitter archive stats]({filename}/images/100d_twitter-archive.png)

(refactored into a package later - see [Day 093](https://github.com/pybites/100DaysOfCode/tree/master/093))

### 2. [Day 014](https://github.com/pybites/100DaysOfCode/tree/master/014) - Lynda.com new Python course auto-tweeter

Script to automatically tweet out new @lynda (#Python) titles

> (log) Feedparser is awesome. Want to run it with filter on Python. Abstracted twitter config away in repo's common dir (re-use).

We were *surprised* to find *us* tweeting out this one yesterday ;)

![lynda notifications]({filename}/images/100d_lynda.png)

### 3. [Day 059](https://github.com/pybites/100DaysOfCode/tree/master/059) - Send an SMS with Twilio

Using the #Twilio #API to send SMS messages

> (log) Prework for another app where I want to use Twilio to send reminder notification and text friends :)

![twilio API]({filename}/images/100d_twilio.png)

### 4. [Day 013](https://github.com/pybites/100DaysOfCode/tree/master/013) - Weather app

A simple #Flask app to compare weather of 2 cities (using OpenWeatherMap #API)

> (log) This was a nice follow-up of 012, making it more generic (support any city), using Jinja templating, Flask form handling, and of course a good chunk of timezone handling (for sunset and sunrise)

![weather compare app]({filename}/images/weather-app.png)

This led to [this article](https://pybit.es/flask-simple-weather-app.html).

### 5. [Day 099](https://github.com/pybites/100DaysOfCode/tree/master/099) - Flask photo gallery

Simple #Flask app to display photos in a directory

> (log) This is a very basic app to demonstrate displaying images using Flask and Jinja templates. All photos need to be stored in the "static" dir within the Flask folder structure. The glob module is used to parse the photo dir. The app can and will be expanded and refactored.

![flask gallery]({filename}/images/100d_photo_gallery.png)

### 6. [Day 003](https://github.com/pybites/100DaysOfCode/tree/master/003) - Gif image creator

Script to generate a gif from various png/jpg images

> (log) Useful for blog, awesome: pip install imageio, cli arg interface is more code :)

![example gif made with script]({filename}/images/slackbot.gif)

### 7. [Day 033](https://github.com/pybites/100DaysOfCode/tree/master/033) - Water reminder app

I need to drink more water at work so I wrote a #Python #script to remind (spam) me every hour

> (log) A simple script using MIME and a cron job (read the readme.txt) to remind me to drink more water at work! Doesn't email on the weekends or before/after hours. Over the top? Maybe. Satisfying? Hell yes.

![water drinking app]({filename}/images/100d_waterdrinking-app.png)

### 8. [Day 022](https://github.com/pybites/100DaysOfCode/tree/master/022) - Amazon affiliation link generator

Create and paste #Amazon affiliation link to clipboard #pyperclip @AlSweigart

> (log) A nice little utility to copy an take Amazon link from clipboard, convert it into an affiliation link and paste it back to clipboard

![amazon affiliation link generator]({filename}/images/100d_affiliation_link_creator.png)

### 9. [Day 074](https://github.com/pybites/100DaysOfCode/tree/master/074) - Making a ecard with Pillow

Using Pillow to add text and opacity to an image = your own cards

> (log) Played with the Pillow module. Script to let user enter an image path (or url) and text to put on the image. Pillow does the rest. Could be a useful recipe to make your own Birthday cards :)

![putting text on image with PIL]({filename}/images/100d_pillow.png)

### 10. [Day 080](https://github.com/pybites/100DaysOfCode/tree/master/080) - "Is this Bob or Julian?"

"Is this Bob or Julian?" - script to reveal who of @pybites tweets

> (log) Fun little exercise that started with Anthony Shaw asking who he was talking to - it actually became more involved turning/testing out location on our tweets and adding exception handling ... nice practice! (and a funny new service for our PyBites community)

![who tweets script]({filename}/images/100d_twotweeted.png)

### Bonus [Day 009](https://github.com/pybites/100DaysOfCode/tree/master/009) - as we initiated this post ... 

Interactive script to create a new Pelican blog article

> (log) A lot of known concepts, but nice to bring a lot of functionality together, and above all a really useful script for our blog

As we started this post: HAPPY BIRTHDAY!

![easter egg]({filename}/images/100d_newpost.png)

## Retrospective

As you can see, not only did we get a lot of code written but we had a hell of a lot of fun doing it!

That’s the only way we got to 100 days with our sanity intact. It wasn’t easy in the least: Family, Kids, new jobs, and the usual PyBites responsibilities didn’t leave us with a heap of time but we managed to push and get there in the end. Again, the fun factor is what made it achievable.

Looking back on the 100 days, it’s quite shocking to see how much we accomplished and learned. Julian developed an almost obsessive love affair with Flask (not a hip flask) and Bob created some truly outstanding, fully functional applications.

The challenge also gave us the opportunity to scratch our own itches. Julian was able to create a [Steam Games notification service](https://github.com/pybites/100DaysOfCode/tree/master/045) for himself and Bob [assigned himself reading goals using Twilio](https://github.com/pybites/100DaysOfCode/tree/master/061).

While it was insanely tough, the payoff has been huge! We’ve honed our skills, created tools, learned new modules and even developed relationships with other coders - all from participating in the challenge.

We encourage anyone with a love of programming to take the 100 days of code challenge. Dedicating ourselves to a working script every day was a bit on the crazy side though and is by no means a requirement for the challenge. Just remember, **anything** is better than nothing so give it a crack!


## next(PyBites.projects) ?!

Yes, the rumors are true: our next 100 days project will be around learning Django. 

We will work incrementally on 2 or 3 projects which we will announce as we go. We will also tailor some articles and code challenges around this effort, so you can learn with us. 

This will be a lot of fun and with this major project under our belt, we're sure that we will learn a thing or two about Django which we hope you can benefit from too. 

Stay tuned ...

---

Keep Calm and Code in Python!

-- PyBites

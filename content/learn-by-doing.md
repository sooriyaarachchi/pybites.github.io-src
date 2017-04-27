Title: Learn Python by Coding for Yourself
Date: 2017-04-27 23:30
Category: Learning
Tags: learning, code, programming, python, resources, Flask, Warcraft, requests, gmail, APIs, sqlite3, challenge, motivation
Slug: learn-by-doing
Authors: Julian
Summary: In this post I discuss (with examples) why it’s important to learn Python by actually coding. It’s not enough to just read!
cover: images/featured/pb-article.png

We all know that the best way to learn *anything* is to just jump in and do it. You don’t learn to play the guitar by simply watching [YouTube videos](https://www.youtube.com/watch?v=tQ0iww5u6_I), you learn by playing every day, trying new songs and challenging yourself.

The same applies to learning Python.


##Sharing is Caring

In typical PyBites fashion, I’m going to share my experiences from the past two weeks regarding this “Learn by Doing” concept.

This is also a crucial part of learning Python - sharing. Don’t be afraid to put yourself out there and share your code.

- Put it on GitHub for the world to see.
- Share it on the [Reddit Learn Python page](reddit.com/r/learnpython) for it to be critiqued.
- Take part in [code challenges](http://pybit.es/pages/challenges.html) (shameless plug!) and actually submit your code for review.
- Send the code to friends with more coding experience for some feedback.

Whatever the case, sharing your code with others is one of the best ways to learn and *retain* the knowledge.


##Challenge Yourself

This week our [code challenge](http://pybit.es/codechallenge16.html) is based on APIs. Why? Because I didn’t know jack about them. When Bob and I brainstorm ideas for the code challenges, we generally settle on a topic that we’re not entirely comfortable with ourselves.

While Bob can query APIs in his sleep, just the thought of working with APIs made me collapse and start foaming at the mouth. Again, that’s why it was chosen.

It’s important to challenge yourself. If you just stick with what you know and stay within your comfort zone, not only will you never improve but you’re never going to have a *reason* to.


##The Results

On the surface, my foray into the world of APIs was disastrous. Seriously. Dive a little deeper though and it’s honestly been one of the greatest Python learning experiences I’ve had.

Being a World of Warcraft nerd, naturally the first API I looked into was the [Blizzard Warcraft API](https://dev.battle.net/). Needless to say, I had no idea what the heck I was doing. The documentation assumed a level of familiarity with APIs and clearly that wasn’t me.

After hours of playing around, I was able to get the basics down and pull some meaningful (to me!) data from my player profile. The saddest part is that after all of that effort, the most “crucial” line of code for the API call was this:

~~~~
url = ('https://us.api.battle.net/wow/character/%s/%s?fields=mounts&locale=en_US&apikey=%s' % (realm, char_name, API_KEY))
~~~~

It was like a kick in the teeth seeing such a pitiful line of code sitting there after such long period of time. ([Full code here](https://github.com/pybites/100DaysOfCode/tree/master/027)).

Why was it such a great experience? Well…

- Being thrown in the deep end can be super beneficial. Assumptive documentation and almost zero meaningful content online meant I had to figure it out through trial and error.
- I was forced to read code that called *other* APIs in order to see how it was done, then apply that to this scenario.
- I learned that you can use the `requests` module to pull data from the API using a specific HTTP URL. This was using the `get` attribute of `requests`.
- I learned a little about `OAuth`!
- This all resulted in me playing around with JSON content for the first time ever.
- I discovered that you can make JSON print out in a readable format using `pprint`.
- This forced me to then start looking into how one parses JSON data effectively, especially when you have multiple layers of dicts stored in the one JSON dict.
- I did this completely for me. This wasn’t out of a book or something someone told me to do. *I* wanted to play with this specific API because *I’m* a big Blizzard fan. This meant that I was engaged and **determined** to learn it even though it was bloody frustrating.

While my code is nowhere near a success and most definitely unPythonic, it’s one heck of an achievement for me. I actually understand this stuff now!


##The GMAIL API Experience

The next day I decided to hit up the [Gmail API](https://developers.google.com/apis-explorer/#p/gmail/v1/) because of the whole [Unroll.me fuss](https://www.gizmodo.com.au/2017/04/how-did-unrollme-get-users-to-allow-it-to-sell-their-inbox-data/) going on at the moment. I figured if they could do it, so could I!

I was wrong. But at least I learned something!

- I learned how Google uses OAuth to authenticate applications with your Google account.
- I was able to pull down a list of my Gmail labels, messages and filters.
- I performed all of these requests using the Python `apiclient` module to talk directly to the Gmail API (didn’t use `requests`).
- I learned that each type of call to the API has its own set of options that allow you to filter the returned data. Seems obvious now…
- I had more practice trying to parse multi-tiered JSON output.

~~~~
results = service.users().settings().filters().list(userId='me').execute()
    pprint(results)
~~~~

Again, I was underwhelmed with the outcome but learned so much more by actually doing this than if I was just reading a book. (Full code not online).


##Python Flask App

Last week we created [Python Flask Apps for our code challenge](http://pybit.es/codechallenge15_review.html). It was freaking awesome. If you saw my website you’ll see that it’s very “I’m just learning HTML” retro. (I didn’t have time for the CSS and Bootstrap).

I think I learned more Python in that week than any other time. It was full on and it was damn satisfying.

- I revived my HTML and CSS “skills” (Steady on! It's been a while!).
- I got to push learning Flask!
- I played with Jinja2 templates.
- I created my very first, working HTML Form that returned data to my *own* backend script and DB.
- Subsequently, I learned about HTML `GET` and `POST` requests! (Who knew?!)
- I learned `sqlite3` from scratch. I knew absolutely no SQL prior to last week!
- I created my first persistent SQL database.
- I created my first working Web App!

It was a *massive* learning experience. None of which was taught from one book as part of an “end of chapter exercise”.

This was purely for the thrill of creating my own web app. And it was **fun**! (Meal Tracker 5000 baby!).

The best part was that for this challenge I found information everywhere. YouTube, StackOverflow, Reddit, PyBites (Bam!), GitHub and some other books.

I’m happy with the code too. [Check it out here](https://github.com/pybites/challenges/tree/solutions/15/meal).


##Get on With it

So here’s the deal. If you’re finding it tough to learn Python then do the following:

- Come up with an idea for something to code. Make it something you’d want or use yourself. (My first app was an Overtime Tracker for the extra hours I worked at Oracle!)
- If you’re learning something new, make it something fun! (To learn how to automate sending emails I created a script that spams my workmates every evening! Sorry fellas!)
- Don’t just use one resource, search **everywhere**. Expect to find many ways to solve your problem, not just the way they might be telling you in the book you’re reading.
- Experiment in the Python Shell! It’s the best place to stuff around!
- As I said before, share your code and get people to give you feedback.
- Join us in our [100 Day Code Challenge](http://pybit.es/special-100days.html)! It’s been the leading factor for my recent increase in Python understanding.

Most of all though: **STICK WITH IT**. The failures and the frustrating evenings where the code just doesn’t work are so important. They totally suck but man do you learn!

And I seriously mean it when I say, Keep Calm and Code in Python!

-- Julian

*Anyone else remember the guy from the YouTube video at the top? That video may be **the** reason I started playing the guitar! I love it!*

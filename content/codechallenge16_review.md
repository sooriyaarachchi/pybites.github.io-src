Title: Code Challenge 16 - Query Your Favorite API - Review
Date: 2017-04-30 23:59
Category: Challenges
Tags: codechallenges, learning, Flask, APIs, Github, Google, books, Warcraft, quotes, Wikipedia, Forismatic
Slug: codechallenge16_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge16.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Query Your Favorite API](http://pybit.es/codechallenge16.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## PyBites

### Julian

As I discussed in my [post this week](http://pybit.es/learn-by-doing.html) about learning Python, this code challenge was pretty much directed at me.

Going into this one, I'd never accessed an API in my life!

I spent the entire week playing around with different APIs but primarily the World of Warcraft and Gmail APIs.

The work with the Gmail API was great learning but essentially a bust when it came to having a working script. I had an idea in mind as to what I wanted from it but I just wasn't able to get it done.

I did have a little more success with the [World of Warcraft API](http://wowwiki.wikia.com/wiki/World_of_Warcraft_API) however. I'm sure it means nothing to most of you reading this but I was able to pull down data about my player character and have it presented in a readable format. (JSON was also new to me!).

The code for this is [here](https://github.com/pybites/100DaysOfCode/tree/master/027). As it was my first API attempt, it is definitely quite simplistic. The intention is to wrap it all up such that I can recreate my character profile locally.

### Bob

I used various APIs this week:

* I combined the Twitter and Slack API in my article of this week: [How to Write a Simple Slack Bot to Monitor Your Brand on Twitter](http://pybit.es/twitter-monitor-slack-notify.html).

* For our 100 days challenge I created [an interactive script to query the OMDb API](https://github.com/pybites/100DaysOfCode/tree/master/026).

* For the challenge I really wanted to make a start migrating [fbreadinglist](http://fbreadinglist.com/) from PHP to Python. As it uses the [Google Books API](https://developers.google.com/books/) it was a good fit for this challenge. I completed the autocomplete feature using the same JS, but Python/Flask for the back-end:

![google books autocomplete 1]({filename}/images/pcc16_googlebooks1.png)

When you select a title it redirects to a page where it pulls more details from the Google Books API (buttons not yet implemented):

![google books autocomplete 2]({filename}/images/pcc16_googlebooks2.png)

## Community 

We got 2 cool Pull Requests. We are really stoked you submit code to our repo. Good work folks, keep up the momentum!

### Clamytoe

Martin submitted a cool project called [GitHub-Profiler](https://github.com/clamytoe/Github-Profiler) where he queries the Github API for a given user, entering 'pybites' it generates this nice page, awesome:

![github api 1]({filename}/images/pcc16_clamytoe1.png)

If bio and repos was not enough, scrolling towards the end it also lists gists: 

![github api 2]({filename}/images/pcc16_clamytoe2.png)

Code merged [on our community branch](https://github.com/pybites/challenges/tree/community/16/clamytoe).

### Dseptem

Another usage of APIs we got from Dante who used the [Forismatic API](http://forismatic.com/en/api/) to pull random quotes. The author's bio gets crawled from Wikipedia, really nice:

![Forismatic api 1]({filename}/images/pcc16_dseptem1.png)

When you hit "Another Quote!" the page refreshes and shows another random quote and its author + bio:

![Forismatic api 2]({filename}/images/pcc16_dseptem2.png)

Code merged [on our community branch](https://github.com/pybites/challenges/tree/community/16/dseptem).

---

We hope you are enjoying these challenges, learning along the way. Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...

---

Keep Calm and Code in Python!

-- Bob and Julian

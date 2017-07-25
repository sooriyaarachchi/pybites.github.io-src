Title: Learning Python by Building a Wisdom Quotes App
Date: 2017-05-09 14:10
Category: Learning
Tags: challenges, learning, guest, wikipedia, API, code review, flask, requests, quotes, forismatic
Slug: guest-learning-apis
Authors: Dante
Summary: In this guest post Dante tells us about his [Wisdom of the Ages](https://github.com/pybites/challenges/tree/community/16/dseptem) app he built for [PyBites code challenge 16](http://pybit.es/codechallenge16.html) (reviewed [here](http://pybit.es/codechallenge16_review.html)). The best way to learn Python is to build something and we are proud of our community achieving just that. 
cover: images/featured/pb-guest.png

In this guest post Dante tells us about his [Wisdom of the Ages](https://github.com/pybites/challenges/tree/community/16/dseptem) app he built for [PyBites code challenge 16](http://pybit.es/codechallenge16.html) (reviewed [here](http://pybit.es/codechallenge16_review.html)). The best way to learn Python is to build something and we are proud of our community achieving just that. 

---

## Query Your Favorite API Challenge

Only recently I started following PyBites, but I really liked the idea of the [code challenges](http://pybit.es/pages/challenges.html), so when I saw the opportunity to put some of my knowledge in practice, I took it without thinking twice.

As I like to challenge myself and up the bets, I decided I was going to query one API and then query another one using somehow the results of the first. Since I had some experience querying the Wikipedia API, I chose it then googled up for free APIs on the internet to use. I came by [an API to get random inspirational quotes](http://forismatic.com/en/api/), and the idea struck me: 

> A simple website that displays a random inspirational quote, with its author's biography as an addendum. Wikipedia could provide those biographies!

### App implementation

I quickly sketched the app using the well-known 'flask' and 'requests' modules, with a simple jinja2 template to display three variables: 

* The quote, 
* the quote's author, and 
* the quote's author's biography.

### Error handling

After the core functionality was done, I started to iron out some bugs by adding try/except blocks for expected errors: 

* the quotes API sometimes returned malformed JSON, 
* I couldn't grab a biography for an anonymous author.

## Making it pretty

Done with the 'insides' of my machine, I wanted to make it look pretty on the outside too, so I used my google-fu to search for bootstrap templates and themes, found one I liked ([Amoeba](https://bootstraptaste.com/free-one-page-bootstrap-template-amoeba/)) and after cutting down all the things I didn't need and downloading a favicon, my first iteration of [**Wisdom of the Ages**](https://github.com/pybites/challenges/tree/community/16/dseptem) was finished:

![wisdom of ages design]({filename}/images/pcc16_dseptem2.png)

## Experimenting

But I wanted more! Recently I had heard about a Python module called [pywebview](https://github.com/r0x0r/pywebview), which displays a barebones browser as an application to the user. I figured I could make the user of my script choose between the 'embedded' simple view of the website flask created and her own browser, but eventually dropped the functionality because it made everything more complicated (I even had to use threading to run code after starting the flask app website) with no real benefit.

## Refactoring

Finally, after some back-and-forth with PyBites (thanks for the feedback, again!), I refactored the code for readability, made it more pythonic, added an "another quote" button that refreshes the website on click and last but not least, prepared the app to display an 'Internal server error' if the quotes API is down or the user has no internet connection.

## Conclusion

I really enjoyed this experience and I'm looking forward to more challenges! Peer-reviewing code is a joy I don't usually get to experience. Thanks to the folks at PyBites and have fun with your coding!

---

Keep Calm and Code in Python!

-- [Dante](pages/guests.html#danteseptem)

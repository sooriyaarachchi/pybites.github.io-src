Title: Code Challenge 25 - Notification Service of Now Playing and Upcoming Movies - Review
Date: 2017-07-03 11:20
Category: Challenges
Tags: codechallenges, movies, series, digest, email, themoviedb, apis, argparse, requests, mailgun
Slug: codechallenge25_review
Authors: PyBites
Summary: In this article we review last week's [Notification Service of Now Playing and Upcoming Movies](http://pybit.es/codechallenge25.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Notification Service of Now Playing and Upcoming Movies](http://pybit.es/codechallenge25.html) code challenge. 

### The Movie Database (TMDb) 

This challenge we focused on [TMDb's API](https://www.themoviedb.org/documentation/api) to send html emails of movies / tv series. We decided to query 4 API endpoints: now playing movies, upcoming movies, popular TV series, and on-the-air TV series. 

We used 2 shelves for caching: movie info and items sent (to avoid duplicates in the mails). We also got to play with decorators and classes. We used [tmdbsimple](https://pypi.python.org/pypi/tmdbsimple) to interface with TMDb's API.

We followed [what we learned about packaging](https://pybit.es/python-packaging.html) to structure our modules. Having a notifications package now makes it easier to add a Twitter bot later on for example.

The code is [here](https://github.com/pybites/challenges/tree/community/25/bbelderbos) and this is a screenshot of part of the notification email:

![upcoming movies]({filename}/images/upcoming-movies.png)

We did not have time to build a front-end to add filters. We did start a login system in Flask but ran out of time. I think this would be a nice exercise for us learning Django. To be continued ...

### PRs

We got a nice PR from [santiagobenitez](https://github.com/santiagobenitez): a single script allowing to filter on genre, year and vote average, using `argparse`. It uses [mailgun](https://www.mailgun.com/) - "The Email Service For Developers" - for emailing.

His script demonstrates that it's not necessary to use a API wrapper package. He uses `requests` which leads to compact code like: `movies_resp = requests.get(upcoming_movies_url, params=query_params)` to query TMDb's API.

You can checkout the code [here](https://github.com/pybites/challenges/blob/community/25/santiagobenitez/movies.py). We read in the PR: "This is my first ever python code ..." - really? Good job! 

### Next

This was a challenge to sink your teeth in, there were many options, lot to code. This week we try to keep it simpler making the challenge smaller, not necessarily easier. We will also change topics a bit to do something entirely different: build a simple GUI app. Stay tuned ...

By the way there is no deadline to these challenges, you can start any challenge at any time. 

Just follow [our instructions](https://github.com/pybites/challenges/blob/master/INSTALL.md) and start coding. Have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

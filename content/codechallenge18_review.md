Title: Code Challenge 18 - Get Recommendations - Review
Date: 2017-05-15 11:37
Category: Challenges
Tags: codechallenges, books, Goodreads, API, oauth, Manning, Machine Learning, Netflix, recommendation engine, Parrotread, recommender system
Slug: codechallenge18_review
Authors: PyBites
Summary: Before moving onto the new challenge let's review [last week's challenge](http://pybit.es/codechallenge18.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

Last week we aimed at [Getting Recommendations From Twitter Influencers](http://pybit.es/codechallenge18.html). It required a bit more work and knowledge than anticipated so we leave it pending/working for now. We were also pretty busy last week.

We did fiddle with the Goodreads API managing to get a user authorized (oauth) and pull their friends' updates. We only need to parse the output and probably filter "books read" with a rating of >= 4 (out of 5). Some code to get you started [here](https://github.com/pybites/challenges/tree/solutions/18).

Another thing we'd like to build at some point is getting Netflix recommendations (digest email) because there is just too much to watch. Netflix does not have an API anymore though :( - Twitter has [a lot of Netflix tweets](https://twitter.com/search?q=netflix%20recommend&src=typd) but the challenge is the free text (spam) and filtering out the exact show name. [Parrotread](https://parrotread.com/) managed to do it for books so there must be a way. To be continued ... 

So building a recommendation engine takes more (structured) data and ML skills. We found some good resources to get started: 

* [List of Recommender Systems](https://github.com/grahamjenson/list_of_recommender_systems) 

* ML starter book: [Introduction to Machine Learning with Python: A Guide for Data Scientists](http://www.amazon.com/dp/1449369413/?tag=pyb0f-20). 

* In the making: Manning's [Practical Recommender Systems](https://www.manning.com/books/practical-recommender-systems). You can download a free chapter and [source](https://github.com/practical-recommender-systems) is already up and seems to use an interesting data set: [MovieTweetings](https://github.com/sidooms/MovieTweetings).

Challenges don't have deadlines so we will refer back to this one when we learned more about recommendation engines. Let us know if you made further progress on this one.

---

This week we have another nice free-form challenge for you: after last time's [API challenge](http://pybit.es/codechallenge16.html) success, we have a part 2 this week where we will let you post to your favorite API. Standby as we post the challenge in a bit ...

---

Keep Calm and Code in Python!

-- Bob and Julian

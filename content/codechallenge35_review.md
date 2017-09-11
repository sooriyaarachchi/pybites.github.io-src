Title: Code Challenge 35 - Improve Your Python Code With BetterCodeHub - Review
Date: 2017-09-11 14:00
Category: Challenges
Tags: bettercodehub, SIG, refactoring, code quality, clean code, software development, tools, platform
Slug: codechallenge35_review
Authors: PyBites
Summary: In this article we review last week's [Improve Your Python Code With BetterCodeHub](http://pybit.es/codechallenge35.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Improve Your Python Code With BetterCodeHub](http://pybit.es/codechallenge35.html) code challenge. 

### Submissions

* [hobojoe1848](https://github.com/hobojoe1848) submitted his [Generic Emailer Script](https://github.com/hobojoe1848/generic-emailer):

	This is a simple script I wrote to automate sending emails from my Gmail account. It’s generic such that I use it in various different programs. When I had BCH analyse the repo I received a score of 7, meaning it failed 3 points. The most obvious to me was the “Write Short Units of Code” test:

	![Better Code Hub Score of 7]({filename}/images/emailer-bch-7.png)

	The original script that resulted in this score is [here](https://github.com/hobojoe1848/generic-emailer/blob/master/generic_emailer.old)

	Tackling this issue had me refactor the entire script after which, BCH gave me a pass and my score jumped to 8:

	![Better Code Hub Score of 8]({filename}/images/emailer-bch-8.png)

	What a great tool! I’m a big fan of BCH after this!!

* [bbelderbos](https://github.com/bbelderbos) ran BCH on his small [codetips](https://github.com/pybites/codetips) Django REST Framework submission [of last week](https://pybit.es/codechallenge34_review.html): wow I was amazed to see it got a 9 right off the bat. DRF / Django lets you write quality code! 

	I did have to ignore the settings file adding a `.bettercodehub.yml` file to get to a 10. I also opened another issue to add tests (as the project is < 200 LOC BCH did not complain yet):

	![codetips final score]({filename}/images/bch-codetips.png)

	I also refactored Julian's [timezone-list project](https://github.com/hobojoe1848/timezone-list/pull/4) improving the already nice score of 8 to a 10

	* Before:
		![tzlist begin score]({filename}/images/bch-tzlist-before.png)

	* Seperating tz conversion into own module, separate from Flask app:
		![tzlist comp balance]({filename}/images/bch-tzlist-change1.png)

	* Added some unittests:
		![tzlist tests]({filename}/images/bch-tzlist-change2.png)
	
	* Final score:
		![tzlist final score]({filename}/images/bch-tzlist-after.png)

	I also like BCH: it makes you think about your code and improve it. The tool has a nice design and performs well. I also like the GitHub workflow we learned during this challenge.

* If you did some work for this challenge, PR it or message us with the details and we'll include it here.

---

As there is no deadline to these challenges, we will update here when we get more cool submissions for this challenge ... 

Just follow [our instructions](https://github.com/pybites/challenges/blob/master/INSTALL.md) and start coding!

Stay tuned for our next challenge ...

---

Keep Calm and Code in Python!

-- Bob and Julian

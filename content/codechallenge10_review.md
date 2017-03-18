Title: Code Challenge 10 - Build a Hangman Game - Review
Date: 2017-03-18 10:00
Category: Challenges
Tags: codechallenges, code review, learning, game, hangman, forks, dunder
Slug: codechallenge10_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge10.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge10.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Possible solution and learning

First of all it is great to see [more people working on our challenges](https://github.com/pybites/challenges/network).

Games are challenging, we learned quite a bit from this one. We also saw better ways of doing things. Here is a summary what we learned:

* We used a class to keep state. We used two lists for secret and guessed_word. Looking at it now self.secret_word should probably be a tuple (inmutable). Handling non-ASCII in the constructor made the rest easier:
		
		self.secret_word = list(word.lower())
		self.guessed_word = [PLACEHOLDER if c in ASCII else c
							for c in self.secret_word]

* We could probably save the extra self.num_wrong_guesses variable by just popping states of the HANG_GRAPHICS list (or use the hang_graphics() generator directly). It's a real eye opener how you pick up these kind of improvements from reading other's code. If you pick up one habit from our challenges let it be to start reading source. As somebody remarked:

	> I like seeing the other solutions. There are definitely small things that I could have done better/more pythonically.

* It was also fascinating to see that there are various ways to accomplish this task: to check for a win, you can compare word with secret. We checked for absense of PLACEHOLDER in the guess letter list. 

* Small details. For example we had a debug flag while developing, and we used the \_\_str\_\_ dunder to build up a string representation of the object. What was new though was that you can use it with 'self' as in .format(self). Small tricks you pick up by practice. 

* UI: we saw other solutions clearing the screen after each guess, and showing the ASCII constant (alphabet) with guesses stripped out, nice. 

* We even saw an try/except block wrapped around 'input = raw_input' to account for Python 2vs3. We will study this in more detail soon ...

Our solution is [here](https://github.com/pybites/challenges/blob/solutions/10/hangman-pb.py). 

## Process update around Forking

We got some feedback that Forks don't lead to activity on your GH profile. One of our followers was so nice to update [our INSTALL](https://github.com/pybites/challenges/blob/master/INSTALL.md) (via PR). Maybe you want to go that route if the credit aspect is an issue for you. See [issue #2](https://github.com/pybites/challenges/issues/2) for more details.

## Feedback

We hope you enjoy these challenges. Please provide us feedback if we can improve anything ...

If you have an interesting challenge you want us to feature, don't hesitate to reach out to us.

See you next week ...

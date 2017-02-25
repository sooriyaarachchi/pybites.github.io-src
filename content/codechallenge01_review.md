Title: Code Challenge 01 - Word Values Part I - Review
Date: 2017-01-13 12:40
Category: Challenges
Tags: codechallenges, code review, HN, github, learning, max, generators, scrabble, refactoring
Slug: codechallenge01_review
Authors: PyBites
Summary: Wow! We have been amazed by the great response on [github](https://github.com/pybites/challenges) and [HN](https://news.ycombinator.com/item?id=13352447). It's Friday so we review the code challenge of this week. We describe our learning and a possible solution. We will also digest comments left on the [Monday post](http://pybit.es/codechallenge01.html).
cover: images/featured/pb-challenge.png

## Thanks for coding with us!

Wow! We have been amazed by the great response on [github](https://github.com/pybites/challenges) and [HN](https://news.ycombinator.com/item?id=13352447). It's so cool to see [many developers](https://github.com/pybites/challenges/network/members) jump on this :) 

This is awesome!

![awesome response on github, 70 forks as of this writing]({filename}/images/awesome-response.png)

It's Friday so we review the code challenge of this week. We describe our learning, a possible solution. We will also digest comments left on the [Monday post](http://pybit.es/codechallenge01.html).

## Process and learning

### >>> Julian

It's funny, going into this challenge I actually thought it was going to be easy! I was wrong!
The concept was simple enough and I had a decent idea as to how I was going to write the program. I hit a wall however, when I realised I had to code my answer within the framework of the unittest. 

As a newbie programmer, having to almost "restrict" my code to work with the unittest was quite difficult.
Furthermore, working with the external data.py file also added a little complexity. I'm definitely used to having all data and variables located in the local file I'm working on.

Probably the biggest pain point was trying to work with the LETTER_SCORES dict:

~~~~
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                              for letter in letters.split()}
~~~~

The for loop within the dict threw me off completely and I spent what felt like hours trying to make sense of it. It wasn't until Bob expanded it out into multiple lines of code that it finally made sense.

On the flip side, I was pleasantly surprised with myself when I got the load_words() function working. I recalled Bob's comment on my code that I could use 'with' (context manager) to open an external file. Doing this made it much simpler.

Working on the max_word_value() function was equally as satisfying as it was much more familiar coding ... but that may not be a good thing.

In the end I wasn't actually able to get the program working. Not my proudest moment but definitely an eye opener as to how much further I have to go with my code. I'll hopefully have time this weekend to take another look - maybe a fresh look after a day off will highlight something I missed earlier!

My code is [here](https://github.com/hobojoe1848/challenges/tree/master/01) if you're interested! Be gentle!

Going forward with these challenges, I think we'll try and shake it up a little. Not make it "mandatory" to code the program within the unittest framework which should allow us to get a more diverse code base from the community.

Overall, while difficult for me and even frustrating at times, I definitely enjoyed the challenge. It forced me to learn to read code I'd never seen before and rethink the way I write it myself.

## Possible solution and Python idioms

### >>> Bob

This was a good exercise. As Julian said we might leave out unittests next time to make it less stringent and make up other requirements like max LOC. We also will provide two template files: beginner (more hand-holding) and advanced (almost blank file). You will see it on Monday ...

My code is [here](https://github.com/bbelderbos/challenges/blob/master/01/wordvalue.py). Some comments:

#### load_words()

	def load_words():
		with open(DICTIONARY) as f:
			return [word.strip() for word in f.read().split()]

Yes, "with" is the way to go to open files. Initially I had return f.read().split() but then I saw the comment of [sesh00](http://pybit.es/codechallenge01.html): he used a list comprehension to make sure each word had whitespace stripped which is a good approach.

#### calc_word_value(word)

	def calc_word_value(word):
		return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

The dictionary. You can access values by using letter keys as LETTER_SCORES['A'] etc, but what if there is a non-valid character? There were two words with '-' in it so they would cause a KeyError. Using the dict get() method you can give it a default value of 0. Safety first: 

	$ grep [^A-Za-z] dictionary.txt 
	Jean-Christophe
	Jean-Pierre
	>>> word = 'Jean-Christophe'
	>>> from data import LETTER_SCORES
	>>> [LETTER_SCORES[c.upper()] for c in word]
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 1, in <listcomp>
	KeyError: '-'
	>>> [LETTER_SCORES.get(c.upper(), 0) for c in word]
	[8, 1, 1, 1, 0, 3, 4, 1, 1, 1, 1, 1, 3, 4, 1]

For another more verbose (cleaner?) way to write this see [here](https://github.com/jrjames83/pybit-es-01/blob/master/01%20Scrabble%20Solution.ipynb):

	scores = [LETTER_SCORES[letter] for letter in letters 
				if letter in LETTER_SCORES.keys()]

Then I use sum() to add up all letter values. You can give it a list comprehension but also a generator which is best practice (lazy loading):

	# sum with list comprehension
	>>> sum([LETTER_SCORES.get(c.upper(), 0) for c in word])
	31
	# or with a generator, just drop the []
	>>> sum(LETTER_SCORES.get(c.upper(), 0) for c in word)
	31

Of course you can totally write just a for loop and sum to a total variable. And as a beginner I encourage you to actually do this to get a feel for how an iterator works internally.

#### max_word_value(words)

	def max_word_value(words=None):
		return max(words or load_words(), key=lambda w: calc_word_value(w))

This might be advanced to a beginner. To pass the unittests you have to account for two scenarios: 

* A word list is given, if not load the default dictionary, I do this in one statement with or, using default arg None for words.

* Use a criteria for max.

The max builtin calculates the max of an iterator, very convenient here. The cool thing is that it takes a key optional argument (like the sorted() builtin) which you can give a function to 'max on'. 

In this case I don't want to max on for example len of word, but on the word value, so we re-use calc_word_value() here. For more details on this I recommend reading [this great article](https://dbader.org/blog/python-min-max-and-nested-lists).

## PyBites digest of comments on Monday's challenge post

Thanks for [your comments](http://pybit.es/codechallenge01.html#disqus_thread). We are really stoked to learn about all these different approaches. Also you cannot read enough other developers' code, it's a great way to learn fast!

* We already mentioned [Sesh' solution](https://github.com/sesh/challenges/blob/master/01/wordvalue.py), similar to ours, yet still some minor differences / improvements. Queston for the comments (anybody?): words=load_words() as default arg to max_word_value(), probably not a problem here, but doesn't that fall under the [Mutable Default Arguments gotcha](http://docs.python-guide.org/en/latest/writing/gotchas/)?

* [ukaratay solution](https://github.com/ukaratay/challenges/blob/master/01/wordvalue.py) is also similar, but he uses upper() on the word = 1 call instead my multiple calls for each char = better. Tiny details but they matter when you add them up and when things scale.

		return sum(LETTER_SCORES.get(char, 0) for char in word.upper())

* [alhart2015 solution](https://github.com/alhart2015/challenges/blob/master/01/wordvalue.py) is a great addition, specially max_word_value() has a longer format, probably easier to read to people just starting out in Python.

* [check out this notebook](https://github.com/jrjames83/pybit-es-01/blob/master/01%20Scrabble%20Solution.ipynb), Jeffrey James shared a complete Pandas solution. The cool thing about this approach is that it calculates the score for each dictionary word and loads it into a Pandas dataframe which he uses to show us the relationship between word length and score, interesting. Well done and thanks Jeffrey!

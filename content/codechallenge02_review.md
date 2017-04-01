Title: Code Challenge 02 - Word Values Part II - A Simple Game - Review
Date: 2017-01-20 9:00
Category: Challenges
Tags: codechallenges, code review, github, learning, game, scrabble, itertools
Slug: codechallenge02_review
Authors: PyBites
Summary: It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge02.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's Friday again so we review the [code challenge of this week](http://pybit.es/codechallenge02.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## A possible solution

See [here](https://github.com/pybites/challenges/blob/solutions/02/game.py) for the complete solution.

Some learnings:

* First we had the user interface like this: 

		def input_word(draw):
			while True:
				word = input('Form a valid word: ').upper()
				if not set(word) < set(draw):
					print('One or more characters not in draw, try again')
					continue
				elif not word.lower() in DICTIONARY:
					print('Not a valid dictionary word, try again')
					continue
				return word

	But after learning about [EAFP (easier to ask for forgiveness than permission)](http://pybit.es/error_handling.html) we thought it was more Pythonic to use exceptions. There was also a bug in the first check above (see comments, great learning!)

		def input_word(draw):
			while True:
				word = input('Form a valid word: ').upper()
				try:
					return _validation(word, draw)
				except ValueError as e:
					print(e)
					continue

		def _validation(word, draw):
			# thanks Durmus
			for char in word.upper():
				if char in draw:
					draw.remove(char)
				else:
				raise ValueError("{} is not a valid word!".format(word))
			if not word.lower() in DICTIONARY:
				raise ValueError('Not a valid dictionary word, try again')
			return word

* random.sample makes it easy to get n number of random letters in one go: 

		def draw_letters():
			return random.sample(POUCH, NUM_LETTERS)

* get_possible_dict_words - the hardest part. To get all possible letter combinations from the letter draw, you need itertools.permutations, not combinations, because order does matter: 

		>>> len(list(itertools.combinations(letters, 2)))
		21
		>>> len(list(itertools.permutations(letters, 2)))
		42

	See also [our post on itertools](http://pybit.es/itertools-examples.html). See also Durmus' comment / solution here for an alternative using combinations ...

* First the helper generator to do the work:

		def _get_permutations_draw(draw):
			for i in range(1, 8):
				yield from list(itertools.permutations(draw, i))  # >= 3.3

	This creates all permutation of 1, 2, 3, 4, 5, 6, and 7 letters.

	We store all those in permutations and then use a set operation again to get all valid dictionary words:

		def get_possible_dict_words(draw):
			permutations = [''.join(word).lower() for word in _get_permutations_draw(draw)]
			return set(permutations) & set(DICTIONARY)

We use the calc_word_value and max_word_value methods from [challenge 01](http://pybit.es/codechallenge01.html) to calculate which word has the most value. 

The rest is main() calling the methods and outputting (as was provided in the template).

## Tests

We got a request in the comments for tests to verify the work. Good idea, they are [here](https://github.com/pybites/challenges/blob/master/02/test_game.py).

	$ python test_game.py 
	......
	----------------------------------------------------------------------
	Ran 6 tests in 0.056s

	OK

## Its fun (addictive?) to play :)

	[bbelderb@macbook 02 (master)]$ python game.py 
	Letters drawn: T, I, I, G, T, T, L
	Form a valid word: tig
	Word chosen: TIG (value: 4)
	Optimal word possible: gilt (value: 5)
	You scored: 80.0
	[bbelderb@macbook 02 (master)]$ python game.py 
	Letters drawn: O, N, V, R, A, Z, H
	Form a valid word: zar
	Word chosen: ZAR (value: 12)
	Optimal word possible: zonar (value: 14)
	You scored: 85.7
	[bbelderb@macbook 02 (master)]$ python game.py 
	Letters drawn: E, P, A, E, I, O, A
	Form a valid word: pi
	Word chosen: PI (value: 4)
	Optimal word possible: apio (value: 6)
	You scored: 66.7
	[bbelderb@macbook 02 (master)]$ python game.py 
	Letters drawn: B, R, C, O, O, E, O
	Form a valid word: broc
	Not a valid dictionary word, try again
	Form a valid word: f
	One or more characters not in draw, try again
	Form a valid word: bore
	Word chosen: BORE (value: 6)
	Optimal word possible: boce (value: 8)
	You scored: 75.0

## Any issues or feedback?

What did you learn this challenge? Feel free to share you code in the comments below. 

How are you experiencing these challenges? You like the format? What can we do differently and/or better?

## next(challenges)

Monday we will be back with a new challenge, stay tuned ...

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/) if you already forked it.

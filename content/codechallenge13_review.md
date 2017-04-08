Title: Code Challenge 13 - Highest Rated Movie Directors - Review
Date: 2017-04-08 23:59
Category: Challenges
Tags: codechallenges, learning, data analysis, movies, imdb, sort, namedtuples, defaultdict
Slug: codechallenge13_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge13.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Highest Rated Movie Directors](http://pybit.es/codechallenge13.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Our solution and learning

You can find our solution [here](https://github.com/pybites/challenges/blob/solutions/13/directors.py). Some highlights:

* In get_movies_by_director() we use csv.DictReader to parse the csv file:

		with open(MOVIE_DATA) as f:
			for line in csv.DictReader(f):
				...

* We use a defaultdict(list) for our initial parsing of movies:

		m = Movie(title=movie, year=year, score=score)
		directors[director].append(m)

* get_average_scores() returns a directors dict via a dict comprehension (note the [subtle refactoring](https://github.com/pybites/challenges/commit/959acf258a99730b732eb0915aa2088adf11e143), glad we had our tests), where keys are (director, mean score) and values their movies. We only take directors with at least MIN_MOVIES.

* Although Python3 has statistics.mean we rolled our own (\_calc_mean) because we first extract the score from the Movie namedtupe and added rounding (although that should maybe go in the print_results function). 

    Next time we would use statistics.mean, because the more you leverage the stdlib the better. These considerations happen when coding, reviewing your and others code, good learning. 
    
    Although movies should not be 0 we are defensive by never allowing the denominator to be 0:

		mean = sum(ratings) / max(1, len(ratings))

	You could also write: 
		
		mean = sum(ratings) / len(ratings) if ratings else 0

* print_results() then prints the desired output. The enumerate is handy to get the sequence numbers for the top NUM_TOP_DIRECTORS directors. You can give it a start with a 2nd argument, 1 in this case. 

    We used zfill before to print 01 / 02 etc., but found out that [you can tackle this in the format syntax](https://github.com/pybites/challenges/commit/72b4642e24058758530ea463cbd3c0fbe2dfce1d). We might refactor all these formats to use F-string, it would make this a lot cleaner :)

* Again it was nice to work on this code having tests:

		$ python test_directors.py
		tests pass

## TODOs

We realized during the challenge that you could also solve this with SQL or Pandas. We will update the solutions branch when we get around this. It would be nice to give it a try. Of course if you took these (or other) approaches feel free to share your solution [opening a PR against our community branch](https://github.com/pybites/challenges/compare).

## Community 

Here is [another solution by atakume](https://github.com/pybites/challenges/blob/community/13/directors-atakume.py) we merged in our community branch. What we like about this solution is the use of itertools.groupby, doing the sorting outside the print_results function, and the second namedtuple which adds readability:

	Filmography = namedtuple('Filmography', 'director movies avg_score')
	
## Stay tuned

Next week we will let you play with decorators, a great feature for writing DRY, reusable code. It will be fun :)

We hope you are enjoying these challenges, learning along the way. Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...

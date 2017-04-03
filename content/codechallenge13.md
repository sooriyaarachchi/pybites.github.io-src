Title: Code Challenge 13 - Highest Rated Movie Directors
Date: 2017-04-03 00:25
Category: Challenges
Tags: codechallenges, learning, data analysis, movies, rating
Slug: codechallenge13
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! After last week's ([tictactoe game](http://pybit.es/codechallenge12.html)), we'd like to sharpen your data analysis skills this week by parsing a movie data set in search for highest rated directors. Enjoy and we review solutions end of this week.
cover: images/featured/pb-challenge.png

> There is nothing like a challenge to bring out the best in man. - Sean Connery

Hi Pythonistas, a new week, a new 'bite' of Python coding! After last week's [tictactoe game](http://pybit.es/codechallenge12.html), we'd like to sharpen your data analysis skills this week by parsing a movie data set in search for highest rated directors. Enjoy and we review solutions end of this week.

### Details

There is this great ML article [Predict Movie Rating](https://blog.nycdatascience.com/student-works/machine-learning/movie-rating-prediction/). In this week's code challenge we use its data set to get the 20 highest rated directors based on their average movie IMDB ratings.

Steps:

* As mentioned in the article the dataset is [here](https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv), but we provided a copy in the repo's 13/ subfolder.

* Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts from which you only need the following k,v pairs:

		OrderedDict([...
					('director_name', 'Lawrence Kasdan'),   
					...
					('movie_title', 'Mumford\xa0'),
					...
					('title_year', '1999'),
					...
					('imdb_score', '6.9'),
					...

* Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data. However going to min 5 movies we miss Sergio Leone :(

* Take movies of year >= 1960.

* Print the top 20 highest rated directors with their movies ordered desc on rating.

It should look something like this (indeed some awesome movies here!):

	$ python directors.py

	01. Sergio Leone                                         8.5
	------------------------------------------------------------
	1966] The Good, the Bad and the Ugly                     8.9
	1968] Once Upon a Time in the West                       8.6
	1984] Once Upon a Time in America                        8.4
	1964] A Fistful of Dollars                               8.0

	02. Christopher Nolan                                    8.4
	------------------------------------------------------------
	2008] The Dark Knight                                    9.0
	2010] Inception                                          8.8
	2014] Interstellar                                       8.6
	2012] The Dark Knight Rises                              8.5
	2006] The Prestige                                       8.5
	2000] Memento                                            8.5
	2005] Batman Begins                                      8.3
	2002] Insomnia                                           7.2

	03. Hayao Miyazaki                                       8.2
	------------------------------------------------------------
	2001] Spirited Away                                      8.6
	1997] Princess Mononoke                                  8.4
	2004] Howl's Moving Castle                               8.2
	2008] Ponyo                                              7.7

	04. Quentin Tarantino                                    8.2
	------------------------------------------------------------
	1994] Pulp Fiction                                       8.9
	2012] Django Unchained                                   8.5
	1992] Reservoir Dogs                                     8.4
	2009] Inglourious Basterds                               8.3
	2003] Kill Bill: Vol. 1                                  8.1
	2004] Kill Bill: Vol. 2                                  8.0
	2015] The Hateful Eight                                  7.9
	1997] Jackie Brown                                       7.5

	...
	16 more
	...

We included [a template](https://github.com/pybites/challenges/tree/master/13/directors-template.py) but maybe you want to code this up from scratch and/or use your favorite power tools (Pandas, SQL, etc.)

We also included [some tests](https://github.com/pybites/challenges/blob/master/13/test_directors.py).

### Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking. If you want to share your solution do [a PR](https://github.com/pybites/challenges/compare) and we will add it to [our community branch](https://github.com/pybites/challenges/tree/community) and link to it in our end-of-the-week review.

### Archive

You can find all our code challenges so far [here](http://pybit.es/pages/challenges.html). If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

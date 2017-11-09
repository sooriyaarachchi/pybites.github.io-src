Title: Code Challenge 44 - Marvel Data Analysis (Alicante PyChallengeDay)
Date: 2017-11-10 00:01
Category: Challenge
Tags: marvel, data, data analysis, csv, collections, namedtuple, Counter, Live Challenge, Python Alicante, Bokeh, coffee
Slug: codechallenge44
Authors: PyBites
Summary: Hi Pythonistas, this is a very special edition! Today, the 10th of November, we launch our first Live Code Challenge. We partnered up with [Python Alicante](https://twitter.com/python_alc) and we will be hosting this code challenge with them at the University of Alicante. If you don't happen to live in Alicante but do want to code today 10am-13pm CET you are more than welcome to join [this Gitter channel](https://gitter.im/pybites/marvel).
cover: images/featured/pb-challenge.png
status: draft

> It's not that I'm so smart, it's just that I stay with problems longer. - A. Einstein

Hi Pythonistas, this is a very special edition! Today, the 10th of November, we launch our first Live Code Challenge. We partnered up with [Python Alicante](https://twitter.com/python_alc) and we will be hosting this code challenge with them at the University of Alicante. If you don't happen to live in Alicante but do want to code today 10am-13pm CET you are more than welcome to join [this Gitter channel](https://gitter.im/pybites/marvel).

![marvel spiderman coffee mug]({filename}/images/pcc44-coffee-mug.jpg)

## The Challenge

We all love Marvel, don't you? So here's the deal: we found a CSV with Marvel data taken from [this database](http://marvel.wikia.com/wiki/Marvel_Database).

We are going to have you write some Python to get this data into a usable data structure to answer some questions about the data.

### Preparation

1. If you don't have git installed, please [install it now](https://git-scm.com/downloads). Then fork [our repo](https://github.com/pybites/marvel_challenge) and follow these steps

		(after forking the repo)
		$ git clone https://github.com/<your_user>/marvel_challenge -b community
		$ cd marvel_challenge
		$ git checkout -b PCC44

2. Open `marvel.py` in your favorite editor.

3. Code your solution (see next section)

4. Verify your solution:

		$ python test_marvel.py
		.....
		----------------------------------------------------------------------
		Ran 5 tests in 0.424s

		OK

5. Submit your solution by pushing your branch to

		$ git push origin PCC44

	Then browse to your fork and open a PR again [our repo](https://github.com/pybites/marvel_challenge) -> community branch. No worries we are happy to help you if you get stuck.

### Please answer ...

`marvel.py` has already some stubs, here is what we want you to try:

1. Parse the `marvel-wikia-data.csv` CSV file and load it into a data structure. You probably want a list of dicts or namedtuples, one for each row. Store this in `data` which will be in the module's namespace (`data = list(...` line already there)

2. Get the most popular characters based on the number of appearances they made in comics over the years.

3. Get the year with most and least new Marvel characters introduced respectively, return a (max_year, min_year) tuple. Expect min/max to be pretty far apart.

4. What percentage of the comics characters is female? Please give us the percentage rounded to 2 digits.

5. Good vs bad characters: return a dictionary of bad vs good vs neutral characters per sex. The keys are *Bad Characters*, *Good Characters*, *Neutral Characters*, the values are integer percentages. Who plays the villain more often, a man or a woman?

### Data Viz Bonus

OK you know Python inside out, and this was pretty easy. Sounds like you? Please surprise us with:

* Use your favorite Python visualization library and make one or more plots for 2.-5.
* Or try to answer some question you might have about this data set. 
* Feel free to use [nbviewer](nbviewer.jupyter.org) and just PR the link to your notebook. 
* You could even write a quick Flask app to wrap your graph, like [we did here](https://pybit.es/codechallenge28_review.html).

Here for example we used [Bokeh](https://bokeh.pydata.org/en/latest/) to plot newly introduced characters per year:

![example bokeh plot for bonus]({filename}/images/pcc44-bokeh-plot.png)

## Win a Python book!

The best part, right? You can win a hardcopy of [Automate the Boring Stuff](https://automatetheboringstuff.com/) (it's cool, it [surely helped us](https://pybit.es/automate_the_boring_stuff_review.html)).

There are 2 conditions though:

- You can only PR once, that's the PR that counts, so make sure you have a working solution before you hit that button.
- Only PRs submitted before 13 CET (10th of Nov) are taken into account.

We will determine the winner by a simple algorithm: solution*0.5 + speed*0.3 + design*0.2 (does it work / how fast did you PR / PEP8 + code quality)

![flyer announcement]({filename}/images/pcc44-flyer.jpeg)

## Pybites Slack

You like these challenges? We have published [quite a few](https://github.com/pybites/challenges) and we're not planning to stop anytime soon.

You really like them and plan on PR'ing more in the future? Then consider joining our private Slack channel sending us [an email](mailto:pybitesblog@gmail.com). This way you get the unique opportunity to learn from other passionate Pythonistas and share some of your experience.

## About

Our goal is to learn and teach you Python through practical exercises. Learning a programming language is way more fun as a community!

For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or [drop us an email](mailto:pybitesblog@gmail.com).

---

Keep Calm and Code in Python!

-- PyBites

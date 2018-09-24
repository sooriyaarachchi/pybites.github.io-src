Title: Code Challenge 51 - Analyse NBA Data with SQL/sqlite3 - Review
Date: 2018-09-24 11:18
Category: Challenges
Tags: sqlite3, SQL, data analysis, data, NBA
Slug: codechallenge51_review
Authors: PyBites
Summary: In this article we review last week's [Analyse NBA Data with SQL/sqlite3](http://pybit.es/codechallenge51.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Analyse NBA Data with SQL/sqlite3](http://pybit.es/codechallenge51.html) code challenge. 

## Our solution

Check out [our solution for this challenge](https://github.com/pybites/challenges/blob/solutions/51/nba.py).

Some learnings:

- Use `cursor.executemany` to bulk insert records.

- We were using `cursor.fetchall` but to get one record/row you can use `fetchone` (thanks @clamytoe)

- Practice `GROUP BY` (`year_with_most_drafts`)

- Simple SQLite arithmetic (`games/active AS games_per_year`)

- Probably don't need `CAST` if you add types to DB columns (looking at other PRs!)

## Community solutions

Check out [solutions PR'd by our community](https://github.com/pybites/challenges/tree/community/51).

Some learnings taken from these Pull Requests: 

- > Refreshed SQL. Learned about sqlite command line. Learned PyCharm DataSource integration and querying. Refreshed git commands.

- > I used this challenge as a chance to experiment with Jupyter notebook to help visualize the data

## Read Code for Fun and Profit

You can look at all submitted code [here](https://github.com/pybites/challenges/pulls?q=is%3Apr+is%3Aclosed) and/or pulling [our Community branch](https://github.com/pybites/challenges/tree/community).

Other learnings we spotted in Pull Requests week: _itertools, difflib / similarity measures, collections, pytest and patch._

Thanks to everyone for your participation in our blog code challenges! 

## Need more Python Practice?

Subscribe to our blog (sidebar) to get a new PyBites Code Challenge (PCC) in your inbox each Monday. 

And/or take any of our 50+ challenges [on our platform](https://codechalleng.es/challenges/). 

Prefer coding self contained exercises in the comfort of your browser? Try our growing collection of [Bites of Py](https://codechalleng.es/bites/).

Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your progress [on our platform](https://codechalleng.es/100days/).

---

Keep Calm and Code in Python!

-- Bob and Julian

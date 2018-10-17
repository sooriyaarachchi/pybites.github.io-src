Title: Code Challenge 55 - #100DaysOfCode Curriculum Generator
Date: 2018-10-16 12:47
Category: Challenge
Tags: code challenge, challenges, 100DaysOfCode, json, books, learning, data science
Slug: codechallenge55
Authors: PyBites
Summary: Hi Pythonistas, Welcome to Pybites Code Challenge 55! In this challenge we're asking that you create your own #100DaysOfCode Curriculum Generator.
cover: images/featured/pb-challenge.png

> There is an immense amount to be learned simply by tinkering with things. - Henry Ford

Hey Pythonistas,

It's time for another code challenge! This week we're asking you to create your own #100DaysOfCode Curriculum Generator.

Sounds exciting? It gets even better: with this challenge you can even be featured on [our platform](https://codechalleng.es/)! Read on ...

## The Challenge

Did you notice that every serious progress starts with a plan? This is why we are big advocates of the [#100DaysOfCode](https://www.100daysofcode.com). Heck we even build [a whole Python course around it](https://talkpython.fm/100days?utm_source=pybites).

So here is the deal: PyBites is expanding its _[100 Days tracker ("grid") feature](https://codechalleng.es/100days)_: we want folks to add their own curriculums or _learning paths_.

### Only one requirement: return a valid JSON response

You can make this as simple or sophisticated as you want, the only thing we request is a standard response JSON template so we can easily parse it on the platform:

Built with [ObjGen](http://www.objgen.com) -> [http://www.objgen.com/json/models/q2S4Q](http://www.objgen.com/json/models/q2S4Q)

		{
		"title": "title of your 100 days",
		"version": 0.1,
		"github_repo": "https://github.com/pybites/100DaysOfCode",
		"tasks": [
			{
			"day": 1,
			"activity": "what you need to do this day?",
			"done": false
			},
			{
			"day": 2,
			"activity": "what you need to do this day?",
			"done": false
			},
			{
			"day": 3,
			"activity": "what you need to do this day?",
			"done": false
			},
		...
		...
			{
			"day": 100,
			"activity": "milestone ... 100 days done",
			"done": false
			}
		]
		}

**Update 17/10/2018:** we took `startDate` and `goals` out because these are not relevant for the learning path, more for the cosumers of it. `github_repo` is optional.

### An example

Here is what we plan to do, maybe it serves as an idea how you could code this challenge up:

* as I (Bob) want to learn Data Science I am selecting 4 or 5 books I want to go through
* as #100DaysOfCode works best by spending an hour a day I am dividing the books in _n_ pages to read every day
* I am going to add the books to [our reading list app](http://pbreadinglist.herokuapp.com)
* keeping it generic, my script will accept a bunch of book IDs (URLs) from that app and scrape the title and number of pages for each book
* I calculate the daily number of pages to read every day and define page ranges for each of the 100 days
* I convert this to the required JSON output above

If you like this idea, we opened an API endpoint to more easily pull in book info based on (Google) book ID, for example: [http://pbreadinglist.herokuapp.com/api/books/bRpYDgAAQBAJ](http://pbreadinglist.herokuapp.com/api/books/bRpYDgAAQBAJ). Just replace the bookid in this endpoint.

### More ideas

Of course it does not have to be centered around books, it can be any other way you like to plan your #100DaysOfCode. As long as you return the required JSON. 

Other ideas that come to mind: 

* Set out your plan in a Google sheet and parse that,
* Make a curriculum pointing to various Lynda/Safaribooks/Pluralsight courses and try to make a daily task list scraping those sites,
* Make a curriculum parsing one or more (Pycon) YouTube feeds,
* Make a curriculum parsing our blog challenges and Bites of Py exercises,
* It all comes down to planning your resources and break them down into 100 digestible units. 

As usual, this is a challenge that came about wanting to _scratch our own itch_. Lack ideas? Remember there is always something you can enhance or automate for yourself or somebody else, and by doing so sharpening your coding skills!  

### Be featured

If you want to share your learning path with our community let us know in your PR linking to your JSON file and a short description. We will then add it to [our 100 days grid app](https://codechalleng.es/100days/). 

If you need help getting ready with Github, see our new [instruction video](https://youtu.be/vJsyLSZxqVw).
<br>

## PyBites Community

A few more things before we take off:

* Do you want to discuss this challenge and share your Pythonic journey with other passionate Pythonistas? Confirm your email on our platform then request access to our Slack via [settings](https://codechalleng.es/settings/).

* PyBites is here to challenge you because becoming a better Pythonista requires practice, a lot of it. For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or ping us on our Slack.

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!

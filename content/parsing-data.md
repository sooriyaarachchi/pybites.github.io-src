Title: How to Parse Common Data Formats in Python
Date: 2017-05-16 20:37
Category: Learning
Tags: learning, code, programming, python, resources, csv, sqlite3, json, xml
Slug: parsing-data
Authors: PyBites
Summary: In this post we demonstrate ways in which you can parse common data formats used in Python.
cover: images/featured/pb-article.png

One of the biggest jumps you make in your Python learning is when you start dealing with external data. 

With this post we wanted to demonstrate a few ways you can work with the more common data formats. Why? Because it’s a big deal when you’re starting out! Furthermore, unless you do it often enough it’s easy to forget how so bookmark this baby and reference it!

The links below are to articles and scripts we’ve actually written as well as to external resources we’ve found helpful.

<br>
##1. CSV

If you’re going to play with CSV files, `DictReader` is your friend. It converts each row into an `OrderedDict` (Hallelujah!).

**Reading the contents of a CSV file:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/001/pytip.py)
~~~~
for entry in csv.DictReader(f, fieldnames=FIELDS):
    yield entry
~~~~

<br>
**Opening and reading the CSV using a `with` statement:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/030/movies.py)

~~~~
def read_csv(cf=CSV_FILE):
    with open(cf, 'r') as csvfile:
        return list(csv.DictReader(csvfile))
~~~~

<br>
##2. JSON

JSON is a must these days, especially if you want to work with APIs. 

**Simple read of JSON data pulled down by `requests`:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/027/warcraft_scraper.py)

~~~~
data = json.loads(r.text)
~~~~

<br>
**One of our first articles used a `with` statement to load in JSON data:**

[Article/Code Link](http://pybit.es/kindle-json-to-html.html)

~~~~
def load_json(json_file):    
    with open(json_file) as f:        
        return json.loads(f.read())
~~~~

<br>
**Our Challenge 07 review used `yield` to return the JSON data:**

[Article/Code Link](http://pybit.es/codechallenge07_review.html)

~~~~
def get_tweets(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)

~~~~

<br>
**Note the `.json()` method on `requests.get`:**

[Code Link](https://github.com/pybites/weather_compare/blob/master/weather.py)

~~~~
data = requests.get(API_URL.format(city, API_KEY)).json()
~~~~

<br>
**Resources** 

- You can use `dump` to write to a file as per this [Stack Overflow question](http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python).


<br>
##3. SQLite

We’ve learned to love SQLite recently and have found ourselves using it all the time. It’s worth picking up as it’s such an easy and great way of getting a persistent DB!

**Recent use to convert a CSV of movies to an `sqlite` DB:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/030/movies.py). 

<br>
**Resources**

- This [Python Cookbook chapter](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s08.html) details working with Relational Databases ([Amazon Link](http://amzn.to/2qMGNaN)).

- We enjoyed this thorough `sqlite` [Python tutorial](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html) by Sebastian Raschka too.


<br>
##4. XML

XML! The data format of choice for RSS feeds. Can be a bit troublesome at times but always worth the effort.

**Example of using `xml.etree.ElementTree` to parse the Safari RSS feed:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/017/safari.py) - Worth checking out the full code but the gist of it is…

~~~~
for item in doc.iterfind('channel/item'):
    ...
~~~~

<br>
**Using `feedparser` to pull specific XML tags and add to a list:**

[Code Link](https://github.com/pybites/100DaysOfCode/blob/master/045/xml_steam_scraper.py)

~~~~
feed = feedparser.parse(FEED_FILE)
    for entry in feed['entries']:
        Game = (entry['title'], entry['link'])
            games_list.append(Game)
~~~~

<br>
##Challenge Solutions

We’ve had numerous challenges over the past few months where the solutions involved these data formats. Here are a few of the noteworthy ones:

[Code Challenge 04](http://pybit.es/codechallenge04.html)

- [Read CSV](goo.gl/6gvF0b)

- [Write CSV](goo.gl/udmLRm)


<br>
[Code Challenge 07](http://pybit.es/codechallenge07.html)

- [Dump tweet JSON](goo.gl/lsv2MJ)

- [Load tweets](goo.gl/VjEukO)

[Code Challenge 17 Review](http://pybit.es/codechallenge17_review.html)

This was definitely a great challenge. Check out the multiple community contributions for some examples of using `sqlite` and XML in functional scripts written by your fellow Pythonistas.

<br>
##Learn By Doing

Now that you have the info, as we said in our [Learn By Doing article](http://pybit.es/learn-by-doing.html), open up a vim session and get coding!

One awesome, shameless plug of a way to do this would be to come up with a solution for [Code Challenge 19](http://pybit.es/codechallenge19.html). Playing with an API means you’ll more than likely need to use quite a few of these formats.

We’d love to hear if you have any Pythonic tips on using these formats too so leave a comment!

And as always, Keep Calm and Code in Python!

-- Julian and Bob

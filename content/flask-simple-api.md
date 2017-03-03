Title: How To Build a Simple API with Flask and Unit Test it
Date: 2017-03-03 20:00
Category: Concepts
Tags: API, Flask, REST, curl, testing, unittest, inventory
Slug: simple-flask-api
Authors: Bob
Summary: In this post I will create a simple API with Flask and test it, first manually with curl, then automatically with a set of unit tests.
cover: images/featured/pb-article.png

REST has gained lot of popularity and is virtually the default architectural style for designing and implementing RESTful web services. [Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer) states:

> Representational state transfer (REST) or RESTful Web services are one way of providing interoperability between computer systems on the Internet. REST-compliant Web services allow requesting systems to access and manipulate textual representations of Web resources using a uniform and predefined set of stateless operations.

Implementing REST APIs in Flask is relatively easy. As [this week's challenge](http://pybit.es/codechallenge08.html) is a House Inventory Tracker, lets do [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) on room items.

## Setup

First [create a virtualenv](http://pybit.es/the-beauty-of-virtualenv.html) and do pip install [Flask](http://flask.pocoo.org/).

## API code and endpoints

To create a simple API you basically implement the [HTTP methods](http://www.restapitutorial.com/lessons/httpmethods.html) you need, in this case GET, POST, PUT and DELETE, see the full code [here](https://github.com/pybites/blog_code/blob/master/flaskapi/app.py), I implemented the following endpoints:

	@app.route('/api/v1/items', methods=['GET'])
	@app.route('/api/v1/items/<int:id>', methods=['GET'])
	@app.route('/api/v1/items', methods=['POST'])
	@app.route('/api/v1/items/<int:id>', methods=['PUT'])
	@app.route('/api/v1/items/<int:id>', methods=['DELETE'])

## Testing part I) - manually with curl

How to test this? I first lazily put some curl commands in a [test script](https://github.com/pybites/blog_code/blob/master/flaskapi/curl.py), isn't it cool you can just use curl to test your new shiny API?

	$ python test.py

	# get items

	curl -i http://127.0.0.1:5000/api/v1/items
	HTTP/1.0 200 OK
	...

	{
	"items": [
		{
		"id": 1,
		"name": "laptop",
		"value": 1000
		},

	...

	# add item with proper values

	curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"monitor", "value": 200}' http://127.0.0.1:5000/api/v1/items
	HTTP/1.0 201 CREATED
	...

	{
		"item": {
			"id": 4,
			"name": "monitor",
			"value": 200
		}
	}
	...

However you have to read the output every time you test. Not cool :(

## Testing part II) - automation with unittest

Here the whole exercise became pretty interesting, how to test an API?! 

Flask makes this pretty easy with the test_client() method you can use in your setUp:

> test_client(use_cookies=True, **kwargs)
> 
> Creates a test client for this application. For information about unit testing head over to [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/).

You can test response codes and of course see how the data (list of items in this case) changes after each request. The only challenge was the isolation of each unit test: I had to do copy the app.items to a backup variable in setUp (a [deepcopy](https://docs.python.org/3.6/library/copy.html) to not leave references around) and pass it back in tearDown. The unit tests are [here](https://github.com/pybites/blog_code/blob/master/flaskapi/test_app.py).

This whole exercise took me some time and it was great learning, not something you get from just reading about it!

## next(API)

Since listening to [Soft Skills](https://www.manning.com/books/soft-skills) I want to do some time logging to increase my productivity. 

What if I can have a simple API where I can send log entries of 'start time - stop time - activity' via a POST request, and retrieve the data with GET for reporting?

Then deploy it somewhere (Heroku?) and set up a [webhook in Slack](https://api.slack.com/custom-integrations/outgoing-webhooks) to just input the entries in a dedicated channel and automatically log them to a back-end via the API. 

At the time of writing this article I stumbled upon [Flask-RESTful](http://flask-restful-cn.readthedocs.io/en/0.3.5/quickstart.html#a-minimal-api) and this morning I saw an article on [Google Spreadsheets and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) which might be cool to use for this ... stay tuned for a part II article ...

---

## Further reading

Apart from the Flask documentation / links above, Miguel Grinberg has a lot of excellent material on Flask including his [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask), recommended.

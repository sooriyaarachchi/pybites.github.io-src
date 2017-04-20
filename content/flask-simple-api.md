Title: How To Build a Simple API with Flask and Unit Test it
Date: 2017-03-03 21:00
Category: Flask
Tags: APIs, Flask, REST, curl, testing, unittest, inventory
Slug: simple-flask-api
Authors: Bob
Summary: In this post I will create a simple API with Flask and test it with curl and unit testing its HTTP methods.
cover: images/featured/pb-article.png

REST has gained lot of popularity and is virtually the default architectural style for designing and implementing RESTful web services. [Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer) states:

> Representational state transfer (REST) or RESTful Web services are one way of providing interoperability between computer systems on the Internet. REST-compliant Web services allow requesting systems to access and manipulate textual representations of Web resources using a uniform and predefined set of stateless operations.

Implementing REST APIs in Flask is relatively easy. As [this week's challenge](http://pybit.es/codechallenge08.html) is a House Inventory Tracker, lets do [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) on room items.

Note this post uses the simplest possible example, and focuses on the testing. I use an in-memory list for storage. In real life you probably want a DB, although you could also use a [Google Spreadsheet and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html). Security / authentication is critical too, see Miguel Grinberg's excellent [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) how to implement that.

## Get ready

First [create a virtualenv](http://pybit.es/the-beauty-of-virtualenv.html) and do pip install flask

## API code and endpoints

To create a simple API you implement one or more [HTTP methods](http://www.restapitutorial.com/lessons/httpmethods.html), in this case the following endpoints:

	@app.route('/api/v1.0/items', methods=['GET'])
	@app.route('/api/v1.0/items/<int:id>', methods=['GET'])
	@app.route('/api/v1.0/items', methods=['POST'])
	@app.route('/api/v1.0/items/<int:id>', methods=['PUT'])
	@app.route('/api/v1.0/items/<int:id>', methods=['DELETE'])

Full code [here](https://github.com/pybites/blog_code/blob/master/flaskapi/app.py). 

## Testing part I) - manually with curl

I first put some curl commands in a [test script](https://github.com/pybites/blog_code/blob/master/flaskapi/curl.py), isn't it cool you can just use curl to test your new shiny API?

	$ python curl.py

	# get items

	curl -i http://127.0.0.1:5000/api/v1.0/items
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
	...

	# add item with proper values

	curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"monitor", "value": 200}' http://127.0.0.1:5000/api/v1.0/items
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
	...

It surely is! However you have to read the output every time you test. Not cool :(

## Testing part II) - automation with unittest

Here the whole exercise became pretty interesting, how to unit test an API?! 

Flask facilitates a nice method you can use in your setUp (= repeats for each unit test):

> test_client(use_cookies=True, **kwargs)
> 
> Creates a test client for this application. For information about unit testing head over to [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/).

You can test response codes and of course see how the data (list of items in this case) changes after each request. 

The only challenge was the isolation of each unit test: I had to do copy the app.items to a backup variable in setUp (a [deepcopy](https://docs.python.org/3.6/library/copy.html) to not leave references around) and pass it back in tearDown. Similarly for a DB back-end you would probably construct and drop a test table to have a clean slate for every test. 

The full unit tests are [here](https://github.com/pybites/blog_code/blob/master/flaskapi/test_app.py), summary:

	def test_get_all(self): ...
	def test_get_one(self): ...
	def test_item_not_exist(self): ...
	def test_post(self): ...
	def test_update(self): ...
	def test_update_error(self): ...
	def test_delete(self): ...

This whole exercise took me some time but it was great learning, not something you get from just reading about it! And this can serve as a template when testing other APIs.

## next(API)

Since listening to [Soft Skills](https://www.manning.com/books/soft-skills) I want to do some time logging to increase my productivity. 

What if I can have a simple API where I can send log entries of 'deep work time x spent on activity y' via a [Slack Webhook](https://api.slack.com/custom-integrations/outgoing-webhooks) to a DB or earlier mentioned Google Spreadsheet?

At the time of writing this article I stumbled upon [Flask-RESTful](http://flask-restful-cn.readthedocs.io/en/0.3.5/quickstart.html#a-minimal-api) which should make this even easier (more elegant). So stay tuned for a part II ...

---

Keep Calm and Code in Python!

-- Bob

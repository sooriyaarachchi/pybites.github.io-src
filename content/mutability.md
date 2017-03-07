Title: Don't let mutability of compound objects fool you!
Date: 2017-03-07 11:00
Category: Concepts
Tags: list, mutable, copy, deepcopy
Slug: mutability
Authors: Bob
Summary: In this article I explain the difference between shallow versus deep copy with a working example. It's an important concept when working with compound objects.
cover: images/featured/pb-article.png

In this post I wanted to expand a bit on mutability. As already indicated [here](http://pybit.es/py-mistakes.html) and [here](http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments) using mutable default values for methods gets you into trouble. 

Last week I had a similar issue with mutability when writing test code for [our simple Flask API post](http://pybit.es/simple-flask-api.html):

> The only challenge was the isolation of each unit test: I had to do copy the app.items to a backup variable in setUp (a deepcopy to not leave references around) and pass it back in tearDown. ...

It is important to become familiar with shallow vs deep copy when dealing with compound (nested) objects!

The [documentation](https://docs.python.org/3.6/library/copy.html) explains it well: 

> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
> 
> * A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
> * A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original

In our API exercise app.items was a list of dicts, so I needed deepcopy:

	def setUp(self):
        self.backup_items = deepcopy(app.items)  
		...

	...

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items

I even ended up adding a test in [the *test_update* method](https://github.com/pybites/blog_code/blob/master/flaskapi/test_app.py) to make sure the backup did not get corrupted:

	..
	..
	self.assertEqual(data['item']['value'], 30)
	# proof need for deepcopy in setUp: update app.items should not affect self.backup_items
	# this fails when you use shallow copy
	self.assertEqual(self.backup_items[2]['value'], 20)  # 20 == org value

See REPL output to clarify this further: 

	>>> items = [
	...     {
	...         'id': 1,
	...         'name': 'laptop',
	...         'value': 1000
	...     },
	...     {
	...         'id': 2,
	...         'name': 'chair',
	...         'value': 300,
	...     },
	...     {
	...         'id': 3,
	...         'name': 'book',
	...         'value': 20,
	...     },
	... ]

	>>> items
	[{'id': 1, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items2 = items[:]  # shallow copy
	>>> items2
	[{'id': 1, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items2 == items
	True

	>>> items[0]['id'] = 5
	# oops the items2 copy got updated as well!
	# -> id of first item got corrupted (5 != 1)

	>>> items2 == items
	True 

	>>> items2  
	[{'id': 5, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items
	[{'id': 5, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]

	# same for copying with list constructor, another shallow copy it turns out
	>>> items2 = list(items)
	>>> items2 == items
	True

	>>> items
	[{'id': 5, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items2
	[{'id': 5, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]

	>>> items[0]['id'] = 6

	# oops
	>>> items2 == items
	True

	# again both data structures' first item were updated
	>>> items
	[{'id': 6, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items2
	[{'id': 6, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	
	# now the right way
	>>> from copy import deepcopy
	>>> items2 = deepcopy(items)
	>>> items == items2
	True
	>>> items[0]['id'] = 7

	# cool
	>>> items == items2
	False
	
	# backup items2 intact
	>>> items
	[{'id': 7, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]
	>>> items2
	[{'id': 6, 'name': 'laptop', 'value': 1000}, {'id': 2, 'name': 'chair', 'value': 300}, {'id': 3, 'name': 'book', 'value': 20}]i

See another example taken from [Fluent Python](http://amzn.to/2lxsmBg) shown on [this Reddit thread](https://redd.it/5xqwa8) which inspired me to write this up. 

I hope this saves some of you Python developers a debugging headache some day :)

---

Keep Calm and Code in Python!

-- Bob

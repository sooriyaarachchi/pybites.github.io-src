Title: All You Need to Know to Start Using Fixtures in Your pytest Code
Date: 2018-03-15 13:00
Category: Testing
Tags: pytest, fixtures, testing, refactoring, pytest-cov, coverage
Slug: pytest-fixtures
Authors: Bob
Summary: Setting up test cases for code that manage data can be challenging but it's an important skill to reliably test your code. You might have heard of the setup and teardown methods in `unittest`. In `pytest` you use _fixtures_ and as you will discover in this article they are actually not that hard to set up. Fixtures have been labelled _pytest's killer feature_ so let's explore them in this article using a practical example.
cover: images/featured/pb-article.png

Setting up test cases for code that manage data can be challenging but it's an important skill to reliably test your code. You might have heard of the setup and teardown methods in `unittest`. In `pytest` you use _fixtures_ and as you will discover in this article they are actually not that hard to set up. Fixtures have been labelled _pytest's killer feature_ so let's explore them in this article using a practical example.

> pytest fixtures ... are the reason why many people switch to and stay with pytest. ... one of the great reasons to use fixtures: to focus the test on what you’re actually testing, not on what you had to do to get ready for the test. - Brian Okken's [Python testing with pytest](https://pybit.es/pytest-book.html)

## Why do you want fixtures?

If your tests need to work on data you typically need to set them up. This is often a process that has to be repeated and independent for each test. This often leads to duplicate code which is "number one in the stink parade" ([Kent Beck and Martin Fowler](https://www.safaribooksonline.com/library/view/building-maintainable-software/9781491955987/ch04.html)).

The `@pytest.fixture` decorator provides an easy yet powerful way to setup and teardown resources. You can then pass these defined fixture objects into your test functions as input arguments.

You want each test to be independent, something that you can enforce by [running your tests in random order](https://twitter.com/tarek_ziade/status/973848758227173376).

 Fixtures are also referred to as dependency injections which you can read more about [here](https://en.wikipedia.org/wiki/Dependency_injection). Let's look at some actual code next.

## An example - working with databases

This is a common scenario. In my guest article [Building a Simple Web App With Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/blog/python/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/) I used a small DB app and pytest for testing. I defined a fixture to make a fresh DB with some test tweets for every test:

	@pytest.fixture()
	def db_setup(request):

		tweets = list(_gen_tweets())
		import_tweets(tweets)
		import_hashtags()

		def fin():
			truncate_tables()

		request.addfinalizer(fin)


A couple of things to notice here:

* You define a fixture with a function wrapping it into the `@pytest.fixture()` decorator

* You probably want some static data to work with, here `_gen_tweets` loaded in a _tweets.json_ file

* To define a teardown use the `def fin(): ...` + `request.addfinalizer(fin)` construct to do the required cleanup after each test. You can also use `yield` (see [pytest docs](https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code)).

Then to use this fixture on the test methods we can just pass it in as function argument:

	def test_get_tips(db_setup):
		...


	def test_add_tips(db_setup):
		...


	def test_get_hashtags(db_setup):
		...


	def test_add_hashtags(db_setup):
		...

You can access this code [here](https://github.com/pybites/pytip/blob/master/tests/test_tips.py).

## Second example - a groceries cart

I prepared a second example for this article. Here is a `Groceries` class (final code examples are [here](https://github.com/pybites/blog_code/tree/master/pytest/fixtures)). It lets you manage a list of items. Each `Item` is a `namedtuple` of product (name), price and a craving `bool`. The `DuplicateProduct` and `MaxCravingsReached` exceptions are used to control the data added and the amount of sugary foods I try to buy 😂

	from collections import namedtuple

	MAX_CRAVINGS = 2

	Item = namedtuple('Item', 'product price craving')


	class DuplicateProduct(Exception):
		pass


	class MaxCravingsReached(Exception):
		pass


	class Groceries:

		def __init__(self, items=None):
			"""This cart can be instantiated with a list of namedtuple
			items, if not provided use an empty list"""
			self._items = items if items is not None else []

		def show(self):
			"""Print a simple table of cart items with total at the end"""
			for item in self._items:
				product = f'{item.product}'
				if item.craving:
					product += ' (craving)'
				print(f'{product:<30} | {item.price:>3}')
			print('-' * 36)
			print(f'{"Total":<30} | {self.due:>3}')

		def add(self, new_item):
			"""Add a new item to cart, raise exceptions if item already in
			cart, or when we exceed MAX_CRAVINGS"""
			if any(item for item in self if item.product == new_item.product):
				raise DuplicateProduct(f'{new_item.product} already in items')
			if new_item.craving and self.num_cravings_reached:
				raise MaxCravingsReached(f'{MAX_CRAVINGS} allowed')
			self._items.append(new_item)

		def delete(self, product):
			"""Delete item matching 'product', raises IndexError
			if no item matches"""
			for i, item in enumerate(self):
				if item.product == product:
					self._items.pop(i)
					break
			else:
				raise IndexError(f'{product} not in cart')

		def search(self, search):
			"""Case insensitive 'contains' search, this is a
			generator returning matching Item namedtuples"""
			for item in self:
				if search.lower() in item.product:
					yield item

		@property
		def due(self):
			"""Calculate total due value of cart"""
			return sum(item.price for item in self)

		@property
		def num_cravings_reached(self):
			"""Checks if I have too many cravings in my cart """
			return len([item for item in self if item.craving]) >= MAX_CRAVINGS

		def __len__(self):
			"""The len of cart"""
			return len(self._items)

		def __getitem__(self, index):
			"""Making the class iterable (cart = Groceries() -> cart[1] etc)
			without this dunder I would get 'TypeError: 'Cart' object does
			not support indexing' when trying to index it"""
			return self._items[index]


Some non-pytest related things to notice here:

* It supports _show_/_add_/_delete_, I left the _update_ method out for now. I did leave the _search_ method in though (to show `@pytest.mark.parametrize` later)

* The convenient use of [properties](https://pybit.es/property-decorator.html)

* Using \_\_len\_\_ and \_\_getitem\_\_ to make the class _iterable_ (we discussed _dunder methods_ in depth in [this guest article](https://dbader.org/blog/python-dunder-methods)). Thanks to this Groceries now supports _indexing_ for example (_slicing_ would work too). So when I later instantiate a `cart` object from it, I can do `cart[0].product` instead of `cart._items[0].product`, etc.

## Initial tests for Groceries

And here is the initial set of tests I wrote for this class:

	import re

	import pytest

	from groceries import (Groceries, Item, DuplicateProduct,
						MaxCravingsReached)


	def _setup_items():
		products = 'celery apples water coffee chicken pizza'.split()
		prices = [1, 4, 2, 5, 6, 4]
		cravings = False, False, False, False, False, True
		for item in zip(products, prices, cravings):
			yield Item(*item)


	def test_initial_empty_cart():
		cart = Groceries()

		assert len(cart) == 0
		assert cart.due == 0


	def test_initial_filled_cart():
		items = list(_setup_items())
		cart = Groceries(items=items)

		# thanks to __getitem__ can index the cart
		assert cart[0].product == 'celery'
		assert cart[0].price == 1
		assert cart[-1].product == 'pizza'
		assert cart[-1].price == 4

		assert len(cart) == 6
		assert cart.due == 22
		assert not cart.num_cravings_reached


	def test_add_item():
		items = list(_setup_items())
		cart = Groceries(items=items)

		oranges = Item(product='oranges', price=3, craving=False)
		cart.add(oranges)

		assert len(cart) == 7
		assert cart[-1].product == 'oranges'
		assert cart[-1].price == 3
		assert cart.due == 25
		assert not cart.num_cravings_reached


	def test_add_item_duplicate():
		items = list(_setup_items())
		cart = Groceries(items=items)

		apples = Item(product='apples', price=4, craving=False)
		with pytest.raises(DuplicateProduct):
			cart.add(apples)


	def test_add_item_max_cravings():
		items = list(_setup_items())
		cart = Groceries(items=items)

		chocolate = Item(product='chocolate', price=2, craving=True)
		cart.add(chocolate)
		assert cart.num_cravings_reached

		croissants = Item(product='croissants', price=3, craving=True)
		with pytest.raises(MaxCravingsReached):
			cart.add(croissants)  # wait till next week!


	def test_delete_item():
		items = list(_setup_items())
		cart = Groceries(items=items)

		# not in collection
		croissant = 'croissant'
		with pytest.raises(IndexError):
			cart.delete(croissant)

		# in collection
		assert len(cart) == 6
		apples = 'apples'
		cart.delete(apples)
		# new product at this index
		assert len(cart) == 5
		assert cart[1].product == 'water'


	@pytest.mark.parametrize("test_input,expected", [
		('banana', 0),
		('water', 1),
		('Apples', 1),
		('apple', 1),
		('le', 2),
		('zZ', 1),
		('e', 5),
	])
	def test_search_item(test_input, expected):
		items = list(_setup_items())
		cart = Groceries(items=items)

		assert len(list(cart.search(test_input))) == expected


	def test_show_items(capfd):
		items = list(_setup_items())
		cart = Groceries(items=items)

		cart.show()
		output = [line for line in capfd.readouterr()[0].split('\n')
				if line.strip()]

		assert re.search(r'^celery.*1$', output[0])
		assert re.search(r'^pizza \(craving\).*4$', output[5])
		assert re.search(r'^Total.*22$', output[-1])


Things to notice:

* Right off the bat you see that annoying setup repetition in each test: `cart = Groceries`! We will tackle this shortly.

* Here are some other nice pytest features I am using a lot lately:

	* To test an exception (`DuplicateProduct` and `MaxCravingsReached` here) you can use this construct:

			with pytest.raises(Exception):
				run code that triggers the Exception

	* `@pytest.mark.parametrize` to run a test with a different set of _input_ and _expected_ values. This addresses the same need to keep your code slim avoiding duplication.

	* to consume the _stdout_ of your program you can pass in the _capfd_ input parameter to your test function and accessing its `readouterr` method. I use it in `test_show_ output` to test the groceries report output. Actually as I was writing this article I discovered that `capfd` is actually a _fixture_ itself, you can see this when you run `pytest --fixtures`:

			...
			...
			capfd
			Enable capturing of writes to file descriptors 1 and 2 and make
			captured output available via ``capfd.readouterr()`` method calls
			which return a ``(out, err)`` tuple.  ``out`` and ``err`` will be ``text``
			objects.

## Coverage

I am making a habit of using [pytest-cov](https://pypi.python.org/pypi/pytest-cov) to see my test coverage:

	(pytest) [bbelderb@macbook fixtures (master)]$ pytest --cov-report term-missing --cov='.'
	============================================= test session starts ==============================================
	platform darwin -- Python 3.6.1, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
	rootdir: /Users/bbelderb/code/pybites_code/pytest/fixtures, inifile:
	plugins: cov-2.5.1
	collected 14 items

	test_groceries.py ..............                                                                         [100%]

	---------- coverage: platform darwin, python 3.6.1-final-0 -----------
	Name                Stmts   Miss  Cover   Missing
	-------------------------------------------------
	groceries.py           42      0   100%
	test_groceries.py      71      0   100%
	-------------------------------------------------
	TOTAL                 113      0   100%


	========================================== 14 passed in 0.34 seconds ===========================================

As I run this over and over again I added this alias to my `.vimrc` so I can run this from my test file pressing `,t`:

	nmap ,t :w<CR>:!pytest -s --cov-report term-missing --cov='.'<CR>

(if you don't want to see stdout from your tests drop the _-s_)

## Let's refactor this using a fixture

As we saw the setup code of the Groceries gets repeated over and over again. Let's wrap it in a fixture:

	@pytest.fixture
	def cart():
		"""Setup code to create a groceries cart object with 6 items in it"""
		products = 'celery apples water coffee chicken pizza'.split()
		prices = [1, 4, 2, 5, 6, 4]
		cravings = False, False, False, False, False, True

		items = []
		for item in zip(products, prices, cravings):
			items.append(Item(*item))

		return Groceries(items)

To use it I need to add it as input argument to each test function that uses it:

	$ grep ^def test_groceries.py
	def cart():
	def test_initial_empty_cart():
	def test_initial_filled_cart(cart):
	def test_add_item(cart):
	def test_add_item_duplicate(cart):
	def test_add_item_max_cravings(cart):
	def test_delete_item(cart):
	def test_search_item(cart, test_input, expected):
	def test_show_items(cart, capfd):


Note that:

* In the first test I left the `Groceries` instantiation in because I wanted to create it with an empty `items` list (you can probably parametrize the fixture but this will do for now).

* In the tests that use other arguments like `@pytest.mark.parametrize` and `capfd` (in `test_search_item` and `test_show_items` respectively), the fixture argument comes first!

And now I can ditch these lines of code which were duplicated multiple times:

	items = list(_setup_items())
	cart = Groceries(items=items)

Let's run the tests again:

	(pytest) [bbelderb@macbook fixtures (master)]$ pytest --cov-report term-missing --cov='.'
	============================================= test session starts ==============================================
	platform darwin -- Python 3.6.1, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
	Using --random-order-bucket=module
	Using --random-order-seed=270491

	rootdir: /Users/bbelderb/code/pybites_code/pytest/fixtures, inifile:
	plugins: random-order-0.5.4, cov-2.5.1
	collected 14 items

	test_groceries.py ..............                                                                         [100%]

	---------- coverage: platform darwin, python 3.6.1-final-0 -----------
	Name                Stmts   Miss  Cover   Missing
	-------------------------------------------------
	groceries.py           42      0   100%
	test_groceries.py      59      0   100%
	-------------------------------------------------
	TOTAL                 101      0   100%


	========================================== 14 passed in 0.14 seconds ===========================================

Nice: 12 lines of test code less!

I only covered the basics so far. However this should get you started using fixtures in your tests. Next I will highlight 2 more features of fixtures.

## Define a scope of a fixture

How to share your fixture across tests in a class, module or session?

In our example the setup is super fast so it is not really needed. But what if your setup code deals with a lot of data or has a costly network connection dependency? To simulate this let's add a `sleep(1)` to our `cart` fixture to see what happens:

	from time import sleep
	...

	@pytest.fixture
	def cart():
  		"""Setup code to create a groceries cart object with 6 items in it"""
  		sleep(1)
		...

	$ pytest
	...
	14 passed in 13.15 seconds

Oops ... it slept upon each test function! That is because a fixture's scope is set to _function_ by default. To run the fixture once per module add `scope="module"` to the `@pytest.fixture` decorator (or `scope="session"` as we will see later on). Let's compare:

	@pytest.fixture(scope="module")
	def cart():
  		"""Setup code to create a groceries cart object with 6 items in it"""
  		sleep(1)
		...

	$ pytest
	...
	6 failed, 8 passed in 1.21 seconds
	$ pytest
	...
	3 failed, 11 passed in 1.17 seconds

What happened?! The timing is right, there is a sleep of 1 second, but I introduced random test failures! The tests became tainted because it changed the same mutable `cart` object in various tests, not resetting it back to its initial state (like it did when scope was _function_).

So use this with caution. In this case we should just use the default _function_ scope because the setup is very fast (`14 passed in 0.14 seconds` remember?). But to further demo the _scope_ feature let's make this example work.

In this case I just make a copy of the `cart` object where I am going to  manipulate it. I am using `deepcopy` because this is a nested data structure (learn more why you want this [here](https://pybit.es/mutability.html)). It was only in 3 places:

	$ grep -B1 deepcopy test_groceries.py
	...
	from copy import deepcopy
	--
	def test_add_item(cart):
		cart = deepcopy(cart)  # not needed if scope > function (module/session)
	--
	def test_add_item_max_cravings(cart):
		cart = deepcopy(cart)
	--
	def test_delete_item(cart):
		cart = deepcopy(cart)

And it works again:

	$ pytest
	...
	14 passed in 1.10 seconds

## Re-use fixtures in various test files

The second and last feature I want to highlight. You can add fixtures to a predefined file called `conftest.py`. Fixtures in this file will be automatically discovered upon running pytest, no import needed.

Let's do an experiment: let's move the tests that make changes to the `cart` object into `test_edit_cart.py` and the ones that don't into `test_view_cart.py`. We will need the fixture for both test files so I am moving it into `conftest.py`. The code looks more modular now:

[conftest.py](https://github.com/pybites/blog_code/blob/master/pytest/fixtures/conftest.py)

	from time import sleep

	import pytest

	from groceries import Groceries, Item


	@pytest.fixture(scope="module")
	def cart():
		"""Setup code to create a groceries cart object with 6 items in it"""
		print('sleeping a bit at session level')
		sleep(1)  # for scope=module/session demo purposes
		products = 'celery apples water coffee chicken pizza'.split()
		prices = [1, 4, 2, 5, 6, 4]
		cravings = False, False, False, False, False, True

		items = []
		for item in zip(products, prices, cravings):
			items.append(Item(*item))

		return Groceries(items)

[test_view_cart.py](https://github.com/pybites/blog_code/blob/master/pytest/fixtures/test_view_cart.py)

	import re

	import pytest

	from groceries import Groceries


	def test_initial_empty_cart():
	    """Note no fixture here to test an empty cart creation"""
	    cart = Groceries()
	    assert len(cart) == 0
	    assert cart.due == 0


	def test_initial_filled_cart(cart):
	    # thanks to __getitem__ can index the cart
	    assert cart[0].product == 'celery'
	    assert cart[0].price == 1
	    assert cart[-1].product == 'pizza'
	    assert cart[-1].price == 4

	    assert len(cart) == 6
	    assert cart.due == 22
	    assert not cart.num_cravings_reached


	@pytest.mark.parametrize("test_input,expected", [
	    ('banana', 0),
	    ('water', 1),
	    ('Apples', 1),
	    ('apple', 1),
	    ('le', 2),
	    ('zZ', 1),
	    ('e', 5),
	])
	def test_search_item(cart, test_input, expected):
	    assert len(list(cart.search(test_input))) == expected


	def test_show_items(cart, capfd):
	    cart.show()
	    output = [line for line in capfd.readouterr()[0].split('\n')
	              if line.strip()]

	    assert re.search(r'^celery.*1$', output[0])
	    assert re.search(r'^pizza \(craving\).*4$', output[5])
	    assert re.search(r'^Total.*22$', output[-1])


[test_edit_cart.py](https://github.com/pybites/blog_code/blob/master/pytest/fixtures/test_edit_cart.py)

	from copy import deepcopy

	import pytest

	from groceries import Item, DuplicateProduct, MaxCravingsReached


	def test_add_item(cart):
	    cart = deepcopy(cart)  # not needed if scope=function

	    oranges = Item(product='oranges', price=3, craving=False)
	    cart.add(oranges)

	    assert len(cart) == 7
	    assert cart[-1].product == 'oranges'
	    assert cart[-1].price == 3
	    assert cart.due == 25
	    assert not cart.num_cravings_reached


	def test_add_item_max_cravings(cart):
	    cart = deepcopy(cart)
	    chocolate = Item(product='chocolate', price=2, craving=True)
	    cart.add(chocolate)
	    assert cart.num_cravings_reached

	    croissants = Item(product='croissants', price=3, craving=True)
	    with pytest.raises(MaxCravingsReached):
	        cart.add(croissants)  # wait till next week!


	def test_add_item_duplicate(cart):
	    apples = Item(product='apples', price=4, craving=False)
	    with pytest.raises(DuplicateProduct):
	        cart.add(apples)


	def test_delete_item(cart):
	    cart = deepcopy(cart)
	    # not in collection
	    croissant = 'croissant'
	    with pytest.raises(IndexError):
	        cart.delete(croissant)

	    # in collection
	    assert len(cart) == 6
	    apples = 'apples'
	    cart.delete(apples)
	    # new product at this index
	    assert len(cart) == 5
	    assert cart[1].product == 'water'


And let's run the tests again:

	$ pytest
	================================================ test session starts ================================================
	platform darwin -- Python 3.6.1, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
	Using --random-order-bucket=module
	Using --random-order-seed=885306

	rootdir: /Users/bbelderb/code/pybites_code/pytest/fixtures, inifile:
	plugins: random-order-0.5.4, cov-2.5.1
	collected 14 items

	test_edit_cart.py ...                                                                                         [ 21%]
	test_view_cart.py ...........                                                                                 [100%]

	============================================= 14 passed in 2.12 seconds =============================================

Again note that I did not have to import `conftest.py`, nice!

But wait, the `sleep` ran twice this time, because the scope was still defined as _module_ (meaning _file_). Let's change it to _session_ and check again:

	@pytest.fixture(scope="session")
	def cart():
	    """Setup code to create a groceries cart object with 6 items in it"""
	    print('sleeping a bit at session level')
	    sleep(1)  # for scope=module/session demo purposes

Running the tests now gives:

	(pytest) [bbelderb@macbook fixtures (master)]$ pytest
	================================================ test session starts ================================================
	platform darwin -- Python 3.6.1, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
	Using --random-order-bucket=module
	Using --random-order-seed=578283

	rootdir: /Users/bbelderb/code/pybites_code/pytest/fixtures, inifile:
	plugins: random-order-0.5.4, cov-2.5.1
	collected 14 items

	test_view_cart.py ...........                                                                                 [ 78%]
	test_edit_cart.py ...                                                                                         [100%]

	============================================= 14 passed in 1.13 seconds =============================================

Awesome!

## List all fixtures

Lastly I recommend adding docstrings to your fixtures so that they show up when somebody probes for them with the `--fixtures` flag:

	$ pytest --fixtures test_groceries.py
	...
	pytest's fixtures
	...
	...
	pytest_cov's fixtures
	...
	--------------------------------------- fixtures defined from test_groceries ----------------------------------------
	cart
		Setup code to create a groceries cart object with 6 items in it

## Resources

This should give you all you need to start using fixtures in your pytest code. You will save time, be more content and most importantly produce more robust test code!

There is more to fixtures though, checkout the well written [pytest docs](https://docs.pytest.org/en/latest/fixture.html). Also [Brian Okken's book](https://pybit.es/pytest-book.html) covers them extensively.

Let us know in the comments below if you came up with interesting use cases or you hit a wall?

You will see fixtures increasingly used in our [Bites of Py](http://codechalleng.es) test code and I am happy we covered it here now, because it is one of the things that makes pytest great!

---

Keep Calm and Code in Python!

-- Bob

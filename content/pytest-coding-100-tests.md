Title: Enough pytest to be Dangerous, 10 Things I Learned Writing Tests for 100 Python (Bites of Py) Exercises
Date: 2018-06-07 16:30
Category: Testing
Tags: pytest, learning, mock, parametrize, capfd, fixtures
Slug: pytest-coding-100-tests
Authors: Bob
Summary: We hit 100 Bite exercises on [our Code Platform](https://codechalleng.es/) and that means we have written tests for 100 exercises. In this article I share 10 things I learned about writing test code and pytest.
cover: images/featured/pb-article.png

We hit 100 Bite exercises on [our Code Platform](https://codechalleng.es/) and that means we have written tests for 100 exercises. In this article I share 10 things I learned about writing test code and pytest.

## 1. One thing, one test

When you write test code it is important to stick to general code best practices and that means: one function ideally does one thing. Shorter test functions means more focus and you can adequately name each test function which leads to better outputs, compare:
![too much in one function]({filename}/images/pytest-too-much-in-one-function.png)

to:
![one functon one thing to test, much better]({filename}/images/pytest-one-function-one-thing-better.png)

I rather see the latter.

## 2. Tests should be independent

A test should never depend on another test. This goes back to good design and decoupling functionality. Read up on [orthogonality](https://en.wikipedia.org/wiki/Orthogonality_(programming)), greatly explained in the [Pragmatic Programmer book](https://bobbelderbos.com/2011/02/great-book-about-software-engineering/).

## 3. Test for edge cases

In case you are looping through a sequence what are the boundaries? If my function throws an exception for bad input what are all scenarios that exception should be thrown and not. For example throwing a `ValueError` for a non numeric value, are we testing more than `str` and `int` types?

This is also a good way to document what your code is supposed to do. A good example of an edge case and added documentation was our addition of None checking in [Bite 1. Sum n numbers](https://codechalleng.es/bites/1/), look at the last line of `test_sum_numbers_various_inputs`:

		from numbers import sum_numbers


		def test_sum_numbers_default_args():
			assert sum_numbers() == 5050
			assert sum_numbers(numbers=None) == 5050


		def test_sum_numbers_various_inputs():
			assert sum_numbers(range(1, 11)) == 55
			assert sum_numbers([1, 2, 3]) == 6
			assert sum_numbers((1, 2, 3)) == 6
			assert sum_numbers([]) == 0  # !! [] not the same as None

This was one of our first tests, `assert sum_numbers([])` could actually go into its own test function, because it handles a separate test case!

## 4. Mocking and performance

If you call an external service you probably want to [mock it out](https://pybit.es/tag/mock.html). But use mocking with caution, it might drive you away from testing the real thing (anti-pattern). Also in our case beginner Pythonistas need to understand the test code and this can make things more confusing.

But for some code it's inevitable, for example random outputs, you can use the patch decorator to mock out random behavior:

		from unittest.mock import patch

		@patch.object(random, 'randint')
		def test_get_random_number(m):
			m.return_value = 17
			assert get_random_number() == 17


Apart from controlling external resources we want tests to be fast and mocking out an external API call speeds up tests.

You will run your test suite over and over again so non performant tests slow down your development.

On our platform we run the tests via AWS lambda which performs a bunch of additional tasks like picking up the submitted code and test file. And we have a user waiting for a pass/fail response. More reasons for the test code to be performant.

In this context you also want to abstract common code into setup/teardown code, which pytest offers via _fixtures_  (see more under 8). For some Bites we needed to pull in an input text file (AWS Lambda runs in its own sandbox). This is an example of something you'd make sure you do once for a set of tests. 

## 5. Test coverage

Since teaching a lesson on pytest in our [100 Days of Code course](https://talkpython.fm/100days?s=pybites) I discovered [_coverage_](https://pypi.org/project/pytest-cov/) and made this alias in my _.vimrc_ to simply check it with one keystroke:

		nmap ,t :w<CR>:!pytest -s --cov-report term-missing --cov='.'<CR>

You have to install this plugin for it to work:

		# enable venv (TODO: switch to pipenv)
		$ pip install pytest-cov

Our Bites are small so it might be overkill but it's good practice to use this tool:

![check coverage with one keystroke]({filename}/images/pytest-test-coverage.png)

---

OK next the pytest specific things I learned:

## 6. Why pytest is our framework of choice

To recap what we wrote in our review of [Brian Okken](https://twitter.com/brianokken)'s [awesome book on pytest](https://pybit.es/pytest-book.html), what are wins of pytest over the builtin unittest framework?

Answer: it's less verbose (assert vs. self.assertEqual etc.) / classes are not required, it as a rich cli interface, informative test failures, a more convenient way to write setup/teardown functions with fixtures, parameterized tests, and a better test runner (marker- and name-based test selection).

## 7. Reading pytest output (and _Bites of Py_ validation at its core)

Our [_Bites of Py_](https://codechalleng.es/bites/) endorses reading test code output.

It's our way to lead programmers to get their code to work. It might mean some extra effort for newer coders but the pay off is huge, as somebody said:

> The gold of your solution is in the tests

... and we concur:

* as a developer you are going to read way more code than write!

* as a developer you will write vast amounts of test code to verify your code and maybe even drive its design (TDD),

* running tests makes you better understand what your code does and is supposed to do,

* test failure output might require some debugging what/where it went wrong and debugging is another crucial programmer skill.

Hence why coding on our platform requires becoming friends with reading test outputs.

Luckily that's also an area where pytest really shines: it's output is very intuitive!

Let's look at a practical example: [Bite 5. Parse a list of names](https://codechalleng.es/bites/5), and let me only focus on the first function (the Bite has 3). Note you would probably write more code between each step, but just to show how the tests may guide you:

Running the template code without adding any code it shows:

Code:

		NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
				'julian sequeira', 'sandra bullock', 'keanu reeves',
				'julbob pybites', 'bob belderbos', 'julian sequeira',
				'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

		def dedup_and_title_case_names(names):
			"""Should return a list of names, each name appears only once"""
			pass

Test output:

		=================================== FAILURES ===================================
		_______________________ test_dedup_and_title_case_names ________________________

			def test_dedup_and_title_case_names():
				names = dedup_and_title_case_names(NAMES)
		>       assert names.count('Bob Belderbos') == 1
		E       AttributeError: 'NoneType' object has no attribute 'count'

		/tmp/test_names.py:7: AttributeError
		...
		...
		output for other tests - note how a test per function makes it easier to focus on one thing at a time!
		...
		...

`dedup_and_title_case_names` does not return anything, let's return the `NAMES` list (as passed in as argument):

Code:

		def dedup_and_title_case_names(names):
			"""Should return a list of names, each name appears only once"""
			return names

Test output:

		=================================== FAILURES ===================================
		_______________________ test_dedup_and_title_case_names ________________________

			def test_dedup_and_title_case_names():
				names = dedup_and_title_case_names(NAMES)
		>       assert names.count('Bob Belderbos') == 1
		E       AssertionError: assert 0 == 1

OK now I don't assert the amount of names and that is because the original `NAMES` list passed in is still lowercase:

So let's address that next in `dedup_and_title_case_names`:

Code:

		def dedup_and_title_case_names(names):
			"""Should return a list of names, each name appears only once"""
			return [name.title() for name in NAMES]

Test output:

		=================================== FAILURES ===================================
		_______________________ test_dedup_and_title_case_names ________________________

			def test_dedup_and_title_case_names():
				names = dedup_and_title_case_names(NAMES)
		>       assert names.count('Bob Belderbos') == 1
		E       AssertionError: assert 2 == 1

OK so I have my name in there twice, should be once, let's make have the list only contain unique values using a set:

Code:

		def dedup_and_title_case_names(names):
			"""Should return a list of names, each name appears only once"""
			return {name.title() for name in NAMES}

Test output:

		=================================== FAILURES ===================================
		_______________________ test_dedup_and_title_case_names ________________________

			def test_dedup_and_title_case_names():
				names = dedup_and_title_case_names(NAMES)
		>       assert names.count('Bob Belderbos') == 1
		E       AttributeError: 'set' object has no attribute 'count'

Oops! That's right, the docstring already said it should return a list, fair enough:

		def dedup_and_title_case_names(names):
			"""Should return a list of names, each name appears only once"""
			return list({name.title() for name in NAMES})

That works, I have a pass (dot) and the test is not under `FAILURES` anymore:

		../../tmp/test_names.py .FF

		... other 2 tests still to pass for the other 2 functions for this Bite ...

We think teaching people how to read test code is win/win, but for that it's important to write isolated tests (see 1. and 2.) and have intuitive failure outputs, which pytest nails.

## 8. Fixtures are your friend!

To quote from Brian's book:

> pytest fixtures ... are the reason why many people switch to and stay with pytest. ... one of the great reasons to use fixtures: to focus the test on what you’re actually testing, not on what you had to do to get ready for the test.

Teaching pytest in our [100 Days of Code course](https://talkpython.fm/100days?s=pybites), I got to the end of +/- 40 min dense video section without addressing them (WTF?). So I wrote [this article about fixtures](https://pybit.es/pytest-fixtures.html).

Fixtures are awesome, basically any time you want to do some (repetitive) setup/teardown for a (set of) tests you want to use them.

In [Bite 99. Write an infinite sequence generator](https://codechalleng.es/bites/99/) for example we test a sequence generator and we want a fresh instance before each test ... easy:

	@pytest.fixture
	def gen():
		"""Return a fresh new generator object for each test"""
		return sequence_generator()

You can then access this fixture by passing it as argument to the test functions:

		def test_first_ten_first_round(gen):
			...
		def test_first_ten_second_round(gen):
			...
		def test_last_ten_third_round(gen):
			...

If you want to share the generator between tests, you can just give it a scope argument:

	@pytest.fixture
	def gen(scope="module"):
		"""Return a fresh new generator object for each test"""
		return sequence_generator()

You probably don't want to do that for this code (remember: make tests independent), but you could have database setup code that persists across a bunch of tests for example.

## 9. Handle repetitive tests with parametrize

The `pytest.mark.parametrize` decorator elegantly handles repetitive tests, for example to test an Uno card deck ([Bite 60. Create a deck of Uno cards](https://codechalleng.es/bites/60/)):

		@pytest.mark.parametrize("suit, count", [
			('Red', 25),
			('Green', 25),
			('Yellow', 25),
			('Blue', 25),
			(None, 8),  # wild cards don't have an associated suit
		])
		def test_create_uno_deck_suit_distribution(deck, suit, count):
			assert _count_suits(deck, suit) == count

Not only is this readable, it splits every tuple into a test, showing a dot in the output:

		[bbelderb@macbook 60 (master)]$ pytest test_uno.py::test_create_uno_deck_suit_distribution
		==================================== test session starts ====================================
		platform darwin -- Python 3.6.1, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
		rootdir: /Users/bbelderb/code/bites_of_py/60, inifile:
		collected 25 items

		test_uno.py .....

		================================= 5 passed in 0.03 seconds ==================================

You will find it more in later Bites because, as the other pytest features, once we knew about them we made them part of our daily pytest vocabulary :)

## 10. Capturing stdout

This was an important technique to know about because, although most Bites have functions returning values, some exercises lend themselves better to have the user print to the console, so you need to capture the script's standard output:

Here is the diff that shows the code we initially wrote to do this, before knowing about the `capfd` (`capsys`) fixture (thanks Brian):

![knowing about capfd saved a lot of unnecessary code]({filename}/images/pytest-if-we-did-not-have-capfd.png)

Yep, all you need is: `output = capfd.readouterr()[0]` - sweet!

---

I hope you learned a few things about testing and pytest, at least enough to _become dangerous_. Let us know if you have any feedback, some valuable improvements to our tests so far has come from user feedback, we really appreciate it.

And the learning never stops. Yes, writing test code is a big part of the learning, but some formal reading is useful too. So I loaded [this book on my Kindle](http://www.amazon.com/dp/0321503627/?tag=pyb0f-20) and am planning to listen to Brian's [Test and Code podcast](http://testandcode.com/).

---

### Featured in this article: our Bites of Py service - _Do you want to grow as a programmer solving interesting Python challenges?_

Our Bites of Py have helped many programmers learn and practice more Python. We've seen them strengthen their skills and even start new careers - all while challenging themselves with our Bites.

You not only get to solve interesting and relatable problems, but you also get to see how to do it in idiomatic Python.

We challenge you! Click [here](http://codechalleng.es/) and see if you can crack some Free Bites.

Like what you see?

[Subscribe here](https://gumroad.com/l/ZFrD) and become a Premium member instantly unlocking our (at the time of this writing) 100 Bites of Py exercises.

The key to improving your Python skills is continuous practice and PyBites makes it easy to get you into the coding habit and/or retain your existing coding muscles.

Additionally, coding with PyBites gives you access to an incredible (Slack) community of passionate Pythonistas happy to share their knowledge and learn from your experience.

---

Keep Calm and Code in Python!

-- Bob

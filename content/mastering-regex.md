Title: 10 Tips to Get More out of you Regexes
Date: 2017-01-15 9:00
Category: Tips
Tags: regex, tips, parsing, regular expressions, findall
Slug: mastering-regex
Authors: Bob
Summary: Regular expressions can be arcane, yet when used with care they can also be very powerful. In this post a couple of tips for using Python's re module.
cover: images/featured/pb-article.png
status draft

> Some people, when confronted with a problem, think, "I know, I'll use regular expressions." Now they have two problems.
> - Jamie Zawinski

Regular expressions can be arcane, yet when used with care they can also be very powerful. In this post a couple of tips for using Python's re module.

## 1. Do we need a regex?

First and foremost don't overuse them, specially when a string operation might do.

I like this comparison [by Jeff Atwood](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/), explaining the quote above:

> Regular expressions are like a particularly spicy hot sauce – to be used in moderation and with restraint only when appropriate

Note that you should only start thinking about regexes when normal string methods like starts-/endswith, replace, or 'in' can suffice. 

	>>> import re
	>>> text = 'regexes are powerful but use with care, some more text, lets play!'

	# overkill!
	>>> re.sub(r'some', 'a bit', text)
	'regexes are powerful but use with care, a bit more text, lets play!'

	# just use
	>>> text.replace('some', 'a bit')
	'regexes are powerful but use with care, a bit more text, lets play!'

	>>> os.path.splitext(file)
	('facter-1.6.2.tar', '.gz')

## 2. re.match() vs re.search()

* match() checks at the start of a string and returns None if nothing is found.
* search() moves up the string, looking for the first occurrence of the given pattern, and returns None only if the pattern occurs nowhere in the string.

	>>> text = 'Use match vs search as approriate'
	>>> re.match('search', text)
	>>> re.search('search', text)
	<_sre.SRE_Match object; span=(13, 19), match='search'>

## 3. Non-capturing parenthesis 

Use (?: ) to not capture matching contents, for example I want to get all links and hashtags out of a tweet. I need the outer parenthesis for capturing but also need parenthesis to say # or http:

	>>> tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
	>>> re.findall(r'((?:#|http)\S+)', tweet)
	['http://pybit.es/requests-cache.html', '#python', '#APIs']

When I don't use (?: ) more capturing happens making it a mess: 

	>>> re.findall(r'((#|http)\S+)', tweet)
	[('http://pybit.es/requests-cache.html', 'http'), ('#python', '#'), ('#APIs', '#')]

## 4. Always use raw string (r'<your_regex>')

The [excellent Regex HOWTO](https://docs.python.org/3.6/howto/regex.html) gives a nice example: in order to match \section you end up writing \\\\section in your regex :( - regexes can be complex enough, use r'' and take escaping out of the equation.

> The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline. Regular expressions will often be written in Python code using this raw string notation.

## 5. Watch out for greediness

Take this modified html from our blog: 

	html = """<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>"""

Imagine we want to match the first paragraph:

>>> m = re.search('<p>.*</p>', html)
>>> m.group()

Oops:

	'<p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p>'

Regular expressions are greedy, you can prevent this simply by using the ? after the repeating metacharacter (*, +, etc) which makes it match as little text as possible.

	>>> m = re.search('<p>.*?</p>', html)
	>>> m.group()
	'<p>Today a quick article on a nice caching module when working with APIs.</p>'
	 
## 6. Backreferences are powerful

I like this example from the HOWTO: find double words in a text:

	>>> p = re.compile(r'(\b\w+)\s+\1')
	>>> p.search('Paris in the the spring').group()
	'the the'

See also 9. re.sub where we use them fo string replacements.

## 7. findall (finditer) is awesome

We used it [here](https://github.com/pybites/blog_code/blob/1f4dc534d43ec2c8582a890a15fb54486b58af39/katas/course_time/js_course_time_scraper.py) for example to get al mm:ss timestamps of a course TOC, very cool:

	TIME_REGEX = re.compile(r'\(\d+:\d+\)')  # note I escaped the parenthesis (I think they were needed to get all timestamps)

	def search_file(file):
    	file_content = open(file).read()
    	time_regex = re.compile(r'\(\d+:\d+\)') 
    	return time_regex.findall(file_content) 

Output: 

	$ python js_course_time_scraper.py

	# intermediate result from findall:
	['(3:47)', '(4:41)', '(1:21)', '(5:32)', '(2:23)', '(1:01)', '(0:43)', '(1:46)', '(4:08)', '(3:20)', ...
	
	# further parsing + sum
	The course takes 6.841944444444445 hours to complete.

## 8. Advanced string replacements

re.sub is your friend, I use it quite often, [one example](https://github.com/bbelderbos/quotes_on_design/blob/master/quotes.py) or [for last challenge](https://github.com/pybites/challenges/blob/master/10/movies.py):

	MOVIE_TITLE = re.compile(r'\d+\.\s+(.*)\s\(.*').sub
	
	def get_movie():
		with open('movies.txt') as f:
			rand_line = random.choice(f.readlines())
			return MOVIE_TITLE(r'\1', rand_line.rstrip())

Use subn to also get the number of replacement:

	>>> html
	'<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>'
	>>> def strip_html(text):
	...     return re.subn(r'<[^<]+?>', '', text)
	...
	>>> strip_html(html)
	('Today a quick article on a nice caching module when working with APIs.Read more ...', 6)

re.sub even can take a function, nice example from [the documentation](https://docs.python.org/2/library/re.html):

	>>> def repl(m):
	...     inner_word = list(m.group(2))
	...     random.shuffle(inner_word)
	...     return m.group(1) + "".join(inner_word) + m.group(3)
	>>> text = "Professor Abdolmalek, please report your absences promptly."
	>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
	'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'

## 9. Compilation flags / modifiers + readability

See [here](https://docs.python.org/3.6/howto/regex.html#compilation-flags): apart from re.I (IGNORECASE), I don't use them often, but good to know which one we have available. The VERBOSE (X) flag can make a regex much more readable as nicely shown in Jeff Atwood's article and the HOWTO:

	pat = re.compile(r"""
	\s*                 # Skip leading whitespace
	(?P<header>[^:]+)   # Header name
	\s* :               # Whitespace, and a colon
	(?P<value>.*?)      # The header's value -- *? used to
						# lose the following trailing whitespace
	\s*$                # Trailing whitespace to end-of-line
	""", re.VERBOSE)

## 10. Python's unique naming style

Another readability feature is the Python's specific syntax for named groups:

>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Bob Belderbos")
>>> m.group('first_name')
'Bob'
>>> m.group('last_name')
'Belderbos'

---

## Further reading

* [Regular Expression HOWTO](https://docs.python.org/3.6/howto/regex.html) 

* [Docs: 6.2. re — Regular expression operations](https://docs.python.org/3.6/library/re.html)

* Wesley Chun's [Core Python Applications Programming](https://www.amazon.com/Core-Python-Applications-Programming-3rd/dp/0132678209/ref=sr_1_1?s=books&ie=UTF8&qid=1489510087&sr=1-1&keywords=wesley+chun) - Chapter 1. Regular Expressions

* [Regular Expressions: Now You Have Two Problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)

* To go really deep [Mastering Regular Expressions](https://www.amazon.com/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/ref=sr_1_1?ie=UTF8&qid=1489509976&sr=8-1&keywords=regular+expressions) - warning: for generic regex overview, language specific chapters include Perl/Java/.NET/PHP sections, not Python.

---

Keep Calm and Code in Python!

-- Bob

Title: Simple script to generate a blog page of your kindle book notes
Date: 2016-12-27 0:10
Category: Tools
Tags: kindle, Template strings, json, html, books, bookcision, generators, 
Slug: kindle-json-to-html
Authors: Bob
Summary: In this post I share a simple script to convert Bookcision json into a html page for your blog.

## Kindle notes

I was looking at an effective way to organize my Kindle highlights. I started looking at parsing the Kindle's My Clippings.txt file. However I had not much luck with existing PyPi modules and it is a bit cumbersome to always have to manually copy it via USB cable.

## Starting point: Cloud + Bookcision

Then I found a much better starting point: [https://kindle.amazon.com](https://kindle.amazon.com) = cloud. OK, this only works for Kindle purchased books, but using Amazon's [Whispersync](https://www.amazon.com/gp/help/customer/display.html?nodeId=200911660) really makes this convenient. Also, the Kindle site lets you filter / adjust your highlights and notes before exporting. 

For export I use the nice [Bookcision JS bookmarklet](http://www.norbauer.com/bookcision/) which - when used in Chrome - gives you the ability to dowload the highlights JSON format.

## JSON => HTML

I wrote a script to convert the Bookcision JSON download into a static html page (for blog use, inspired by [Sivers](https://sivers.org/book)).

Code is [here](https://github.com/pybites/blog_code/tree/master/kindle_notes).

Some things to note:

* Use json.loads(fh) to convert json into dict: 

	def load_json(json_file):
		with open(json_file) as f:
			return json.loads(f.read())

* [Template strings](https://docs.python.org/2/library/string.html#template-strings): in [templates.py](https://github.com/pybites/blog_code/blob/master/kindle_notes/templates.py) PAGE defines the whole page, I use embedded CSS to make this a standalone solution. QUOTE defines a list item (highlight). Variables are defined with $ so: $title, $author, etc. In the [main script](https://github.com/pybites/blog_code/blob/master/kindle_notes/kindle_json2html.py) I can substitute these variable placeholders with a dict: 

	def get_highlights(highlights):
		for hl in highlights:
			yield QUOTE.safe_substitute({
				'text' : hl['text'],
				'note' : ' / note: ' + hl['note'] if hl['note'] else '',
				'url' : hl['location']['url'],
				'location': hl['location']['value'],
			})

Note the 'yield' makes get_highlights() a generator. If this is new, check out [this SO thread](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do) about Iterables -> Generators -> Yield.

* Use list() to consume all generator's values in one go: 

	highlights = get_highlights(content['highlights'])
	...
	...
    	'content': '\n'.join(list(highlights)),

* You can give the script one or more json files simply by using a slice on sys.argv:

	for json_file in sys.argv[1:]:
		...

* So you can batch process json downloads:

	$ ls *json
	anything-you-want.json	arnold.json		choose-yourself.json	hustle.json		the-circle.json

	$ python kindle_json2html.py *json
	anything-you-want.html created
	arnold.html created
	choose-yourself.html created
	hustle.html created
	the-circle.html created

## Example 

Here is how an output looks:

![resulting html page]({filename}/images/example-book-html.png)

As the html contains everything you can just put this file in your blog version control, commit, push, done.

---

Keep Calm and Code in Python!

-- Bob

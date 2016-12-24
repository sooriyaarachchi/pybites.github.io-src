Title: Get a weekly digest from a Pelican blog
Date: 2016-12-24 15:40
Category: Tools
Tags: pelican, feedparser, rss
Slug: blog-digest
Authors: Bob
Summary: In this post a script we use to get a weekly digest of our posts.

## Prep work

We built this blog in Pelican, adding this in pelicanconf.py adds an RSS feed:

FEED_RSS = 'feeds/all.rss.xml'

And voila, after pushing this change we have [our RSS feed](http://pybit.es/feeds/all.rss.xml).

## Script (use PyPi!)

The script is [on github](https://github.com/pybites/blog_code/tree/master/pybites_digest) in our [new blog repo](https://github.com/pybites/blog_code).

No need to re-invent the wheel, PyPI (Python Package Index) has so much good stuff, feedparser is just what we need. It can take both a remote as well as local xml file, so you don't even need requests. 

This single line parses the feed into a comprehensive data structure:

    feed = feedparser.parse(xml)

Which you can then easily consume: 

	for article in feed['entries']:
		# ... filtering
        yield article

The only thing I had to add was some timestamp conversations/calculations to go x days back (the returned feed data has a convenient [time.struct_time field](https://docs.python.org/3.5/library/time.html#time.struct_time)).

## Mail digest as txt/html in a cronjob

I left this for sendmail which accepts a mailheader, see [here](http://stackoverflow.com/questions/24010230/mailx-send-html-message). So this is my weekly cronjob:

	# html email 
	0 7 * * 6 cat pybites_header <(python3 /path/to/pybites_digest/digest.py 7 1) | sendmail -t

	# text version for copy+paste into social media
	0 7 * * 6 cat pybites_header <(python3 /path/to/pybites_digest/digest.py 7) | sendmail -t

* First arg is "days back" = 7 = one week / 2nd arg = html True

* You might need to do a export PYTHONPATH=/path/to/python3.x/site-packages if you installed Python3 in your $HOME on a shared hosting provider. 

* The '<()' syntax is a nice way in Unix to join in output from a subprocess.

## Don't miss any post

If you want to receive these weekly digests please subscribe to our blog or join our [FB group](https://www.facebook.com/groups/1305028816183522/).


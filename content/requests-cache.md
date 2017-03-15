Title: Module of the Week - Requests-cache for Repeated API Calls
Date: 2017-03-14 8:00
Category: Modules
Tags: requests, cache, APIs, package
Slug: requests-cache
Authors: Bob
Summary: Today a quick article on a nice caching module when working with APIs: [Requests-cache](https://pypi.python.org/pypi/requests-cache).
cover: images/featured/pb-article.png

Today a quick article on a nice caching module when working with APIs: [Requests-cache](https://pypi.python.org/pypi/requests-cache).

I stumbled upon this [excellent article by RealPython](https://realpython.com/blog/python/caching-external-api-requests/) when looking for a solution to limit API requests. I needed this when I was playing with the Github API to check [changes to forks of our Challenges repo](https://github.com/pybites/blog_code/blob/master/forks/commits.py) (you can also see this in the repo, under Graphs > Network, but I was just playing around).

This is not a script that would typically need caching, because I probably would run it once a week and then it would make just a couple of requests (at this time: ~100 forks / 30 results per call). However when I was coding this up, I did not want to call the API over and over again:

> For unauthenticated requests, the rate limit allows you to make up to 60 requests per hour. 
> [Github API documentation](https://developer.github.com/v3/#rate-limiting) 

It was also a good exercise to test this module out for a future use case where this does matter.

## Using requests_cache

First I thought: lets write the output to a file. However that adds more code. Maybe use a decorator to sleep between requests? However that slows down my coding/testing. As usual somebody already invented the wheel. 

Enter Requests-cache. It has an easy / friendly interface:

	import requests_cache

	requests_cache.install_cache('cache_filename', backend='backend', expire_after=expiration_in_seconds)

- where backend has [these options](http://requests-cache.readthedocs.io/en/latest/user_guide.html#persistence).

## Verify with curl

* Start API rate limit (already did some calls):

		$ curl -i https://api.github.com/users/whatever 2>/dev/null |grep 'X-RateLimit-Remaining:'
		X-RateLimit-Remaining: 42

* First time around: cache result. DB got created. Cost = 6 calls (1x curl, 5x by script)

		$ python commits.py 2>&1 > /dev/null
		$ lt cache.sqlite
		-rw-r--r--  1 bbelderb  staff   516K Mar 14 08:03 cache.sqlite
		$ curl -i https://api.github.com/users/whatever 2>/dev/null |grep 'X-RateLimit-Remaining:'
		X-RateLimit-Remaining: 36

* Second call = cached, cost down to 1 (= curl)

		$ python commits.py 2>&1 > /dev/null
		$ curl -i https://api.github.com/users/whatever 2>/dev/null |grep 'X-RateLimit-Remaining:'
		X-RateLimit-Remaining: 35

## Keep in mind

Two noteworthy things that were commented on mentioned article:

* Check the documentation of the API you are working with. Maybe they already provide a way to use caching. In case of the GH API this would be [Conditional requests](https://developer.github.com/v3/#conditional-requests):

	> Making a conditional request and receiving a 304 response does not count against your Rate Limit, so we encourage you to use it whenever possible.

	Something to try on the next iteration ...

* You might want to define an output directory for the cache file instead of the default current directory to not end up with multiple files if working from a different folder. 

## More info

See the module's [documentation](http://requests-cache.readthedocs.io/en/latest/index.html) for more info. 

Have you used this module? And/or what do you use for caching API requests? 

---

Keep Calm and Code in Python!

-- Bob

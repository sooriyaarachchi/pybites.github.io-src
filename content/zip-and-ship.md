Title: Zip and ship, make an executable zipfile of your py project
Date: 2016-12-25 9:06
Category: Packages
Tags: zip, packaging, distribute, pip
Slug: zip-and-ship
Authors: Bob
Summary: In this post I show an example how you can distribute your code as an executable zipfile, a neat trick I discovered in Chapter 6 of The Hitchhiker's Guide to Python
cover: images/featured/zip-and-ship.png

## Get started

First of all, new in version 3.5 is [zipapp](https://docs.python.org/3/library/zipapp.html) which makes this easier. As not everybody is on this version yet, I will show the manual way to do this.

We're going to use [the code](https://github.com/pybites/blog_code/tree/master/pybites_digest) of our last post: [Get a weekly digest from a Pelican blog](http://pybit.es/blog-digest.html). 

## Step by step

OK here we go:

	$ git clone https://github.com/pybites/blog_code zip-example
	Cloning into 'zip-example'...
	remote: Counting objects: 22, done.
	remote: Compressing objects: 100% (14/14), done.
	remote: Total 22 (delta 4), reused 22 (delta 4), pack-reused 0
	Unpacking objects: 100% (22/22), done.
	Checking connectivity... done.

	$ cd zip-example/pybites_digest/
	$ mkdir archive && cd $_
	$ cp ../digest.py __main__.py

	# Note that where I say python3 and pip3 for you it might be python and pip

	$ pip3 install -r ../requirements.txt --target=packages
	Collecting feedparser==5.2.1 (from -r ../requirements.txt (line 1))
	Installing collected packages: feedparser
	Successfully installed feedparser-5.2.1

	$ touch packages/__init__.py
	$ ls *
	__main__.py
	packages:
	__init__.py			<dependencies>

	# edit the main script to use the locally installed package (doing 'in place' edit)
	$ perl -pi -e 's/import feedparser/import packages.feedparser as feedparser/g' __main__.py

	# zip it up
    $ zip my_script.zip -r *
	adding: __main__.py (deflated 55%)
	adding: packages/ (stored 0%)
	adding: packages/__init__.py (stored 0%)
	adding: packages/__pycache__/ (stored 0%)
	adding: packages/__pycache__/feedparser.cpython-35.pyc (deflated 59%)
	adding: packages/feedparser-5.2.1.dist-info/ (stored 0%)
	adding: packages/feedparser-5.2.1.dist-info/DESCRIPTION.rst (stored 0%)
	adding: packages/feedparser-5.2.1.dist-info/INSTALLER (stored 0%)
	adding: packages/feedparser-5.2.1.dist-info/METADATA (deflated 64%)
	adding: packages/feedparser-5.2.1.dist-info/metadata.json (deflated 58%)
	adding: packages/feedparser-5.2.1.dist-info/RECORD (deflated 40%)
	adding: packages/feedparser-5.2.1.dist-info/top_level.txt (stored 0%)
	adding: packages/feedparser-5.2.1.dist-info/WHEEL (stored 0%)
	adding: packages/feedparser.py (deflated 74%)

    $ echo '#!/usr/bin/env python3' > my_script
    $ cat my_script.zip >> my_script
    $ chmod ug+x my_script

	# to prove it shows the feedparser package is not installed in my main py3 installation
    $ python3
	Python 3.5.1 |Anaconda 4.0.0 (x86_64)| (default, Dec  7 2015, 11:24:55) 
	[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import feedparser
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ImportError: No module named 'feedparser'
	>>> 

	# yet it works with the zipped package :)
    $ ./my_script 
	Get a weekly digest from a Pelican blog
	http://pybit.es/blog-digest.html
	In this post a script we use to get a weekly digest of our posts.
	--

	2016 py articles and useful books
	http://pybit.es/py-articles-books2016.html
	Some of my Python articles I posted on my blog this year and useful books
	...
	...

	# I can put it in my $HOME/bin now as well:

	$ cp my_script ~/bin/pybites_digest
	$ which pybites_digest
	/Users/bbelderb/bin/pybites_digest
	$ pybites_digest
	Zip and ship, make an executable zipfile of your py project
	http://pybit.es/zip-and-ship.html
	In this post I show an example how you can distribute your code as an executable zipfile, a neat trick I discovered in Chapter 6 of The Hitchhiker's Guide to Python
	--
	...
	...


## Conclusion

Although I would not use this for bigger projects ([you loose debugging abilities](https://blogs.gnome.org/jamesh/2012/05/21/python-zip-files/)), this is still a neat way to package up and ship scripts. Consumers don't have to worry about installing dependencies / doing any pre-work.

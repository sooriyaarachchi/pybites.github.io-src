Title: How to get me up and running
Date: 2016-12-20 10:40
Category: Meta
Tags: pelican, publishing, github, pip, virtualenv
Slug: install-me
Authors: Pybites
Summary: This is a short post for Julian

This is also a useful ref for future collaborators ...

We're open source right? ;)

## Pybites install guide

	# we have a src, output and theme (Flex) repo, use --recursive to get all
	$ git clone --recursive git@github.com:pybites/pybites.github.io-src pybites
    $ cd pybites

	# set up env and install dependencies
    $ virtualenv venv (might need: virtualenv -p python3 venv)
    $ source venv/bin/activate
    $ pip install -r requirements.txt
	
	# add some content
    $ cd content
    $ vi new-blog-post.md ; wq!                                                                                                        

	# check changes on localhost
	$ cd ..
    $ make html && make serve 

	# push this new content to the parent -src repo
    $ git add . 
	$ git commit -m "my new blog post"
	$ git push

	# push the static blog change to the child -io repo
	# TODO: this is duplicate step, should we use gph-import / post-commit?
	# http://docs.getpelican.com/en/3.3.0/tips.html
	$ cd output
    $ git add . 
	$ git commit -m "my new blog post"
	$ git push
	

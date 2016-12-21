Title: How to get PyBites up and running on your machine
Date: 2016-12-20 10:40
Category: Tools
Tags: pelican, publishing, github, pip, virtualenv, git
Slug: install-me
Authors: Pybites
Summary: This is a short post for Julian to get this Pelican blog up and running on his system.

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
	# wait: this is a duplicate step, I don't like duplication!
	# ...

As we have 2 repos: -src for code, -io for generated static content, ideally we want to automate the publishing to -io, so we can just focus on the main repo (-src). 

Here is where [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) come into play. cd into .git/hooks and add below script, name it "pre-push", update your WORKING_DIR and chmod 755 it:

	#!/bin/sh
	# this post update hook is to update the static -io repo (effectively the blog) upon any commit in the -src code repo

	set -e 

	WORKING_DIR=/Users/bbelderb/code/pybites
	OUTPUT_DIR=$WORKING_DIR/output

	cd $WORKING_DIR

	# if venv not enabled turn it on otherwise make html will fail
	if [ "$VIRTUAL_ENV" = "" ]; then
		source venv/bin/activate
	fi

	make html

	if [ $? -eq 0 ]; then
		cd $OUTPUT_DIR
	    git add .
	    git commit -m "commit to pybites.github.io-src, post-commit script auto-creating blog (pybites.github.io)"
	    git push origin master
	else
	    echo "Something went wrong, run make html manually to see what is wrong ..."
	    exit 1
	fi

	exit 0


And voila only one push needed: 

	(venv) [bbelderb@macbook pybites (master)]$ git push
	pelican /Users/bbelderb/Documents/code/pybites/content -o /Users/bbelderb/Documents/code/pybites/output -s /Users/bbelderb/Documents/code/pybites/pelicanconf.py 
	Done: Processed 5 articles, 0 drafts, 2 pages and 0 hidden pages in 0.89 seconds.
	[master 4ab2fd5] commit to pybites.github.io-src, post-commit script auto-creating blog (pybites.github.io)
	..
	..
	To git@github.com:pybites/pybites.github.io.git
	2d71d76..4ab2fd5  master -> master
	..
	To git@github.com:pybites/pybites.github.io-src
	1d531e6..f90c12b  master -> master	

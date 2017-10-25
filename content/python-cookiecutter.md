Title: Bootstrap Your Next Python Project With Cookiecutter
Date: 2017-10-25 00:11
Category: Tools
Tags: Cookiecutter, setup, testing, packages, modules, Bottle
Slug: python-cookiecutter
Authors: Bob
Summary: I finally did it! I bootstrapped my first project with Cookiecutter. There is a lot to discover but wow this tool can save you a ton of time, making your project more professional.
cover: images/featured/pb-article.png

I finally did it! I bootstrapped my first project with Cookiecutter. There is a lot to discover but wow this tool can save you a ton of time, making your project more professional.

This is just a quick article to document this nice tool brought to us by the authors of [Two Scoops of Django](https://www.amazon.com/dp/0692915729/?tag=pyb0f-20).

> Cookiecutter does one thing and it does it well - Daniel Roy Greenfeld

## Installation

First I ran a pip install but I could not find it in my path so I went full force with:

	brew install cookiecutter

That's on Mac. On Ubuntu you would do:

	sudo apt-get install cookiecutter

As it's a tool I will use to boostrap various projects I think having it outside a virtualenv is justified.

## How to start

The best place to check out is their latest documentation jumping straight to the [usage section](https://cookiecutter.readthedocs.io/en/latest/usage.html).

At first I pulled the repo and filled out the `cookiecutter.json`, a convenient defaults file for hands off (`--no-input`) project creation. 

The interactive option is convenient too:

	$ cookiecutter gh:audreyr/cookiecutter-pypackage
	full_name [Audrey Roy Greenfeld]: Bob Belderbos
	email [aroy@alum.mit.edu]: info@bobbelderbos.com
	github_username [audreyr]: bbelderbos
	project_name [Python Boilerplate]: PyBites Hacktoberfest Checker
	project_slug [pybites_hacktoberfest_checker]:
	project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: Checking number of PRs done in Oct for the Digital Ocean's Hacktoberfest challenge. Also my first Bottle app.
	pypi_username [bbelderbos]:
	version [0.1.0]:
	use_pytest [n]: y
	use_pypi_deployment_with_travis [y]:
	Select command_line_interface:
	1 - Click
	2 - No command-line interface
	Choose from 1, 2 [1]:
	create_author_file [y]:
	Select open_source_license:
	1 - MIT license
	2 - BSD license
	3 - ISC license
	4 - Apache Software License 2.0
	5 - GNU General Public License v3
	6 - Not open source
	Choose from 1, 2, 3, 4, 5, 6 [1]:

I only then realized that there are project based cookiecutters so I picked [the bottle one](https://github.com/avelino/cookiecutter-bottle), the micro web-framework I want to use for our [code challenge 38](https://pybit.es/codechallenge38.html).

It could not be easier: just point to the Github repo. It is more bare bones than cookiecutter-pypackage though:

	$ cookiecutter https://github.com/avelino/cookiecutter-bottle.git
	full_name [Thiago Avelino]: Bob Belderbos
	email [thiago@avelino.xxx]: info@bobbelderbos.com
	github_username [avelino]: bbelderbos
	project_name [My Bottle App]: PyBites Hacktoberfest Checker
	app_name [mybottleapp]: hacktoberfestapp
	project_short_description [A cookiecutter template for creating reusable Bottle projects quickly]: Checking number of PRs done in Oct for the Digital Ocean's Hacktoberfest challenge. Also my first Bottle app.

At this point you can cd into it, do a git init, make a virtual env and install the requirements:

	$ virtualenv -p /Users/bbelderb/anaconda/bin/python venv
	$ echo "venv" >> .gitignore
	$ source venv/bin/activate
	(venv) $ pip install -r requirements.txt
	...
	(venv) $ git init
	Initialized empty Git repository in /Users/bbelderb/code/hacktoberfestapp/.git/
	(venv) $ git status
	...

		.gitignore
		README.rst
		hacktoberfestapp/
		manage.py
		requirements.txt
		tests/

	(venv) $ git add . && git commit -m "init commit"
	(venv) $ python manage.py  runserver
	...
	Listening on http://0.0.0.0:8080/

Nice:

![default Bottle cookiecutter homepage]({filename}/images/cookiecutter_bottle.png)

And here is the directory structure with some bootstrap code:

![Bottle bootstrap folder structure and files]({filename}/images/bottle_app_boilerplate.png)

## Conclusion

I think the main take away is that Cookiecutter takes a lot of worries away regarding setup, folder structure, required files, etc. It might be overkill for some projects, but it does add consistency  across your projects and endorses best practices.

I only scratched the service. I really would like to try [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask), [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) and [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest) for future projects. Or how to create our own PyBites Cookiecutter? And what about defining pre- and post-generate hooks (Python or shell scripts to run before or after generating a project)? Enough to explore for a follow-up article ...

Feel free to share what you have used Cookiecutter for in the comments below. 

![cookiecutter is a nice and clean way to bootstrap a Python project]({filename}/images/banners/pb_cookiecutter.png)

## Further resources

* [Cookiecutter GH repo](https://github.com/audreyr/cookiecutter): lists of awesome features that make Cookiecutter a great tool. Scroll down to [*A Pantry Full of Cookiecutters*](https://github.com/audreyr/cookiecutter#a-pantry-full-of-cookiecutters) for *a list of cookiecutters (aka Cookiecutter project templates) for you to use or fork*, there are a lot!
* [Cookiecutter docs](https://cookiecutter.readthedocs.io/en/latest/).
* Author's post: [Cookiecutter: Project Templates Made Easy](https://www.pydanny.com/cookie-project-templates-made-easy.html) introducing the project, including how to create your own cookiecutter templates.
* An > 3 hours in-depth video course by Michael Kennedy: [Using and Mastering Cookiecutter](https://training.talkpython.fm/courses/explore_cookiecutter_course/using-and-mastering-cookiecutter-templates-for-project-creation).

---

Keep Calm and Code in Python!

-- Bob

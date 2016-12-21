Title: The Beauty of Python Virtualenvs
Date: 2016-12-20 22:11
Category: Tools
Tags: python, pip, virtualenv, venv
Slug: the-beauty-of-virtualenv
Authors: Julian
Summary: Python Virtualenvs are incredible yet sadly under utilised!

Ever heard of a Python virtualenv before? No? Neither had I, until one awesome day when I was enlightened while following 
a video course on Python Flask.

A virtualenv (AKA venv) is essentially a Virtual Machine (VM) or sandbox environment that runs an independent and untouched Python environment.
When you create and activate the venv you no longer have access to the main Python environment running on your system.

The problem programmers have is that it can be hard to isolate problems in code when their primary environment is cluttered with imported modules and the like.
When you activate the venv you're launching a standalone Python instance that has pretty much nothing installed by default (see below code).

You can then play around and install whatever the heck you want without having to worry about corrupting or screwing up your primary environment.

Furthermore, you can exit (deactivate) and re-enter (activate) the venv whenever you want and all of your test config will still be in place. It doesn't wipe on exit! (Yay!).

The seasoned veteran out there will surely read this and call me a noob... and they'd be right! It's exactly why I'm so stoked to have discovered venvs!

If you're not using virtualenvs yet, install the package and give it a whirl. Below is some example code detailing the process.

Keep Calm and Code in Python!

- Julian




	

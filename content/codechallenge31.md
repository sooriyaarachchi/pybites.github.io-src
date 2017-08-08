Title: Code Challenge 31 - Imagine Manipulation With Pillow
Date: 2017-08-08 13:28
Category: Challenges
Tags: codechallenges, images, pillow, Flask, newquote
Slug: codechallenge31
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding. Let's shift gears a little bit: this week we have you choose an image manipulation task using [Pillow](https://python-pillow.org/), "the friendly PIL (Python Imaging Library) fork". Have fun!
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, a new week, a new 'bite' of Python coding. Let's shift gears a little bit: this week we have you choose an image manipulation task using [Pillow](https://python-pillow.org/), "the friendly PIL (Python Imaging Library) fork". Have fun!

## The challenge

[Create a new virtual env](https://pybit.es/the-beauty-of-virtualenv.html), `pip install Pillow` and use the module for one of the following tasks:

* Create a tool to create thumbnails of a set of images.

* Use Instagram like filters on a bunch of images.

* Make promo banners for your brand or cause using Pillow: basically put your logo, a nice background and text on a canvas and save to file. [Example](https://twitter.com/pybites/status/853560501854515200) made with Gimp, what about generating something similar with Pillow?

* Similar as last one: make a birthday ecard generator.

* Add a watermark to an image.

* Feel free to do something else if that inspires you more, as long as you use Pillow!

### Bonus

* Wrap the utility up in a little Flask app with interactive input/select boxes, for example: 

	* [Featured Image Creator](http://projects.bobbelderbos.com/featured_image/) was a PHP/JS/CSS project I (Bob) did some time ago. Maybe you can build something similar using Flask (JS) for user interaction and Pillow to generate the image upon form submit?

	* For a thumbnail generator you could have a (multi) image upload button which batch resizes them and shows them in the browser or generates a zipfile for download.

	* What about the (birthday) ecard generator: let the user choose between a set of images, enter a text and show the generated card in the browser with download link.

	* Etc ... combining user interaction (web app) and Pillow you can build some cool stuff. The possibilities are endless, surprise us ...

* Deploy your solution to Heroku to show it to the world (and mention the URL in your PR).

### Resources

* [Pillow homepage](https://python-pillow.org/)

* [Pillow docs](https://pillow.readthedocs.io/en/4.2.x/)

* [How to use Pillow, a fork of PIL](http://www.pythonforbeginners.com/gui/how-to-use-pillow)

* [An Intro to the Python Imaging Library / Pillow](https://www.blog.pythonlibrary.org/2016/10/07/an-intro-to-the-python-imaging-library-pillow/)

* [ATBS - Chapter 17 – Manipulating Images](https://automatetheboringstuff.com/chapter17/)

* [100 DaysOfCode - day 74: Using Pillow to add text and opacity to an image = your own cards](https://github.com/pybites/100DaysOfCode/tree/master/074)

* [Step-by-Step Guide on Deploying a Simple Flask App to Heroku](https://pybit.es/deploy-flask-heroku.html)

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

## Feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or [reach out](http://pybit.es/pages/about.html) directly.

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian

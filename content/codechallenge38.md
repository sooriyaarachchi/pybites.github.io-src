Title: Code Challenge 38 - Build Your Own Hacktoberfest Checker With Bottle
Date: 2017-10-04 11:20
Category: Challenge
Tags: Hacktoberfest, DigitalOcean, Bottle, GitHub, API, Web development
Slug: codechallenge38
Authors: PyBites
Summary: Hi Pythonistas, Hacktoberfest started. Let's make open source better and track our progress with a little app you will build using the [Bottle web framework](https://bottlepy.org/docs/dev/).
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, Hacktoberfest started. Let's make open source better and track our progress with a little app you will build using the [Bottle web framework](https://bottlepy.org/docs/dev/).

## It's Hacktoberfest

DigitalOcean's [Hacktoberfest](https://hacktoberfest.digitalocean.com) is a month-long celebration of open source software. You can earn a cool T-shirt making four pull requests to any public repo on GitHub between October 1–31. 

Potential projects you could contribute to are listed on their site but PRs you make for our code challenges count too!

## The Challenge

[Hacktoberfest Checker](https://hacktoberfestchecker.herokuapp.com) ([code](https://github.com/jenkoian/hacktoberfest-checker)) is a neat web app to see how close you are to achieving the requirements (4 PRs) for a free t-shirt. It is written [in JS](https://github.com/jenkoian/hacktoberfest-checker/blob/master/controllers/index.js).

We thought it would be a cool challenge to build this with Bottle (optionally adding the JS you'd like):

1. Make a virtual env and install Bottle.

2. Make a form to ask for the user. Optionally add GitHub login to retrieve the user automatically.

3. Retrieve the PRs via the GitHub API. You can borrow the required query [here](https://github.com/pybites/hacktoberfest-checker/blob/master/controllers/index.js) (L15). Yes, the date range seems odd but it accounts for various timezones. It was taken from DigitalOcean's 'official' checker (as explained [in this issue](https://github.com/jenkoian/hacktoberfest-checker/pull/104#issuecomment-333376597)).

4. Display the PR's and progress as (*n out of 4*). You can use the [these status messages](https://github.com/pybites/hacktoberfest-checker/blob/master/controllers/index.js) (L67).

5. (bonus) allow checking multiple GH handles so you could compare progress among fellow developers or friends.

## Credit

To get credit PR your work to our Community branch of our [Challenges repo](https://github.com/pybites/challenges). See detailed instructions [here](https://github.com/pybites/challenges/blob/master/INSTALL.md). 

And remember: __any of [our code challenges](https://pybit.es/pages/challenges.html) you PR this month counts towards the Hacktoberfest goal__, have fun!

### About 

Our goal is to learn and teach you Python through practical exercises. Learning a programming language is way more fun as a community!

For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or [drop us an email](mailto:pybitesblog@gmail.com). 

---

Keep Calm and Code in Python!

-- PyBites

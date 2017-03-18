Title: Code Challenge 08 - House Inventory Tracker - Review
Date: 2017-03-05 09:00
Category: Challenges
Tags: codechallenges, code review, learning, inventory, Flask, APIs, data structures
Slug: codechallenge08_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge08.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge08.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Learning

### Julian

The simplicity of this challenge is what made it fun for me. The challenge was in deciding how to store and manage the data in the most effective (and hopefully Pythonic!) way.

I decided to go with multiple dicts: dicts for each room and then one main dict for the list of rooms.

Code wise, the challenge was to then properly list out the required keys and values of each dict when required. I did this using nested for loops in the *print_contents()* function.

I also added in a quick function to get the value of each room in total. It was satisfying seeing the result of sum(v.values()) appear! See output below:

	$ python inventory_julian.py

	Study
	computer: $1200
	lg flatron monitor: $300
	samsung monitor: $500
	desk: $400
	guitar: $500

	Living Room
	couch: $1000
	tv: $3000
	playstation: $500
	speakers: $600
	beanbag: $30

	Master Bedroom
	bed: $400
	mattress: $1000
	chair: $180
	drawers: $250
	lamp: $20

	Totals:
	Study: $2900
	Living Room: $5130
	Master Bedroom: $1850

Code [here](https://github.com/pybites/challenges/blob/solutions/08/inventory_julian.py).

### Bob

I had fun making an interactive version for this. This forced me to think about user input validation: name of item is required, value requires an int.
There might be a bit repetition in resulting *get_name* and *get_value*, they both ask for user input, yet do different validations. 
Maybe something to wrap in a validation class ...

Nice constructs I could use: defaultdict, namedtuple and format printing.

Before I would have mixed calculation and printing, now I isolating the summing in *calc_totals* function which makes it a bit cleaner. 
See output below - I changed the NUM_ITEMS constant to 2 for shorter output (could make it a command line arg ...)

	$ python inventory_bob.py

	Entering items for room study:

	* Item #1:
	- Enter the name of the item: monitor
	- Enter the value of the item: 200
	* Item #2:
	- Enter the name of the item: laptop
	- Enter the value of the item: 1000

	Entering items for room living_room:

	* Item #1:
	- Enter the name of the item: sofa
	- Enter the value of the item: 600
	* Item #2:
	- Enter the name of the item: tv
	- Enter the value of the item: 500

	Entering items for room master_bedroom:

	* Item #1:
	- Enter the name of the item: bed
	- Enter the value of the item: 1000
	* Item #2:
	- Enter the name of the item: couch
	- Enter the value of the item: 400

	* Room: study
	monitor        :   200
	laptop         :  1000
	--
	Subtotal       :  1200

	* Room: living_room
	sofa           :   600
	tv             :   500
	--
	Subtotal       :  1100

	* Room: master_bedroom
	bed            :  1000
	couch          :   400
	--
	Subtotal       :  1400

	----
	Total          :  3700

Code [here](https://github.com/pybites/challenges/blob/solutions/08/inventory_bob.py).

### Bonus: simple API

This was also a good occasion to make a simple API with Flask, which we practiced [here](http://pybit.es/simple-flask-api.html).

## Feedback

What was your solution? Feel free to share in the comments below.

We hope you enjoy these challenges. Please provide us feedback if we can improve anything ...

If you have an interesting challenge you want us to feature, don't hesitate to reach out to us.

See you next week ...

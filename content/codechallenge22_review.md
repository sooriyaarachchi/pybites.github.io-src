Title: Code Challenge 22 - Packt Free Ebook Web Scraper - Review
Date: 2017-06-12 13:00
Category: Challenges
Tags: codechallenges, webscraping, BeautifulSoup, Selenium, Packt, Pybonacci, ebooks, community, automation, sponsoring
Slug: codechallenge22_review
Authors: PyBites
Summary: In this article we review last week's [Packt free ebook code challenge](http://pybit.es/codechallenge22.html). We really scratched our own itch building both a notification service and an ebook download manager.
cover: images/featured/pb-challenge.png

In this article we review last week's [Packt free ebook code challenge](http://pybit.es/codechallenge22.html). We really scratched our own itch building both a notification service and an ebook download manager.

First of all we were a tad disappointed not being able to automate the whole thing. Packt's [free-learning link](https://www.packtpub.com/packt/offers/free-learning) requires a "I'm not a robot" captcha to be solved. We are not the only ones [hitting this wall](https://github.com/igbt6/Packt-Publishing-Free-Learning/issues/51). [2captcha](https://2captcha.com/recaptchav2_eng_instruction) provies a possible way around it, but we didn't go there. 

Update 24/08/2017: there is [a fix](https://github.com/igbt6/Packt-Publishing-Free-Learning/pull/56) for this now.

There was still a lot of room to build cool/useful stuff:

## Packt Daily Notification Email

We wrote a script to get a daily html email of the free html book, the amount of hh:mm before it expires, and adding [Pybonacci's affiliation link](https://www.packtpub.com/packt/offers/free-learning?utm_source=Pybonacci&utm_medium=referral&utm_campaign=FreeLearning2017CharityReferrals) (to sponsor Python Spain).

Here is how it looks: 

![packt-notifier]({filename}/images/packt-notifier.png)

Code is [here](https://github.com/pybites/100DaysOfCode/tree/master/076).

## Packt Ebook Download Manager

We also made a script to manage downloaded/purchased Packt ebooks. It uses requests session (detailed [here](https://pybit.es/requests-session.html)) to login/access/download books. We use BeautifulSoup for html parsing. Here you can see it in action:

	$ python packt.py
	PACKT DOWNLOAD MANAGER

	Logging in
	Retrieving books

	Seach for a book (q for exit): dta
	No matches, try again

	Seach for a book (q for exit): data
	1) Learning Data Mining with Python [eBook]
	2) R Data Visualization Cookbook [eBook]
	3) Practical Data Science Cookbook [eBook]
	4) Data Analysis with R [eBook]
	5) ASP.NET Data Presentation Controls Essentials [eBook]
	6) Implementing Splunk: Big Data Reporting and Development for Operational Intelligence [eBook]
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/21201/pdf
	2) https://www.packtpub.com/ebook_download/21201/epub
	3) https://www.packtpub.com/ebook_download/21201/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/21201/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/learning-data-mining-with-python.pdf
	Choose book (n for new search): n

	Seach for a book (q for exit): python
	1) Expert Python Programming - Second Edition [eBook]
	2) Modern Python Cookbook [eBook]
	3) Python GUI Programming Cookbook [eBook]
	4) What You Need to Know about Python [eBook]
	5) Raspberry Pi Cookbook for Python Programmers [eBook]
	6) Learning Python Application Development [eBook]
	7) Learning Robotics Using Python [eBook]
	...
	many more (thanks Packt!)
	...
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/25257/pdf
	2) https://www.packtpub.com/ebook_download/25257/epub
	3) https://www.packtpub.com/ebook_download/25257/mobi
	Choose url (c to cancel): 3
	Downloading https://www.packtpub.com/ebook_download/25257/mobi
	Saving to /Users/bbelderb/Documents/books/Packt/expert-python-programming-second-edition.mobi
	Choose book (n for new search): 22
	1) https://www.packtpub.com/ebook_download/20125/pdf
	2) https://www.packtpub.com/ebook_download/20125/epub
	3) https://www.packtpub.com/ebook_download/20125/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/20125/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/functional-python-programming.pdf
	Choose book (n for new search): n

	Seach for a book (q for exit): postgres
	1) PostgreSQL 9 Admin Cookbook [eBook]
	2) Learning PostgreSQL [eBook]
	Choose book (n for new search): 2
	1) https://www.packtpub.com/ebook_download/22041/pdf
	2) https://www.packtpub.com/ebook_download/22041/epub
	3) https://www.packtpub.com/ebook_download/22041/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/22041/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/learning-postgresql.pdf
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/6088/pdf
	2) https://www.packtpub.com/ebook_download/6088/epub
	3) https://www.packtpub.com/ebook_download/6088/mobi
	Choose url (c to cancel): c
	Choose book (n for new search): n

	Seach for a book (q for exit): science
	1) Practical Data Science Cookbook [eBook]
	Choose book (n for new search): n

	Seach for a book (q for exit): machine
	1) Practical Machine Learning [eBook]
	2) Machine Learning with R - Second Edition [eBook]
	3) Machine Learning with Spark [eBook]
	4) Python Machine Learning [eBook]
	5) Building Machine Learning Systems with Python [eBook]
	Choose book (n for new search): 6
	Wrong input, please try again
	Choose book (n for new search): f
	Wrong input, please try again
	Choose book (n for new search): 5
	1) https://www.packtpub.com/ebook_download/11703/pdf
	2) https://www.packtpub.com/ebook_download/11703/epub
	3) https://www.packtpub.com/ebook_download/11703/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/11703/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/building-machine-learning-systems-with-python.pdf
	Choose book (n for new search): n
	Seach for a book (q for exit): q
	Bye

And on the file system (some downloads were already there):

![packt-dl-manager]({filename}/images/packt-dl-manager.png)

Code is [here](https://github.com/pybites/100DaysOfCode/tree/master/072).

Bonus: if you want to do login with Selenium, we covered that [in our 100 Days Challenge too](https://github.com/pybites/100DaysOfCode/tree/master/066).

## PacktScraper

We got a nice PR from [wonderfulboyx](http://github.com/wonderfulboyx) scraping the free ebook site and offering email and tweet notification options, all modular and configurable with configparser. Check it out [here](https://github.com/pybites/challenges/tree/community/22/wonderfulboyx).

---

Great work is coming out of these challenges, we are humbled and stoked creating our PyBites community this way. Thanks for joining.

Remember there is no deadline, you can PR your code anytime. Just remember to isolate (branch) your changes and submit against our Community branch - see [our instructions](https://github.com/pybites/challenges/blob/master/INSTALL.md).

Come code with us forking [our challenges repo](https://github.com/pybites/challenges). Have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

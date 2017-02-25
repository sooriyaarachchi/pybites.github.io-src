Title: Create a Simple Web Scraper with BeautifulSoup4
Date: 2017-01-11 13:00
Category: Tools
Tags: python, tips, tricks, code, pybites, beautifulsoup, bs4, webscraping, namedtuple
Slug: simplewebscraper
Authors: Julian
Summary: Learn to create a simple web scraper in Python using BeautifulSoup4
cover: images/featured/pb-article.png

I absolutely loved the idea of web scraping when Bob explained what it was (it sounded so spy-like and hackery!). It did however sound like something that, coding-wise, was completely out of my grasp. Once I dove in and tried to create one though I realised it was actually quite simple!



## Concept

Create a web scraper that probes a site for the latest headlines.

For my example, I'm going to scrape [wowhead.com](http://wowhead.com), a World of Warcraft database site, for their latest news headlines.

Head to the *Wowhead* page and you'll see their home page is just a series of news/blog posts. What we want to do is pull the title of each blog post and output it to text.

(You can follow along with this or, of course, you can use your own site).


## The Setup

- Decide on the site to scrape.
- [Create a venv](http://pybit.es/the-beauty-of-virtualenv.html) to run all of this up in. I created a directory called "wowhead" for this and created the venv in that:

~~~~
# pwd
wowhead
# ls
venv	wowhead_scraper.py
~~~~

- pip install bs4 requests (Install the BeautifulSoup4 (bs4) and Requests modules)


## The Code

The final code for this simple scraper can be found in the [PyBites Code Repo](https://github.com/pybites/blog_code), subdirectory [BeautifulSoup](https://github.com/pybites/blog_code/tree/master/BeautifulSoup).

> Disclaimer: I've lumped everything under the main() function. This is a really simple program and I wanted to keep it as readable as possible, thus it's not all split into different functions.

- After the initial code setup of importing modules and defining main, the first task is to grab a copy of the site's html file:

~~~~
URL = "http://www.wowhead.com"
header_list = []

def main():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
~~~~

The *get* function of the requests module allows us to pull the HTML data from the site. We assign this data to the variable *raw_site_page*. (This is known as the **response** object).

As the comment implies, the *.raise_for_status()* function checks to see if the data was pulled successfully. If, for example, your URL is incorrect, this will error your program out and tell you about it.


- Next, Beautiful Soup fun:

~~~~
soup = bs4.BeautifulSoup(raw_site_page.text, 'html.parser')
~~~~

This code takes the Response object and reads it as plain text. BS4 parses it with the html parser and creates a **Soup Object** which we're assigning to the variable *soup*.


- Now the tricky part:

~~~~
html_header_list = soup.select('.heading-size-1')
    for headers in html_header_list:
        print(headers)
~~~~

We need to use the *.select()* function within BS4 to find what we want in the site HTML code. This is where you'll need to view the page source of the site ([or use Inspect](http://testingfreak.com/inspect-element-in-firefox-chrome-or-ie-browsers/)!) to find something unique about the data you want to pull.

You can see that I've specified the CSS Element ".heading-size-1". On the *Wowhead* page I found that each post heading contained this element and that it was unique to them as well.

We then take this selected data and create *html_header_list* with it.

- I've added a for loop to print the contents of the list. This is where I got caught the first time. Run the program and you'll see something similar to this (showing first line only):

~~~~
$ python3 wowhead_scraper.py 
<h1 class="heading-size-1"><a href="/patch-7-1-5-survival-guide">Patch 7.1.5 Survival Guide: Class Guides, New Legendaries, Brawler's Guild, Artifact Knowledge Catch Up and More!</a></h1>
~~~~

What's happening here is that I'm not only just getting the header of the post but also the URL assigned to by the "a href" HTML tag. We don't need this data for this exercise.

- We could use regex to strop the URLs out but BS4 makes it easier. We can grab just the plain text used within the CSS element using .getText():

~~~~
html_header_list = soup.select('.heading-size-1')
    for headers in html_header_list:
        header_list.append(headers.getText())
~~~~

Using .getText() we can then pull the plain text and append it to the *header_list* list.

- Now if we iterate over *header_list* we see just the data we want!

~~~~
for headers in header_list:
        print(headers)
~~~~

~~~~
$ python3 wowhead_scraper.py 
Patch 7.1.5 Survival Guide: Class Guides, New Legendaries, Brawler's Guild, Artifact Knowledge Catch Up and More!
Official Patch Notes for World of Warcraft 7.1.5
Kirin Tor Quest Fix, World Quest Reset in 7.1.5, Live Developer Q&A Thursday
The Story of Aviana - Lore Collaboration with Nobbel87
All The Demon Hunter Class and Legendary Changes in Patch 7.1.5
Wowhead Weekly #106 and Blizzard Gear Shop Diablo Sale
$ 
~~~~

## More examples (Bob)

[Here](https://github.com/pybites/blog_code/blob/master/BeautifulSoup/scrabble_distribution.py) is another example how to scrape [scrabblewizard.com](http://scrabblewizard.com/scrabble-tile-distribution/) to parse the html table that has the Scrabble tile distribution and load it into a data structure (list of named tuples).

[Titans books kata](http://bobbelderbos.com/2016/12/code-kata/) also used BeautifulSoup to scrape the page, see code [here](https://github.com/pybites/blog_code/blob/master/BeautifulSoup/titans_books.py).

## Areas for Expansion

Again, this is web scraping at its simplest. There are heaps of improvements and additions that can be made with these coming to mind right away:

- Pull the URL for each header and output that alongside the title.
- Automate the script to run (daily?) and store the output.
- Have the output emailed to you along with links to each post.
- Store the Request object in a local file so we don't have to keep making an HTML request every time we run the program.
- Store post headings in an external file to allow us to only send notifications when there's a *new* post.



## Conclusion

This was a pretty satisfying project for me. Web scraping has endless possibilities - you just need to figure out what you want and from where!

This example is as simple as they come but hopefully now you can see just how easy it really is.

Oh and if anyone tries to say, "Isn't that what the RSS feed or Subscribe button is for?", ignore them. This is *way* more satisfying!

Keep Calm and Code in Python!

-- Julian

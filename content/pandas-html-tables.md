Title: Next Time I Will Use Pandas to Parse Html Tables
Date: 2017-06-08 12:46
Category: Concepts
Tags: BeautifulSoup, regex, Pandas, parsing, data, data cleaning, energy, json, csv, html
Slug: pandas-parse-html-table
Authors: Bob
Summary: Last week I did some html table parsing with BeautifulSoup and regex. It turns out there is an easier way to do this: Pandas.
cover: images/featured/pb-article.png

Last week I did some html table parsing for our [Electricity Cost Calculation App challenge](https://pybit.es/codechallenge21_review.html). I used BeautifulSoup and regex. It turns out there is an easier way to do this: Pandas.

## Parsing html tables 

### Take 1: BeautifulSoup and regex

For our challenge I wanted to include a table of wattage uses of standard devices. I did not find any API so ended up with [Wholesale Solar's power table](https://www.wholesalesolar.com/solar-information/how-to-save-energy/power-table). 

However even having a great library like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) available it was still a pain parsing the html (see `get_appliance_wattages()` [here](https://github.com/pybites/challenges/blob/community/21/bbelderbos/data.py))

### Take 2: Pandas

Luckily I stumbled upon [this article](https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58) which shows you how to use Pandas' `read_html()` to grab tabular data from html pages. Very useful! Here is [a Jupyter notebook](https://github.com/pybites/100DaysOfCode/blob/master/070/pandas-html-tables.ipynb) applying it to the power table problem.

Although easy to use, I still had to do some data conversion in Pandas, because the table came with duplicated column names: 3 columns of Appliances and 3 columns of Watts.

So I did end up spending time on both methods, but the Pandas way is more extensible, because once you have the data in a [DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) you have a rich API to your disposal to do all kinds of data manipulations, like grouping, filtering and format conversion (to csv/json).

## The manual part: Data cleaning 

The take away is to use specialized libraries as much as possible. They have most of the common use cases figured out. 

However be it BeautifulSoup, regex or Pandas, there is always some data (manual) manipulation and cleaning involved. 

As you can see in the notebook, although Pandas took care of stripping the thousand separators, I still needed to manually manipulate/clean values like: `80-150` (average), `400-1000+` (strip), or `1080 watt-hours /day*` (normalize).

If you have a magic method for that let me know or if you want to share your data parsing story do so in the comments below, specially if it involved a lot of nasty manipulation and cleaning :)

I realize this would be an ideal code challenge too, if you agree, feel free to suggest one [here](https://github.com/pybites/challenges/issues).

---

Keep Calm and Code in Python!

-- Bob

Title: Module of the Week: Openpyxl - Automate Excel!
Date: 2017-09-12 10:50
Category: Modules
Tags: excel, games, first script, vba, automation, openpyxl
Slug: python-openpyxl
Authors: Bob
Summary: You probably remember your first script. I remember the joy of discovering how I could let the machine automate something for me. It still gets me excited everyday. I played a bit with openpyxl yesterday. I used it to hack an Excel game for which I first used a macro. Not particularly useful but a nice exploration of this useful module.
cover: images/featured/pb-article.png

You probably remember your first script. I remember the joy of discovering how I could let the machine automate something for me. It still gets me excited everyday. I played a bit with openpyxl yesterday. I used it to hack an Excel game for which I first used a macro. Not particularly useful but a nice exploration of this useful module.

## Hack the Game

I wondered how easy it was to redo an Excel (VBA) macro in Python. So I used one of my my first scripts to hack [this Excel game](http://juegosexcel.com/foro/viewtopic.php?t=6396). More info [here](https://bobbelderbos.com/2016/02/fired-up-about-programming/) including a story how I got into programming.

My first shot at it was [xlrd](http://www.lexicon.net/sjmachin/xlrd.html) because the game was in `xls` but it got messy. Not giving in easily, I asked Julian to save it to `xlsx` because I don't have MS Excel (thanks buddy). 

Attacking the problem with [openpyxl](https://openpyxl.readthedocs.io/en/default/) was a much greater experience. You can find the code [here](https://gist.github.com/pybites/e1c04368fd1bc994c6f2e3ef89e90dd4). 

What was fun and beyond the initial Macro solution:

- Apart from the 'save to xlsx' dependency it does not rely on macros, Python is more portable. It took me also far less time, even taking out the advantage of having more experience now.

- As far as I know with Macros you have the same issue of the game creator hiding the answers, I was surprised that in Python I could just get the answers from the formulas that were visible querying the cells with conditional formatting. 

	In that regard you might not even need Python as I could also get the answers out of the spreadsheet using unix' `strings` + data cleaning. See here the cities in the right (zig zag) order:

		$ strings ciudades.xls |grep -n -B10 -A300 AVILA | grep -B1 CORR | egrep -v 'CORR|CASI|^\-\-'|sed 's/.*[-:]//g'
		SANTANDER
		AVILA
		MURCIA
		BADAJOZ
		BILBAO
		SEVILLA
		...
		...

	Point being for as much as we love Python don't forget the power of Unix shell scripting for quick and one-off things!

- As often concluded here: don't reinvent the wheel, often you can [use a module](https://pypi.python.org/pypi). In this case the openpyxl module makes querying, updating and saving the workbook a breeze.

- The regex in `SOLUTION_FORMULA` was pretty useful to extract the destination cell and answer (city). Regexes are useful if you don't overdo them. We have [this resource](https://pybit.es/mastering-regex.html) if you want to learn more about them. We will also dedicate [a code challenge](https://pybit.es/pages/challenges.html) to regexes [at some point](https://github.com/pybites/challenges/issues/96) so you can practice them ...

- Another favorite of mine are [namedtuples](https://docs.python.org/3.6/library/collections.html#collections.namedtuple) which [make your code more readable](https://pybit.es/beautiful-python.html).

## Conclusion

Lessons learned:

- When using Python to work with Excel sheets it's probably best to go with the newer `xlsx` format so you can use openpyxl.

- Not all code exercises have to be useful per se. Apart from this article, with this exercise I got to practice just enough to feel confident doing more useful stuff with Excel + Python when needed.

- For some things you actually don't need Python.

- For me automating stuff has been (and still is) one of the best and most fun ways to learn coding.

## Call out to Finance / Excel folks

Let's do a challenge around this one! I logged [an issue](https://github.com/pybites/challenges/issues/104). If you have cool ideas what we can automate with Excel + Openpyxl update the issue. Thanks.

---

Keep Calm and Code in Python!

-- Bob

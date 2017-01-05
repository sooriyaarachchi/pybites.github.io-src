Title: Code Challenge #01 - code review 
Date: 2017-01-05 9:00
Category: Refactoring
Tags: challenge, refactoring, code review, best practices, pythonic, git, Github, git flow, vim, assert
Slug: challenge01_codereview
Authors: Bob
Summary: In this post I review the code of challenge # 1 and refactor it to make it more Pythonic.
cover: images/featured/code-challenge-refactoring.png

## Intro

First of all we have to praise Julian for learning by challenge, [submitting his code to github](https://github.com/pybites/blog_code/blob/1f4dc534d43ec2c8582a890a15fb54486b58af39/katas/course_time/js_course_time_scraper.py) for review, starting out as a coder this takes tremendous courage. Quick round of applause please ...

The flip-side though is that he will learn super fast his way, he is on his way to become a Python ninja :)

As described in [the previous article](http://pybit.es/js_time_scraper_ch.html) our first challenge was to:

> Parse a copy of the loggedin [practical JS course page](https://watchandcode.com/p/practical-javascript) calculating the total course time. We focussed on the html parsing, not scraping for now (we will use BeautifulSoup in a future post for sure!)

The submitted code is [here](https://github.com/pybites/blog_code/blob/1f4dc534d43ec2c8582a890a15fb54486b58af39/katas/course_time/js_course_time_scraper.py).

## Refactoring 1.0 - making it more Pythonic

Enter the code review.

Github's [history link](https://github.com/pybites/blog_code/commits/master/katas/course_time) lets you browse all the commits. This is very convenient and it shows the benefit (best practice) of making git commits as small as possible. This actually made it very easy to show all refactorings in chronological order, which I will do in a bit.

### Before we dive in ...

* Note that starting 5a34e5a, I ran the script before each commit to see if my assert would work (regression). 

	For convenience I use this shortcut in my .vimrc:

		nmap ,p :w<CR>:!python3.6 %<CR>
		
	I love this shortcut. This way I can just press comma+p and it saves the script and runs it, this saves a lot of cycles as you do this over and over (run tests -> refactor -> run tests). 
	
	Ah and yes, you [probably want to try 3.6 by now](http://pybit.es/3.6_new.html) ;)

* Secondly below could be picky (sorry), but I just want to point out as many things as possible to get the most out of this exercise.

* Again see the [history link](https://github.com/pybites/blog_code/commits/master/katas/course_time) or clone our [blog_code repo](https://github.com/pybites/blog_code) and go through it with:

		$ git log --oneline --reverse 66fb7c7fe..9876f968b
		$ git show <commit-hash>

## Commit by commit

* [1f4dc53 add jul challenge script](https://github.com/pybites/blog_code/commit/1f4dc534d43ec2c8582a890a15fb54486b58af39)
* [9dcbd27 added html to kata](https://github.com/pybites/blog_code/commit/9dcbd27ed348a5d9da0f9e68e2164fcfb7a7a6cd)

	First I added the script to our [katas](https://github.com/pybites/blog_code/tree/master/katas) folder of our [blog_code repo](https://github.com/pybites/blog_code) and the copy+paste of the page content.

* [ce498d7 add assert for regression](https://github.com/pybites/blog_code/commit/ce498d71e0316b2ecf7c4c9884fb988ba3a32c5d)

	When you refactor always have your tests at hand to make sure you don't mess anything up. This was just a small script so an assert was enough, whatever you use (unittest, pytest, ...) the tests need to perform fast, because you run them often (every step).

		assert str(total_hours) == '6.841944444444445'
	
* [5a34e5a add calling code in main](https://github.com/pybites/blog_code/commit/5a34e5a7d4ff1bf2251851aabc18c736a62aeecc)

	I added the [Top-level script environment](https://docs.python.org/3/library/__main__.html) to prevent the prints to run if the module is imported: 

		if __name__ == "__main__":
		...

* [dad9b55 no need to pass file around, we have a constant](https://github.com/pybites/blog_code/commit/dad9b5537a989a1aed02a61f685ead874e12794e)
	
	The search_file() method was called with an argument called 'file', but the constant 'HTML_FILE' was already defined, so could just use that.

* [9d682fa extract time_regex into constant](https://github.com/pybites/blog_code/commit/9d682fa943bf3ab461b6f48dba50b646491b12e5)

		time_regex = re.compile(r'\(\d+:\d+\)')

	This was defined in search_file, being a constant I moved it to the top of the file and used PEP8's uppercase convention:

		TIME_REGEX = re.compile(r'\(\d+:\d+\)')

* [57334a6 use open in with block to auto-close file handle](https://github.com/pybites/blog_code/commit/57334a65de1b8a01aa852f222141f9e36e0a558c)

	open(HTML_FILE).read() was used without close(). Best practice for reading files is using a with block (aka [contextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)): 
	
		with open(HTML_FILE) as f:
	 		...

* [1147bd0 no need for range, can just loop over duration iterator](https://github.com/pybites/blog_code/commit/1147bd08424a1c638661bc840bf6851c8d579873)

	This is probably an inherited C (or other language) style:

		for i in range(len(durations)):
			minutes, seconds = durations[i].strip('()').split(':')

	No list indexing needed, in Python you can just iterate over a sequence very easily with:

		for mm_ss in durations:
			minutes, seconds = mm_ss.strip('()').split(':')

* [bc6ee8a can use shortcut += for summing](https://github.com/pybites/blog_code/commit/bc6ee8a93a4f622687f8811ed571da1ef30c38c7)

		sum_minutes = sum_minutes + int(minutes)

	can be shortened to:

		sum_minutes += int(minutes)

* [9ff89d1 better method name for getting all timestamps](https://github.com/pybites/blog_code/commit/9ff89d123165167c0fde3f0163f1e54fca2f22c3)

	I renamed method search_file() to get_all_timestamps() to better express what it does.

* [f5db013 no need to predeclare time_list at module level](https://github.com/pybites/blog_code/commit/f5db0134ec7e614e9992720fca5dea5cd15f2e12)

	time_list = [] declaration at the top was redundant.

* [f862652 one return value from time_calculation, so convert all to seconds](https://github.com/pybites/blog_code/commit/f86265222406cd83da4836e4207d99d4be9e9e2c)

	time_calculation() returned minutes and seconds, it's best practices to have one return value from a function, so I refactored it to count seconds. Of course I had to update the prints in __main__, but this commit made the design cleaner.

* [752394b match method name last refactoring](https://github.com/pybites/blog_code/commit/f86265222406cd83da4836e4207d99d4be9e9e2c)

	Renamed time_calculation() to calc_duration() which I found a bit more concise.

* [026b9c5 update comments after last refactoring](https://github.com/pybites/blog_code/commit/026b9c545250247981382d4c31b6327b11113b94)

	Deleted 'min(s)' (minutes) from comments as we went for second counting only since commit f862652.

* [e4fad91 strip comments as code is pretty self explanatory](https://github.com/pybites/blog_code/commit/e4fad918f34174d58889916a85cfe6972b3db467)

	Decided to strip comments completely because the code expresses well what it does.

* [76d1b29 strivariable rename](https://github.com/pybites/blog_code/commit/76d1b297ede0871fe285babe6e841dc532e62eaf)

	Oops on the commit message. Renamed time_list to video_timings to better express what the variable stores.

* [d026a7f do adding/summing on one line](https://github.com/pybites/blog_code/commit/d026a7f0c7999821e07b16a46255207e6ccd0da4)
	
		sum_seconds += int(minutes) * SECONDS_IN_MIN
		sum_seconds += int(seconds)

	was still happening twice, so made that a one-liner:

		sum_seconds += int(minutes) * SECONDS_IN_MIN + int(seconds)

* [e45ce53 extract colon seperator into constant](https://github.com/pybites/blog_code/commit/e45ce53e3407e25a648225829f2086e8a9020011)

	When I see any literal values, either numeric or strings, I extract them into constants:

		MM_SS_SEP = ':'

* [9876f96 removed whitespaces to comply with pep8 (used flake8 vim plugin)](https://github.com/pybites/blog_code/commit/9876f968b49745b599e4bc9716802677956c8b46)

	Lastly I ran flake8, which we mentioned [in our PEP8 article](http://pybit.es/pep8.html), to check for style violations, in this case only some whitespaces and a blank line.

## Conclusion

Julian, very well done on the challenge man, you are making good progress.

I hope this inspires you and the readers to think about making code as Pythonic and clean as possible, because the extra time upfront saves a lot of time later on.

Any feedback or questions use the comments below, or if code specific: use the comment box Github has for each commit. 

These refactorings are suggestions, I am learning too, so any improvements are welcome ...

## About Code challenges

As [Julian explained](http://pybit.es/js_time_scraper_ch.html):

> Bob and I thought it'd be interesting to do some code challenges. That is, Bob specifies the challenge and I complete it. Bob then goes through my code and makes any necessary edits/improvements to make it more Pythonic.

We plan to do a code challenge here once a week. Stay tuned.

If you like this subscribe below of follow us on [Twitter](https://twitter.com/pybites). Thanks for reading.

---

Keep Calm and Code in Python!

-- Bob

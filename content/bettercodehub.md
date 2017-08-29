Title: Improve the Quality of Your Code with Better Code Hub
Date: 2017-08-30 00:29
Category: Tools
Tags: bettercodehub, SIG, refactoring, code quality, clean code, software development, tools, platform
Slug: bettercodehub
Authors: Bob
Summary: So you pushed your code to GitHub and deployed v1, congrats! But how maintainable is your code really? Do you have tests? Is your code modular? Are your methods short and concise? What if you could hit a button and a tool conveniently checks this for you? Free and integrated with GitHub? Enter [Better Code Hub](https://bettercodehub.com) from [Software Improvement Group](https://www.sig.eu/) ...
cover: images/featured/pb-article.png
status: draft

> Better Code Hub guides you in writing Better Code. - [BCH Homepage](https://bettercodehub.com/)

So you pushed your code to GitHub and deployed v1, congrats! But how maintainable is your code really? Do you have tests? Is your code modular? Are your methods short and concise? What if you could hit a button and a tool conveniently checks this for you? Free and integrated with GitHub? Enter [Better Code Hub](https://bettercodehub.com) from [Software Improvement Group](https://www.sig.eu/) ...

![Better Code Homepage]({filename}/images/sig-bch-1.png)

## What is Better Code Hub?

You can read a nice introduction about the tool on their blog:

* [Higher Grades for Better Code](https://medium.com/bettercode/higher-grades-for-better-code-23183648f793) which defines the tool as:

	> This newly-built software platform enables users to check the compliancy of software systems with the 10 guidelines for Maintainability introduced in the Building Maintainable Software book.

* And: [Better Code Hub - An ambitious yet achievable Definition of Done for Code Quality](https://medium.com/bettercode/better-code-hub-70f261a86fc7). This is a nice read to learn about the motivation behind the platform: 

	* First of all as [Marc Andreessen famously said](https://a16z.com/2016/08/20/why-software-is-eating-the-world/): *Software is eating the world*: every industry gets disrupted by software hence each company will become a software company.
	* Secondly GitHub has become the *biggest collaborative developer platform* with over 10 million repositories!

	> This triggered us to create the Better Code Hub, an online service that puts 15 years of code quality knowledge at the disposal of all GitHub developers.

It supports 14 programming languages, can run upon each Push or PR, and shows refactoring candidates with their impact. Last but not least: Better Code Hub provides software teams a Definition of Done, in their words:

> If Better Code Hub compliance is achieved, you know you’re performing like the top teams in the industry. This is because the compliance thresholds are derived from a large industry and open-source benchmark that is calibrated yearly in our software laboratory to capture the state-of-the art in software engineering.

BCH has a nice design and a "zero set-up time": just login with your GitHub account and it shows your public repos you can analyze: 

![My Github Repositories]({filename}/images/sig-bch-2.png)

At this point you can run the Analyze (play) button and SIG's tool checks the quality of you code.

## What does it check?

BCH will check your code against their 10 guidelines for maintainable software:

1. Write Short Units of Code - *Short units are easier to understand.*
2. Write Simple Units of Code - *Simple units are easier to test.*
3. Write Code Once - *Duplicated code means duplicated bugs and duplicating changes.*
4. Keep Unit Interfaces Small - *Units with small interfaces are easier to reuse.*
5. Separate Concerns in Modules - *Modules with a single responsibility are easier to change.*
6. Couple Architecture Components Loosely - *Independent components can be maintained in isolation.*
7. Keep Architecture Components Balanced - *A balanced architecture makes it easier to find your way.*
8. Keep Your Codebase Small - *A small codebase requires less effort to maintain.*
9. Automate Tests - *Automated tests are repeatable, and help to prevent bugs.*
10. Write Clean Code - *“Leave the campground cleaner than you found it.”*

These guidelines are based on an impressive body of experience:

> Compliance to guidelines is derived from the Software Improvement Group's [industry benchmark](https://www.sig.eu/files/en/090_Deriving_Metric_Thresholds_from_Benchmark_Data.pdf) which consists of over 8 billion lines of code in more than 180 different technologies.  SIG analyzes around 15 million lines of code every week. - [Better Code Hub Homepage](https://bettercodehub.com/)

For more info I highly recommend [their book](http://www.amazon.com/dp/1491953527/?tag=pyb0f-20). They have a certification program which I described [here](https://bobbelderbos.com/2016/07/certified-software-quality/) and I made this [summary of the guidelines](https://bobbelderbos.com/2016/03/building-maintainable-software/) when I was studying for the exam. 

Although we are a Python blog we wanted to discuss the tool here, because as [Eric Elliott's tweeted](https://twitter.com/_ericelliott/status/893264008438046720):

> Frameworks and APIs change fast. Software design principles are evergreen. Learn principles that translate across language barriers. 

Luckily Python (and its community) endorses a lot of good practices (`import this` folks!)

And we used it for a recent Code Challenge ...

## A practical example

I used the tool recently for our [Code Challenge 30 - The Art of Refactoring: Improve Your Code](https://pybit.es/codechallenge30.html):

At first I wanted to work on an old un-Pythonic script. Problem was: it would have been easy and some scripts are better dead and buried. So I thought: 

> Let's do something real, something that we use and has to be mainained! 

Hence I decided to use this challenge to refactor our [Karmabot](https://github.com/pybites/karmabot). 

> Heck, why not make it more robust now?! (Zen of Python: *Now is better than never.*)

It scored a meager 6 on [Better Code Hub](https://bettercodehub.com), hence it could use some work ...

![sig score before]({filename}/images/sig-score-before.png)

### The refactoring process

1. First I added unittests to have a regression suite.

    Dealing with an external API (Slack) made this a challenge on its own, but luckily [this awesome RealPython article](https://realpython.com/blog/python/testing-third-party-apis-with-mocks/) made it relatively easy.

2. Then I clicked BCH's Analysis button on the repo. Its guidance and rich UI made it a joyful experience. I refactored more than I anticipated making the solution leaner and better maintainable (although not as granular commit history [here](https://github.com/pybites/karmabot/commits/master) for reference).

### Examples of what BCH caught:

No tests!

![no tests]({filename}/images/testcov-before.png)

OK that's better, now we can actually start refactoring!

![now with tests]({filename}/images/testcov-after.png)

Tackling complexity: 

![Better Code Homepage]({filename}/images/sig-bch-flag1.png)

Various issues here: number of branch points, 3 method (interface) params and violation of the [*Single responsibility principle*](https://en.wikipedia.org/wiki/Single_responsibility_principle). This example led to various refactorings even [changing part of the karma module into a class](https://github.com/pybites/karmabot/blob/master/bot/karma.py).

Although not the final result, BCH made the refactoring progress very visual:

![Better Code Homepage]({filename}/images/sig-bch-flag2.png)

When I thought I was done BCH still pointed out I should "Couple Architecture Components Loosely". It turned out `main.py` and `karma.py` were too entangled:

![sig score after]({filename}/images/sig-graphs.png)

Moving `_process_karma_changes` from `main.py` to `karma.py` solved this. 

![code in the wrong module]({filename}/images/sig-bch-balance-comps.png)

It felt like everything fell into place, probably due to earlier refactorings. This was one of those *aha moments*.

And the final result:

![sig score after]({filename}/images/sig-score-after.png)

Lastly SIG made a nice badge you can add to your Project's README:

![sig badge]({filename}/images/sig-badge.png)

## Try it out!

Some code to refactor? Or starting a brand new project? Try this tool out and let us know what you think in the comments below. 

You can follow / reach out to them [on Twitter](https://twitter.com/bettercodehub).

For above mentioned and other interesting articles check out [their Medium page](https://medium.com/bettercode).

And above all keep learning and growing. Writing quality code is hard and takes a lot of practice ([I am no expert, I am the student](https://twitter.com/pybites/status/902556188860194816)). 

A final word of thanks. I feel fortunate to be able to learn from SIG's body of experience and knowledge and their new platform that brings their SW quality guidelines to the greater community. Great job SIG!

---

Keep Calm and Code in Python!

-- Bob

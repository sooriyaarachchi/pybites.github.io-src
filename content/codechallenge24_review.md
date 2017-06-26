Title: Code Challenge 24 - Use Dunder / Special Methods to Enrich a Class - Review
Date: 2017-06-26 10:00
Category: Challenges
Tags: codechallenges, dunders, special methods, magic methods, classes, polymorphism, operator overloading, guest
Slug: codechallenge24_review
Authors: PyBites
Summary: In this article we review last week's [Use Dunder / Special Methods to Enrich a Class](http://pybit.es/codechallenge24.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Use Dunder / Special Methods to Enrich a Class](http://pybit.es/codechallenge24.html) code challenge we coupled to [our guest post](https://dbader.org/blog/python-dunder-methods) on Dan Bader's blog.

### Account class

First of all you can follow along with the code in the article [here](https://github.com/pybites/dunders) (class and notebook). One thing we learned from the comments on the article is that \_\_reversed\_\_ should reverse the normal iteration. So newest to oldest, not by transaction amount ([fix](https://github.com/pybites/dunders/commit/fced4f1f9a22270eb57bf3342289568e5ed7f113))

### Submissions

As there were no PR submissions other than ours we keep it short. 

We made a [Developer class](https://github.com/pybites/challenges/tree/community/24/bbelderbos) pretty similar to the Account class example. 

Funny fact is it was meant for our new [Karma Bot](https://github.com/pybites/karmabot) but [we implementing it without using dunders](https://pybit.es/slack-karma-bot.html)! So it is good to note that you don't always need them. 

Even a word of caution is warranted as pointed out by *\_seemethere*  on the article's [Reddit thread](https://www.reddit.com/r/Python/comments/6ih6cj/enriching_your_python_classes_with_dunder_magic/):

> I would say that you should be careful with magic methods.

> On one hand they can be extremely useful and extend your objects and on the other hand they can make using your library very difficult and hard to understand.

> Use them where you feel as though they make sense and not just because it would be cool to use.

Useful tool, powerful and elegant, but use wisely.

### Next

Stay tuned for this week's code challenge where we get you to code up a weekly digest email of now playing/ upcoming movies or series.

By the way there is no deadline to these challenges, you can start any challenge at any time. 

Just follow [our instructions](https://github.com/pybites/challenges/blob/master/INSTALL.md) and start coding. Have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

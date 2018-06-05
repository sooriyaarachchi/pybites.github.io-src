Title: PyBites Module of the Week - Pendulum 
Date: 2017-06-24 09:00
Category: Modules
Tags: python, tips, code, pybites, pendulum, datetime, pytz, timezones 
Slug: pendulum 
Authors: Julian
Summary: A brief overview of the Pendulum datetime module.
cover: images/featured/pb-article.png

I’ll come clean. When it comes to Python datetime, I’m a shocker! I always struggle with the whole formatting side of things.

This week, I discovered the Pendulum Package and I swear I heard angels sing.

<br>
##What is Pendulum?

Let’s be clear, we’re not talking about one of my [favourite bands](https://en.wikipedia.org/wiki/Pendulum_(drum_and_bass_band))!

Pendulum is a Python Package designed to make the manipulation of Python datetimes easier.  In some cases, you can even totally replace every instance of `datetime` in your code with `pendulum` and the code should still work.


<br>
##Usage

There are so many cool functions and use cases which (unfortunately for this article) are explained clearly and thoroughly in the [Pendulum Documentation](https://pendulum.eustace.io/docs/). I’m not going to bother copying and pasting so I strongly urge you to check it out.


<br>
##My Favourite Uses

The first thing I’ll point out is that Pendulum has a wonderfully simplistic way of describing what each function does. Take the following for example:

~~~~
now = pendulum.now()
print(now)
'2016-06-28T16:51:45.978473-05:00'

today = pendulum.today()
print(today)
'2016-06-28T00:00:00-05:00'

tomorrow = pendulum.tomorrow('Europe/London')
print(tomorrow)
'2016-06-29T00:00:00+01:00'

yesterday = pendulum.yesterday()
print(yesterday)
'2016-06-27T00:00:00-05:00'
~~~~

This is taken straight from the docs. I’m just making a point. How simple is that to read? `.tomorrow()` and `.yesterday()` are super useful!

On top of that, you can even specify the timezone of the place you want to know the time of, thus the `.tomorrow(‘Europe/London’)` line.

<br>

My absolute favourite Pendulum feature is this:

~~~~
>>> pendulum.now().to_datetime_string()
'2017-06-24 09:35:38'
>>>
>>> pendulum.now().to_day_datetime_string()
'Sat, Jun 24, 2017 09:36 AM’
>>>
~~~~

Pendulum has a brilliant set of formatting options for datetime results. No longer do I need to use the convoluted and hard to remember `strftime` type formatting method (%D %M %Y). Pendulum will do it all for me! Mmmm.

<br>
On top of all of this, I feel like date comparisons, calculations and timezone manipulation has also been made easier. For example, you can create a Pendulum instance with a specified timezone and time, then change the timezone for it on the fly with ease:

~~~~
in_paris = pendulum.create(2016, 8, 7, 22, 24, 30, tz='Europe/Paris')
'2016-08-07T22:24:30+02:00'
in_paris.in_timezone('America/New_York')
'2016-08-07T16:24:30-04:00'
~~~~

<br>
There are even more advanced functions when it comes to calculations (addition and subtraction). You can easily add/subtract days, months, years, hours, minutes and seconds. Totally awesome!

<br>
##Conclusion

I’m now using Pendulum for all of my datetime needs. I’m sure the datetime module is capable of doing many of the jobs I’ve mentioned but again, I’ve always found it confusing and tedious.

Pendulum makes things even more [human readable](https://pendulum.eustace.io/docs/#difference-for-humans) and approachable (for me anyway!).

Thanks to [Sébastien Eustace](https://github.com/sdispater) for this wonderful package!

Keep Calm and Code in Python!

-- Julian

Title: First Steps Learning Django: PyPlanet Article Sharer App
Date: 2017-07-17 13:00
Category: Django
Tags: Django, 100DaysOfDjango, Planet Python, Twitter, tutorials, resources
Slug: learning-django
Authors: Bob
Summary: In this post I share my first steps exploring Django. I created [PyPlanet Article Sharer Django App](https://github.com/pybites/pyplanet-django) to make it easier for us to share new [Planet Python feed](planetpython.org) articles. It loads in new articles and generates tweet links. It lets us mark each entry as Shared or Skipped. I am sure this will faciliate our [Twitter activity](https://twitter.com/pybites) and [News Digests](https://pybit.es/pages/news.html). This is our first project of our [100 days of Django](https://pybit.es/special-100days-of-code.html) and our very first Django app overall!
cover: images/featured/pb-article.png

In this post I share my first steps exploring Django. I created [PyPlanet Article Sharer Django App](https://github.com/pybites/pyplanet-django) to make it easier for us to share new [Planet Python feed](planetpython.org) articles. It loads in new articles and generates tweet links. It lets us mark each entry as Shared or Skipped. I am sure this will faciliate our [Twitter activity](https://twitter.com/pybites) and [News Digests](https://pybit.es/pages/news.html). This is our first project of our [100 days of Django](https://pybit.es/special-100days-of-code.html) and our very first Django app overall!

## The app

Homepage:

![pyplanet-django1.png]({filename}/images/pyplanet-django1.png)

Click on an article and click "Mark Skipped":

![pyplanet-django2.png]({filename}/images/pyplanet-django2.png)

Redirects back to index and shows (CSS) article marked as skipped:

![pyplanet-django3.png]({filename}/images/pyplanet-django3.png)

Another article: 

![pyplanet-django4.png]({filename}/images/pyplanet-django4.png)

Tweet it and mark it complete (still 2 steps):

![pyplanet-django5.png]({filename}/images/pyplanet-django5.png)

Index now shows a skipped and a shared article:

![pyplanet-django6.png]({filename}/images/pyplanet-django6.png)

## Try it yourself

I made a [README](https://github.com/pybites/pyplanet-django) with instructions to run this project yourself.

As stated in the README some things still need to be done:

* Deploy to Heroku or PythonAnywhere.

* Add `importfeed` command to a daily cronjob.

* Add user authentication and tracking who (Julian / myself) edits what. I did already manage to setup a ForeignKey relation to the existing (admin) User table - Django comes with batteries included.

* Would be nice: integrate Twitter API so green "Mark Shared" button can be made redundant (could not find callback in Twitter's intent link, so Tweet + "Mark complete" are two steps now). Of course this requires the app to be behind a login.

## Learning

- Although this is a relatively simple app it touches on a lot of Django aspects: DB, ORM, migrations, views, templates, url routes, even a [custom django-admin command](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) I wrote to import the feed (`importfeed`). 

- Learning Django can be daunting, there are a lot of moving parts. So I strongly recommend to build something small and simple first.

- The directory structure and projects vs apps might be confusing at first, but it starts to make more sense as you go. It makes for flexible and extensible projects. 

- My first impression overall is that Django has a robust and elegant design. OK I am not going into Django vs Flask, each has its own use cases. So far I like them both (and Julian loves Flask so I better watch out ...)

- I learned my first baby steps [reading the famous create-a-poll tutorials](https://docs.djangoproject.com/en/1.11/intro/). I referred back to them while writing the app. This worked pretty well for me. The Django docs are excellent: complete, concise, using dev best pratices, written by developers for developers. And up2date (!) which eliminates a lot of potential issues.

- I ended up reading quite a bit on my phone thanks to the [well-formatted epub](https://media.readthedocs.org/epub/django/1.11.x/django.epub). Don't read the entire thing (it would take you weeks if not months), however I did some early exploration on the models (ORM), migrations and QuerySets (how to query the DB) sections, which was quite useful. 

- As we said in [our Python resources article](https://pybit.es/python-resources.html) best is to iterate through practice and reading: *Read some more, try new things you learn in your code. Repeat.*

- Last but not least it was not easy at first. I got stuck a couple of times and luckily there was Stackoverflow ([here](https://stackoverflow.com/questions/24013531/django-model-using-auth-group-as-a-foreignkey) and [here](https://stackoverflow.com/questions/33086444/django-1-8-migrate-is-not-creating-tables), and a bunch of other issues I ran into). 

- Having some Flask and web development experience under my belt did help a lot understand Django's structure and workflow better. So any Flask you do before jumping on Django will be beneficial. It feels like learning Italian after Spanish.

- Getting this out there and understanding the overall Django workflow and how the pieces fit together was extremely satisfying. It created momentum to keep going extending this app and build a more complex app. 

- My next app will be a complete rewrite of [fbreadinglist](http://fbreadinglist.com/) aka *nuke PHP and FB API for good and make an attractive and maintainable reading app your friends will thank you for* - luckily we have Django now :)

## Resources

- In spite of having the docs closeby at all times, from a didactic standpoint I did start reading a Django book cover-to-cover: [Django Unleashed](https://www.amazon.com/dp/0321985079/?tag=pyb0f-20). I hope 1.8 (book) vs 1.11 (latest) won't get me into trouble, but if so that could be good learning too. 

- Another book I often hear mentioned as one of the best in the field is: [Two Scoops of Django](https://www.amazon.com/dp/0692915729/?tag=pyb0f-20). 

- If you want team training check out Trey Hunner's [Truthful Technology](http://truthful.technology).

We will probably write a dedicated resources post when we get further into [our 100 Days of Django](https://pybit.es/special-100days-of-code.html).

## Feedback

Comments, questions, ideas are welcome. Use the comments below or reach out [via Twitter](https://twitter.com/pybites) or <a href="mailto:pybitesblog@gmail.com">email</a>.

---

Keep Calm and Code in Python!

-- Bob

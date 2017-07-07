Title: From Challenge to Project - How I Made PyTrack, Learning Modules and Packaging
Date: 2017-07-07 08:45
Category: Learning
Tags: challenges, guest, PyTrack, packaging, peewee, click, maya, learning
Slug: guest-pytrack-app
Authors: Martin
Summary: This is a guest post by Martin, a passionate Pythonista who turns our code challenges into cool projects. In this article he describes his process of building [pyTrack](https://github.com/clamytoe/pyTrack/), a simple task time tracker. Not only did he learn various Python modules - PeeWee, Maya and Click - he also stunned us delivering a project with great documentation and properly packaged code. 
cover: images/featured/pb-article.png

> Lessons learned during the making of pyTrack

This is a guest post by Martin, a passionate Pythonista who turns our code challenges into cool projects. In this article he describes his process of building [pyTrack](https://github.com/clamytoe/pyTrack/), a simple task time tracker. Quoting the Readme:

> pyTrack helps you keep track of how much time you spend on your projects and tasks. A sqlite database is used to track your time logs, and it is kept simple by only implementing as few commands as needed to get a full featured application. You can add/remove multiple projects, start/stop tracking any of them, or completely reset the database to start with a clean slate.

Not only did he learn various Python modules - PeeWee, Maya and Click - he also stunned us delivering a project with great documentation (check out [the README](https://github.com/clamytoe/pyTrack/blob/master/README.md)!) and properly packaged code. 

Enter Martin:

## PyBites Challenge #23

When I first heard about [this challenge](https://pybit.es/codechallenge23.html), my interest was immediately peaked. It sounded like something that I could use myself on a regular basis. I knew from the get go that I wanted to use [Maya](https://github.com/kennethreitz/maya) for keeping track of the timestamps so I installed it and got to work. Things were going great: I wrote up my classes and was able to create objects and save timestamps, pull them back out and get time intervals and such.

It seemed like a relatively simple challenge. I knew that I needed a database back-end and didn't want to use [SQLAlchemy](https://www.sqlalchemy.org/) again, so I decided to up the stakes a bit by using [PeeWee](https://github.com/coleifer/peewee) ORM. 

I'm usually able to figure things out by checking the docs and playing around with the code. Time was not on my side this time though so I could only work on this sporadically over a couple of weeks. It was hard going at first. I mostly struggled with getting to know how to use PeeWee. Maya on the other hand was relatively easy to pick up.

## PeeWee and Maya

One thing was certain: all of the work that I had already put into creating the classes and tests for this would have to be tossed and replaced with the class models for *PeeWee*...

Figuring out a one-to-many relationship was one of my first hurdles. I read the docs a bit and looked at some quick tutorials. They were very basic, so my implementation ended up basic. I recently came across [Adnan's Random bytes](http://blog.adnansiddiqi.me/develop-database-driven-applications-in-python-with-peewee/) blog, that would have came in really handy when I was first developing this. The way he sets his relationships is how I should have done it.

Another thing that threw me off was not being able to save *MayaDT* objects into the database. Only I didn't realize that it was the problem that I was having! The error messages from PeeWee were really cryptic and hard to follow.

After a few days of cursing and messing around with it, it finally hit me! *PeeWee* was expecting me to store *datetime* objects because that's what I had declared them as in the models! As soon as I converted the *Maya* objects into the correct format, I was able to get the ball rolling.

```bash
timestamp = now().datetime()
```

The next issue was when I would pull those timestamps back out to get my time intervals, *Maya* was not having it. Fortunate for me, the author of *Maya*, had already solved that problem. Instead of using the normal *MayaInterval()* I had to do it this way:

```bash
interval = MayaInterval.from_datetime()
```

Now you would think that would be it, but no, that introduced another issue. See, with the normal *MayaInterval* method, your local timezone is automatically determined and taken care of. Not so with the *.from_datetime()* one. It took me a while to figure out why it was failing when it had all been working before the addition of *PeeWee*.

It turns out that I couldn't simply just use the *datetime* entries that I had placed into the database. I had to first get the timezone and then feed that into *.from_datetime()*. The timezone object has many properties, the one that I was interested in was **zone**.

```bash
# set local timezone
timezone = get_localzone()
local_tz = timezone.zone

# import datetime objects from database
...

# parse them into the proper formats
start = parse(log.start_time).datetime(to_timezone=local_tz, naive=True)
stop  = parse(log.stop_time).datetime(to_timezone=local_tz, naive=True)

# get the interval
duration = MayaInterval.from_datetime(start, stop).timedelta
```

The *timedelta* converts the interval object into *0:00:00* format, which is exactly what I wanted.

> Note from PyBites: we definitely recognize this kind of struggle using new modules and technologies. This is why we encourage learning by code challenges. Reading a book about technology only gets you so far. It's when you start *using* the technology that you run in many (context) specific issues. This can be frustrating, but practice enough and you will be on your way to mastery. We think Martin's *pyTrack* is a great example of this.

## User interface - plan ahead!

Once everything was working smoothly, I remembered that I wanted to make this into a command-line utility. 

A common mistake is to just start coding which often leads to having to rewrite a lot of your code. In that regard I think next time I’ll build out the command-line interface first and then add the code for it. 

I started to add [Click](https://github.com/pallets/click) to get the CLI functionality. I had already used Click before so I thought that it would be pretty easy to add it as an afterthought. Boy was I wrong!

Let's just say that I patched it onto my existing code but then had to refactor the whole thing out once again so that the command-line portion of the code would be its own separate file. This will make it easier to add a GUI later on, if I get the motivation to do it.

My biggest roadblock here was in trying to get the project listing to show whenever no arguments were passed. None of the documentation or tutorials that I found showed how to do this. Took me a while to figure out that you have to call the method that starts off *Click* and since every example that I ran into in the wild started out that way, I thought it was a requirement.

I modified my main function so that it would look for command-line arguments and take action appropriately.

```bash
...
        if len(argv) > 1:
            cli()
        else:
            _ = get_projects(display=True)
...
```

I have that portion of the code wrapped in other code that opens and closes the connection to the database. I found it easier to do it this way instead of using function decorators.

## Packaging
Last but not least came time to package the whole thing. PyBites wrote up [an excellent tutorial](https://pybit.es/python-packaging.html) on how to do it, so I won't repeat it here. I actually learned from it myself and implemented some of it on this project, so go and have a read.

I should also give a shout out to [Dan Bader](https://twitter.com/dbader_org) and thank him for his excellent [README-Template for your GitHub project](https://dbader.org/blog/write-a-great-readme-for-your-github-project), which I use on every single project that I write. It takes your documentation from being so so, up to pro level!

I haven’t covered a lot about actually using my project. I think I did a pretty good job of explaining how it works in the [README](https://github.com/clamytoe/pyTrack), so check it out for yourself and feel free to contact me with any suggestions on how to improve it.

One more bit of advice when starting your own projects. Do a quick **pip** search for your potential project name.

```bash
pip search pyTrack
```

I wasn't planning on pushing this out to [pypi](https://pypi.python.org/pypi), but now that I'm considering it I'm running into the problem that **pyTrack** is already taken! Not only will I have to come up with a new name, but I'm also going to have to rename my GitHub repo to reflect the change.

Conclusion: put in a little bit of leg work at the beginning and save yourself the hassle. 

---

As always, Keep Calm and Code in Python!

-- Martin Uribe

> Martin is a ten year Army Veteran, turned Field Support Technician in the IT and Services Industry, who likes to code on the side to make his daily tasks easier. You can follow him on [Twitter](https://twitter.com/mohhinder) and [GitHub](https://github.com/clamytoe).

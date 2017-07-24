Title: Deploying a Django App to PythonAnywhere
Date: 2017-07-23 23:59
Category: Django
Tags: Django, 100DaysOfDjango, PythonAnywhere, Security, cloud, deployment
Slug: django-python-anywhere
Authors: Bob
Summary: After Julian's great article [on deploying a Flask app to Heroku](https://pybit.es/deploy-flask-heroku.html), let's look at how we can deploy a Django app to [PythonAnywhere](https://www.pythonanywhere.com) (PA).
cover: images/featured/pb-article.png

After Julian's great article [on deploying a Flask app to Heroku](https://pybit.es/deploy-flask-heroku.html), let's look at how we can deploy a Django app to [PythonAnywhere](https://www.pythonanywhere.com) (PA).

In this article a few things I learned deployed our [first Django app](https://pybit.es/learning-django.html) to PA.

### Good docs + nice interface

One of my first tries was the [API / helper script](https://blog.pythonanywhere.com/155/), but unfortunately it did not make it to the end. Yet the [Deploying an existing Django project on PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) using the Manual option worked great for me:

![pa choose manual option]({filename}/images/pa-maual-option.png)

Our first Django app [is online](http://pybites.pythonanywhere.com/pyplanet/):

![pa site online]({filename}/images/pa-online.png)

I really like the infrastructure of browser consoles and intuitive GUIs. Also config files like `wsgi.py` were clearly commented so setting it up was quick and almost painless.

### Git + venv

Import steps of the deployment steps are git pulling your code and creating a virtual env, this worked very well.

![pa supports git and venv]({filename}/images/pa-git-venv.png)

After this step I could just do a `pip install -r requirements.txt` to install Django and feedparser.

Now when I make changes to my app I can just do a `git pull` in the repo dir and restart the app in the browser. It just takes seconds :)

### Scheduled tasks ... OK time to upgrade

Our app pulls in new articles from Planet Python as explained [here](https://pybit.es/learning-django.html). Planet was not on [PA's whitelist](https://www.pythonanywhere.com/whitelist/) and I wanted this task to be run every hour (instead of once a day). At this point I had to upgrade from Free to the *Hacker tier*. This has additional benefits, check out [pricing](https://www.pythonanywhere.com/pricing/). 

Similar to other providers, at PA you pay for what you need/ consume. You can add apps on the fly. I'd hoped to get a small PostgreSQL DB with Hacker's tier, but that requires further upgrading ...

The interface to set up a scheduled task is really nice and easy:

![pa scheduled tasks]({filename}/images/pa-scheduled-task.png)

Notice that I activate the venv in the command because it needs to load env variables.

### Less obvious

* I had to add our PA domain *pybites.pythonanywhere.com* to `ALLOWED_HOSTS` (Django settings).

* Django encapsulation. As detailed in [this excellent article](https://medium.com/@ayarshabeer/django-best-practice-settings-file-for-multiple-environments-6d71c6966ee2) you want to hide your SECRET_KEY, DB credentials, etc from version control. I also followed the settings best practices described in the article. So make sure you do some work upfront. Make sure you check [Django's checklist](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/). 

* Env variables. You need to set them [in 2 places](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/). As the docs admit this is not ideal. At the virtual env level it only seemed to work adding them to the *activate* script, not *postactivate*.

* [Handling static files](https://help.pythonanywhere.com/pages/DjangoStaticFiles) was a bit of a pain. I ended up [using collectstatic](https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#collectstatic) to get them all in one place:

		(venv) 12:27 ~/pybites-django/pybites (master)$ python manage.py collectstatic
		62 static files copied to ...

	Not sure if this is the best solution because I need to rerun this when static files change ...

	Then I set it up like this at the web front-end:

	![pa static files solution]({filename}/images/pa-static-files.png)

	CSS magically came to live upon app restart + browser refresh.

### Multiple apps

As the Hacker tier gives me one app I made [this container project / repo](https://github.com/pybites/pybites-django) to host multiple apps in. It's a nice exercise in Django's architecture of one project -> multiple apps that can be moved around. As said, PA's pricing structure is pretty flexible, so we can always add apps if necessary.

---

Keep Calm and Code in Python!

-- Bob

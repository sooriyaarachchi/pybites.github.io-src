Title: How to Build a Registration Backend with Django-Registration, Gmail and Heroku
Date: 2017-08-05 12:00
Category: Django
Tags: Django, 100DaysOfDjango, Heroku, django-registration, gmail, postgres, tutorial, virtualenv
Slug: django-registration-app
Authors: Bob
Summary: Two-phase registration, consisting of initial signup followed by a confirmation/activation email is a common piece in your web app. In this article I will guide you through setting this up in Django using the [Django-registration plugin](https://django-registration.readthedocs.io/en/2.2/), using Gmail for messaging. Then I show you how to deploy your app to Heroku. You can try it out [here](http://pybites-notifier.herokuapp.com/). 
cover: images/featured/pb-article.png
status: draft

Two-phase registration, consisting of initial signup followed by a confirmation/activation email is a common piece in your web app. In this article I will guide you through setting this up in Django using the [Django-registration plugin](https://django-registration.readthedocs.io/en/2.2/), using Gmail for messaging. Then I show you how to deploy your app to Heroku. You can try it out [here](http://pybites-notifier.herokuapp.com/). 

This serves as the tutorial I wanted to have when I got started. You will probably save time too, because I ran into various issues which I ironed out in the steps below. 

## The plan

The code is [on Github](https://github.com/pybites/django-registration), but I will build it again from scratch below so we can see it step-by-step and Julian can test it out for himself (thanks buddy!)

## Setup

First we create a virtual env and install django, [django-registration](https://django-registration.readthedocs.io/en/2.2/index.html) and the other plugins we will use (if you want to use SQLite you can leave psycopg2 out)

	$ mkdir registration && cd $_
	$ python3 -m venv venv && source venv/bin/activate
	(venv) $ pip install django django-registration dj-database-url gunicorn psycopg2
	...

Now we make our app:

	(venv) $ django-admin.py startproject register
	# (cannot use dir name 'registration')
	(venv) $ ls register/
	manage.py    register
	(venv) $ ls register/register/
	__init__.py    settings.py    urls.py        wsgi.py

## Sanity check

Let's see if this worked:

	$ cd register
	$ python manage.py runserver

Navigate to `http://127.0.0.1:8000/` - you should see Django's *It worked!* page. It also says *You have 13 unapplied migration(s).* - we get to that later in the Migration section.

If you want to use Postgres like I did create the database using psql. If you want to use SQLite you can skip this step.

	(venv) $ psql
	bbelderb=# create database notifications;
	bbelderb=# \c notifications
	You are now connected to database "notifications" as user "bbelderb".

## Messaging

I will use Gmail here but you could also use a service like Heroku's [SendGrid](https://devcenter.heroku.com/articles/sendgrid). This is probably better in the long run because to have Gmail working in your app you have to relinquish security: 

1. you have to enable [this setting](https://www.google.com/settings/security/lesssecureapps) to allow emailing from someplace other than gmail;

2. that worked for localhost, for heroku though I had to [DisplayUnlockCaptcha](http://www.google.com/accounts/DisplayUnlockCaptcha) when I started mailing (testing first signup). See [here](https://stackoverflow.com/questions/18124878/netsmtpauthenticationerror-when-sending-email-from-rails-app-on-staging-envir) for more information.

So I recommend you create a separate gmail if you go this route.

## Environment variables

We need some env variables. I set those in this virtual env so they are bound to this app (namespaces are a honking great idea right?):

At the end of *venv/bin/activate*:

	export SECRET_KEY=some_large_random_string  -> get it from Django's settings.py or generate one yourself
	export DJANGO_ENV='local'
	export GMAIL_SMTP_USER='new_gmail_account'
	export GMAIL_SMTP_PASSWORD='gmail_pw_of_this_account'
	export DB_NAME='notifications'
	export DB_USER='pbcl'
	export DB_PW='your_password'

If you want to use SQLite you can omit the `DB_*` variables.

Make sure you re-activate your venv so these variables are picked up: 

	(venv) $ deactivate
	$ source venv/bin/activate

Last command is convenient to have in your .bashrc (assuming you always have your virtual envs in your project folder and named as *venv*):

	alias ae='source venv/bin/activate'

We will use these variables in the next section.

## Configuring Django

From here on I assume you cd'd into the toplevel register dir, so basically you are where `manage.py` sits.

Let's set up Django's configuration that lives at `register/settings.py`. Some of this is early encapsulation and required/recommended config for later deployment to Heroku. Please bare with me.

1. Delete the `SECRET_KEY` variable and add your own, also let Django know in what environment we are:

		SECRET_KEY = os.getenv('SECRET_KEY')
		DJANGO_ENV = os.getenv('DJANGO_ENV', 'production').lower()

2. Now using the newly Django env variable let's set `DEBUG` to false when not in local dev environment. We will use Heroku later to deploy the app so let's add that to `ALLOWED_HOSTS` (and limit the catch-all `*` to local env only):

		if DJANGO_ENV == 'local':
			DEBUG = True
			ALLOWED_HOSTS = ['*']
		else:
			DEBUG = False
			ALLOWED_HOSTS = ['.herokuapp.com']

	Making these two changes resolves both 'SECURITY WARNING's in `settings.py`.

3. Using the django-registration no additions are needed to `INSTALLED_APPS` and `MIDDLEWARE`, that all works out-of-the-box with Django-registration.

4. Create the following directories for templates and static files cd-ing into the project root folder:

		# just to make sure:
		(venv) $ pwd
		/Users/bbelderb/code/registration/register

		(venv) $ mkdir templates
		(venv) $ mkdir register/templates
		(venv) $ mkdir register/static

	I am making two templates directories to use template inheritance: the upper templates dir will host a base.html we will extend from and the templates associated with the django-registration plugin we will download later on.

	And update the DIRS list in `TEMPLATES` in settings.py so Django knows where to look for templates:

		...
		TEMPLATES = [
			...	
			'DIRS': [
				os.path.join(BASE_DIR, 'templates'),
				os.path.join(BASE_DIR, 'register', 'templates'),
		],
		...	

5. Database config: we load in the env variables for our local use. For production (Heroku) we use `dj_database_url`. This is when using Postgres, for SQLite use the 2nd setting:

	A. Postgres

		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': os.getenv('DB_NAME'),
				'USER': os.getenv('DB_USER'),
				'PASSWORD': os.getenv('DB_PW'),
				'HOST': os.getenv('DB_HOST', 'localhost'),
				'PORT': os.getenv('DB_PORT', '5432'),
			}
		}

		if DJANGO_ENV == 'production':
			import dj_database_url
			db_from_env = dj_database_url.config(conn_max_age=500)
			DATABASES['default'].update(db_from_env)


	B. SQLite = default setting changing the name of the DB:

		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': os.path.join(BASE_DIR, 'notifications.sqlite3'),
			}
		}

6. Static files are still confusing at times for me but this is [the recommended setting for Heroku](https://devcenter.heroku.com/articles/django-assets) that worked for me:

		PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

		STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
		STATIC_URL = '/static/'

		# Extra places for collectstatic to find static files.
		STATICFILES_DIRS = (
			os.path.join(PROJECT_ROOT, 'static'),
		)

7. Add the django-registration setting to limit activation of accounts from the validation email to 7 days:

		ACCOUNT_ACTIVATION_DAYS = 7

8. Set the email config. All sensitive info gets loaded from env variables, we don't want stuff in our version control!

		EMAIL_HOST = 'smtp.gmail.com'
		EMAIL_PORT = 587
		EMAIL_USE_TLS = True
		EMAIL_HOST_USER = os.getenv('GMAIL_SMTP_USER')
		EMAIL_HOST_PASSWORD = os.getenv('GMAIL_SMTP_PASSWORD')

	Note we need port 587 for gmail, see [here](https://stackoverflow.com/questions/2894802/send-activate-email-with-django-registration).

9. And lastly with `DEBUG` set to False in Production / on Heroku, if anything blows up we just see a 500 error. I [found this setting](https://chrxr.com/django-error-logging-configuration-heroku/) which sends errors to Heroku's log. You can then easily debug anything pulling the remote logs with Heroku CLI's `heroku log` command. Add this snippet to `settings.py`:

		LOGGING = {
			'version': 1,
			'disable_existing_loggers': False,
			'handlers': {
				'console': {
					'class': 'logging.StreamHandler',
				},
			},
			'loggers': {
				'django': {
					'handlers': ['console'],
					'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
				},
			},
		}

If you're lost at this point the complete settings file is [here](https://github.com/pybites/django-registration/blob/master/register/settings.py).

## DB migration

Next migrate the DB:

	$ python manage.py migrate
	Operations to perform:
		Apply all migrations: admin, auth, contenttypes, sessions
	...

Finally let's create a superuser to be able to manage users that sign up:

	$ python manage.py createsuperuser
	...


## Base template and static files

Create a `base.html` inside templates/ with the following content:

	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
			<title>PyBites Django-registration Tutorial</title>
			{% load static %}
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/1.0.0/pure-min.css">
			<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
			<link rel="stylesheet" type="text/css" href="{% static 'style.css' %}" />
		</head>
		<body>
		<header>
			<h1>{% block title %}{% endblock %}</h1>
			<div id="login">
				{% if user.is_authenticated %}
					Hey {{ user.username }}, <a href="{% url 'auth_logout' %}?next=/">logout</a>
				{% else %}
					Hello guest,  <a href="{% url 'auth_login' %}">login (register)</a>
				{% endif %}
			</div>
		</header>
		<main>
			{% block content %}
			{% endblock %}
		</main>
	</body>
	</html>

If you want to add your own CSS styles on top of purecss create a `style.css` inside register/static/

## Django-registration templates

Unfortunately the required templates are not included in Django-registration when pip installing it. What I ended up doing was grabbing them from [django-registration-templates](https://github.com/macdhuibh/django-registration-templates). However I made some wording and styling ([purecss](https://purecss.io)) changes to them and one template - *password_reset_email.txt* - was missing which caused password reset to crash. So grab my copy instead:

	# you should be here:
	(venv) $ pwd
	/Users/bbelderb/code/registration/register

	(venv) $ git clone https://github.com/pybites/django-registration ~/Downloads/registration-templates
	...

	(venv) $ cp -r  ~/Downloads/registration-templates/templates/registration templates/
	(venv) $ ls templates/
	base.html    registration

## Write some Django code

OK with all this setup in place (sorry) let's actually write some code. The good news is that django-registration requires very little of it.

## URL routing

cd into the main app: 

	(venv) $ cd register/

Replace the content of `urls.py` with the following code:

	from django.conf.urls import url, include
	from django.contrib import admin
	from django.conf import settings
	from django.views.static import serve

	from . import views

	urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^admin/', admin.site.urls),
		url(r'^accounts/', include('registration.backends.hmac.urls')),
	]

	if not settings.DEBUG:
		urlpatterns += [
			url(r'^static/(?P<path>.*)$', serve, {
				'document_root': settings.STATIC_ROOT,
			}),
		]

The accounts regex entry is required for the Django-registration plugin (we're using the recommended [two-phase or hmac-workflow](https://django-registration.readthedocs.io/en/2.2/hmac.html#hmac-workflow)). The admin route is to manage the signed up users via Django's builtin admin.

I needed the last `if not` block to get static files working on Heroku, see [here](https://docs.djangoproject.com/en/1.11/ref/views/#django.views.static.serve) and [here](https://matthewphiong.com/managing-django-static-files-on-heroku). 

Next time I probably consider using a service like [Whitenoise](https://devcenter.heroku.com/articles/django-assets#whitenoise) which should make this easier.

### Homepage

Let's add a simple index view to greet the guest or logged in user and provide a link to sign up. Still in the register/ main app, create a file called `views.py` and add the following code:

	from django.http import HttpResponse
	from django.template import loader

	def index(request):
		template = loader.get_template('index.html')
		context = {}
		return HttpResponse(template.render(context, request))

It points to an HTML template called `index.html`. Let's create this next inside the register/templates/ folder with the following content:

	{% extends 'base.html' %}

	{% block content %}
	{% if user.is_authenticated %}
		<p><strong>Dear {{ user.username }}, glad to have you here!</strong></p>
		<p>You will receive an email for each new PyBites Code Challenge.</p>
		<p>We will tweak this page to include more notification settings ...</p>
	{% else %}
		<p>You can <a href="{% url 'registration_register' %}">sign up here</a> to get a notification email for each new challenge</p>
	{% endif %}
	{% endblock %}

Here we extend the base.html template in the root templates folder. The `TEMPLATES` -> `DIR` list we updated earlier in `settings.py` makes this magically work. We check if the user is authenticated and message/link accordingly.

Let's collect static files into `STATIC_ROOT` using [collectstatic](https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#collectstatic):

	(venv) $ cd ..
	(venv) $ python manage.py collectstatic

And run the app: 

	(venv) $ python manage.py runserver

You should see this:

![runserver app index template]({filename}/images/django-reg-helloworld.png)

Click on the *sign up here* link, you should see a sign up form, all nicely delivered by Django-register. One thing that does not seem right is the validation messages being visible all the time. I need to fix that, then I will update this screenshot:

![sign up form]({filename}/images/django-reg-reg-form.png)

Enter your username, email and password and click Submit:

![register, email will be send]({filename}/images/django-reg-reg-link-follow.png)

If all is setup correctly (env vars, gmail prep) You should get an email:

![confirmation link]({filename}/images/django-reg-email.png)

Click on the link and your account should be activated:

![runserver app index template]({filename}/images/django-reg-reg-link-follow.png)

You can now login and you should see the logged in page: 

![registed and activated account]({filename}/images/django-reg-registered-and-activated.png)

One enhancement would be to auto-login the user now.

## Commit to version control

Normally I would be make granular commits as we go but I wanted to focus on Django.

First of all init a repo - inside the register/ root folder (where `manage.py` lives):

	(venv) $ git init

Make sure we don't commit irrelevant files by adding a `.gitignore` file with the following content:

	(venv) $ cat .gitignore
	**pyc
	**swp
	**__pycache__
	register/staticfiles/
	*sqlite3

(last line is if you use a SQLite DB)

	(venv) $ git add .
	(venv) $ git commit -m "init commit"
	# again, be more granular with github outside this tutorial

## Deploy to Heroku

Now let's get our shiny app to the cloud. After all we did a lot of config in advance so it should be pretty easy now:

### Heroku login

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and login.

Make sure you are in register/ where `manage.py` lives. This is important because I had issues where I had Heroku look for `wsgi.py` under register/register and it would not work. 

Add the following required files:
 
	(venv) $ echo "python-3.6.2" > runtime.txt

Nice, Heroku uses Python 3.6!

	(venv) $ echo  "release: python manage.py migrate" > Procfile
	(venv) $ echo "web: gunicorn register.wsgi:application --log-file -" >> Procfile

The first line is not required but adds migrate as extra step during deployment, useful.

And finally let Heroku know what dependencies we need:

	(venv) $ pip freeze > requirements.txt

Commit these 3 files:

	(venv) $ git add .
	(venv) $ git commit -m "added heroku config files"

You can test the site locally. If doing so store your env variables in `.env` (and make sure to exclude that file from version control!) 
	
	(venv) $ heroku local web

Crreate the app with a unique enough name:

	(venv) $ heroku apps:create bobregistration
	Creating ⬢ bobregistration... done
	https://bobregistration.herokuapp.com/ | https://git.heroku.com/bobregistration.git

The git remote should be added automatically, if not run:

	(venv) $ git remote add heroku https://git.heroku.com/bobregistration.git

If you want to use a Postgres DB provision it, see [here](https://devcenter.heroku.com/articles/heroku-postgresql):

	(venv) $ heroku addons:create heroku-postgresql:hobby-dev

Heroku automatically sets the `DATABASE_URL` env variable for you. The `dj_database_url` plugin we pip installed and configured in `settings.py` takes care of the rest. This makes the `DB_ *` variables only for local use. You can see your Heroku databases [here](https://data.heroku.com/).

Finally let's set the other env variables via Heroku CLI:

	(venv) $ heroku config:set SECRET_KEY='some_large_random_string'
	(venv) $ heroku config:set DJANGO_ENV=‘production’
	(venv) $ heroku config:set GMAIL_SMTP_USER='new_gmail_account'
	(venv) $ heroku config:set GMAIL_SMTP_PASSWORD='gmail_pw_of_this_account'

With all this in place deploying to Heroku is very easy: just git push!

	(venv) $ git push heroku master
	Counting objects: 45, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (42/42), done.
	Writing objects: 100% (45/45), 16.95 KiB | 0 bytes/s, done.
	Total 45 (delta 7), reused 0 (delta 0)
	remote: Compressing source files... done.
	remote: Building source:
	remote:
	remote: -----> Python app detected
	remote: -----> Installing python-3.6.2
	remote: -----> Installing pip
	remote: -----> Installing requirements with pip
	....
	remote:        Successfully installed Django-1.11.3 dj-database-url-0.4.2 django-registration-2.2 gunicorn-19.7.1 psycopg2-2.7.3 pytz-2017.2
	remote:
	remote: -----> $ python manage.py collectstatic --noinput
	remote:        66 static files copied to '/tmp/build_1f0fe577269a9c44ab8bdaa75f241a79/register/staticfiles'.
	remote:
	remote: -----> Discovering process types
	remote:        Procfile declares types -> release, web
	remote:
	remote: -----> Compressing...
	remote:        Done: 50.6M
	remote: -----> Launching...
	remote:  !     Release command declared: this new release will not be available until the command succeeds.
	remote:        Released v9
	remote:        https://bobregistration.herokuapp.com/ deployed to Heroku
	remote:
	remote: Verifying deploy... done.
	remote: Running release command...
	remote:
	remote: Operations to perform:
	remote:   Apply all migrations: admin, auth, contenttypes, sessions
	remote: Running migrations:
	...
	remote: Waiting for release.... done.
	To https://git.heroku.com/bobregistration.git
	* [new branch]      master -> master


And voilà the app now runs on https://bobregistration.herokuapp.com/ (I delete it after this tutorial, check out [http://pybites-notifier.herokuapp.com/](http://pybites-notifier.herokuapp.com/) if you want to try it and/or subscribe to weekly PyBites Code Challenge notifications.

To add the superuser to the remote DB you can use Heroku's shell: 

	(venv) $ heroku run python manage.py createsuperuser
	...

## In Closing

Wow this was a lot to absorb but I wanted to get it out there. Although Django-registration makes it very easy to get two-phase registration going it does require a lot of setup and things need to go in the right place. 

I hope you found this tutorial useful and we would be happy to hear your feedback or questions.

What we like about this small app that it is a nice utility to bootstrap other Django apps. Having the registration and authentication sorted is a major piece. 

I am sure Julian learned a bite of two of Django and probably will consider it as an alternative to Flask, although I am sure he will never give up his passion for the latter ;)

---

Keep Calm and Code in Python!

-- Bob

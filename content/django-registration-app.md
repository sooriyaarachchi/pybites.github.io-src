Title: How to Build a Registration Backend with Django-Registration, Gmail and Heroku
Date: 2017-08-04 12:00
Category: Django
Tags: Django, 100DaysOfDjango, Heroku, django-registration, gmail, postgres, tutorial, virtualenv
Slug: django-registration-app
Authors: Bob
Summary: In this article I will guide you through setting up a registration system with Django. It ought to be easy using the django-registration plugin, yet I had some issues which can save you time. I will also show you how to deploy the app to Herokoku and configure gmail to send authentication links.
cover: images/featured/pb-article.png
status: draft

In this article I will guide you through setting up a registration system with Django. It ought to be easy using the django-registration plugin, yet I had some issues which can save you time. I will also show you how to deploy the app to Herokoku and configure gmail to send authentication links.

What's cool about this project is that it is easy to use to bootstrap another project. The other day I could just copy it and start building another app on top of it. We use it for code challenge notifications, if you want to receive a weekly email when we post a new code challenge, you can sign up [here](http://pybites-notifier.herokuapp.com/).

## The plan

[This](https://github.com/pybites/django-registration) is the project I built, but I will make it again from scratch here so we can see the steps and Julian can test it out for himself as well (thanks buddy!)

I actually recommend following the steps below as I ended up with a different dir structure the second time.

## Setup

First we create a virtual env and install django (which pull pytz as well) and [django-registration](https://django-registration.readthedocs.io/en/2.2/index.html). We will use a postgres DB so we need psycopg2 as well.

	$ mkdir registration && cd $_
	$ python3 -m venv venv && source venv/bin/activate
	(venv) $ pip install django django-registration psycopg2
	...

Let's also install the other plugins we will use: 

	(venv) $ pip install django-crispy-forms dj-database-url gunicorn
	...
	(venv) $ pip freeze
	dj-database-url==0.4.2
	Django==1.11.4
	django-crispy-forms==1.6.1
	django-registration==2.2
	gunicorn==19.7.1
	psycopg2==2.7.3
	pytz==2017.2

Now we make our app:

	# fair enough	
	(venv) $ django-admin.py startproject registration
	CommandError: 'registration' conflicts with the name of an existing Python module and cannot be used as a project name. Please try another name.

	(venv) $ django-admin.py startproject register
	(venv) $ ls register/
	manage.py    register
	(venv) $ ls register/register/
	__init__.py    settings.py    urls.py        wsgi.py

Let's do a sanity check: 

	$ python manage.py runserver

Navigate to http://127.0.0.1:8000/ - you should see Django's welcome page.

Next let's create the DB in postgres (if you want to use sqlite, skip this step):

	(venv) $ psql
	bbelderb=# create database notifications;
	bbelderb=# \c notifications
	You are now connected to database "notifications" as user "bbelderb".

Next migrate the DB:

	$ python manage.py migrate
	Operations to perform:
		Apply all migrations: admin, auth, contenttypes, sessions
	...

Finally let's create a superuser to be able to manage users that sign up:

	$ python manage.py createsuperuser
	...

## Env variables

We need some env variables. I set those in this virtual env so they are bound to this app (namespaces are a honking great idea right?):

At the end of venv/bin/activate:

	export SECRET_KEY=some_large_random_string  -> get it from register/register/settings.py or make one yourself
	export DJANGO_ENV='local'
	export DB_NAME='notifications'
	export DB_USER='pbcl'
	export DB_PW='your_password'
	export GMAIL_SMTP_USER='new_gmail_account'
	export GMAIL_SMTP_PASSWORD='gmail_pw_of_this_account'

Don't worry for now, I will come back to these variables throughout thoughout this tutorial.

For Gmail I recommend you make a new account because you need to relinquish some security enabling [this setting](https://www.google.com/settings/security/lesssecureapps) and going to [DisplayUnlockCaptcha](http://www.google.com/accounts/DisplayUnlockCaptcha) when starting to send your first Django email. See [here](https://stackoverflow.com/questions/18124878/netsmtpauthenticationerror-when-sending-email-from-rails-app-on-staging-envir).

Another option is Heroku's [SendGrid](https://devcenter.heroku.com/articles/sendgrid).

Make sure you re-activate your venv so these variables are picked up: 

	(venv) $ deactivate
	$ source venv/bin/activate

I actually have this alias in my .bashrc: 

	alias ae='source venv/bin/activate'

## Configuring Django

Let's set up Django's configuration that lives at `register/register/settings.py`. Some of this is early encapsulation and required/recommended config for later deployment to Heroku. Please bare with me.

1. Delete the secret key and add your own, also load in the env variable:

		SECRET_KEY = os.getenv('SECRET_KEY')
		DJANGO_ENV = os.getenv('DJANGO_ENV', 'production').lower()

2. Now using the newly Django env variable let's set debug to false when not in local dev environment. We will use Heroku later to deploy the app so let's add that to ALLOWED_HOSTS (and not have '*' in production):

		if DJANGO_ENV == 'local':
				DEBUG = True
				ALLOWED_HOSTS = ['*']
		else:
				DEBUG = False
				ALLOWED_HOSTS = ['.herokuapp.com']

	Making these two clears both 'SECURITY WARNING' strings.

3. Using the django-registration no additions are needed to INSTALLED_APPS and MIDDLEWARE, that part is setup under the hood after `pip install`

	The only addition to INSTALLED_APPS is crispy_forms to make the form validation a bit nicer:

	INSTALLED_APPS = [
			...
			...	
			# 3rd party
			'crispy_forms',
	]

4. Create the following directories for templates and static files cd-ing into the project root folder:

		(venv) $ cd registar
		(venv) $ pwd
		/Users/bbelderb/code/registration/register
		(venv) $ mkdir templates
		(venv) $ mkdir register/templates
		(venv) $ mkdir register/static

	I am making two templates directories to use template inheritance: the upper templates dir will host a base.html we will extend from and the templates associated with the django-registration plugin we will download later on.

	And update the DIRS list in TEMPLATES in settings.py so Django knows where to locate templates:

		...
		TEMPLATES = [
				...	
					'DIRS': [
							os.path.join(BASE_DIR, 'templates'),
							os.path.join(BASE_DIR, 'register', 'templates'),
					],
				...	

5. Database config: we load in the env variables for our local use. For production (Heroku we use `dj_database_url`):

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

	If you want to use sqlite just leave the default setting and naming your DB:

		DATABASES = {
			'default': {
					'ENGINE': 'django.db.backends.sqlite3',
					'NAME': 'notifications',
			}
		}

6. Static files are still confusing at times for me but this is [the recommended setting for Heroku](https://devcenter.heroku.com/articles/django-assets):

		PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

		STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
		STATIC_URL = '/static/'

		# Extra places for collectstatic to find static files.
		STATICFILES_DIRS = (
				os.path.join(PROJECT_ROOT, 'static'),
		)

7. Add django-registration setting to limit activation of accounts from the validation email to 7 days:

		ACCOUNT_ACTIVATION_DAYS = 7

8. Set the email config, again we load sensitive info from env variables, not putting that stuff under version control!

		EMAIL_HOST = 'smtp.gmail.com'
		EMAIL_PORT = 587
		EMAIL_USE_TLS = True
		EMAIL_HOST_USER = os.getenv('GMAIL_SMTP_USER')
		EMAIL_HOST_PASSWORD = os.getenv('GMAIL_SMTP_PASSWORD')

	Note we need port 587 for gmail, see [here](https://stackoverflow.com/questions/2894802/send-activate-email-with-django-registration).

9. And lastly with debug == False on Heroku, if anything blows up we just see a 500 error. I [found this setting](https://chrxr.com/django-error-logging-configuration-heroku/) which sends errors to heroku's log easily retrievable running `heroku log` when logged in via the Heroku CLI. We are still in settings.py:

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

## Base template and static files

Let's just grab these from the original project, from the project root folder:

	(venv) $ pwd
	/Users/bbelderb/code/registration
	(venv) $ cd templates/
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/templates/base.html
	(venv) $ cd ..
	(venv) $ cd register/static/
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/register/static/uni-form.jquery.min.js
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/register/static/uni-form.css
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/register/static/uni-form-validation.jquery.min.js
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/register/static/style.uni-form.css
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/register/static/style.css
	(venv) $ cd -

You should end up with:

	(venv) $ ls templates/
	base.html
	(venv) $ ls register/static/
	style.css                uni-form-validation.jquery.min.js    uni-form.jquery.min.js
	style.uni-form.css            uni-form.css

## django-registration templates

The bad news is that these are not included with the pip install. What I ended up doing is grab them from [this repo](https://github.com/macdhuibh/django-registration-templates). However I made some changes to them to use nice purecss styling, so better grab mine. Also because the original repo missed `password_reset_email.txt` as I found out testing:

	(venv) $ git clone https://github.com/pybites/django-registration ~/Downloads/registration-templates

	...
	(from project root dir)

	(venv) $ cp -r  ~/Downloads/registration-templates/templates/registration register/templates/
	(venv) $ ls register/templates/
	base.html    registration

While testing I found one template / txt file missing, so add that one from my code repo:

	(venv) $ cd templates/registration 
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/templates/registration/password_reset_email.txt

## Write some Django code

OK with all this setup in place (sorry) let's actually write some code. The good news is that django-registration requires very little of it.

## URL routing

cd into the main app: 

	(venv) $ cd register/register/

And create an `urls.py` file with the following code:

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

The accounts regex entry is required for the django-registration plugin (we're using the recommended [hmac-workflow](https://django-registration.readthedocs.io/en/2.2/hmac.html#hmac-workflow)). I am leaving admin in because it could be useful to manage new users via the admin backend.

This last if not block I needed to get static files to work on Heroku, see [here](https://docs.djangoproject.com/en/1.11/ref/views/#django.views.static.serve) and [here](https://matthewphiong.com/managing-django-static-files-on-heroku). Next time I probably consider using [Whitenoise](https://devcenter.heroku.com/articles/django-assets#whitenoise).

### Homepage

Let's add a simple index view to show if a user is logged in an provided the registration link. Still in register/register/ add the following code to views.py:

	from django.http import HttpResponse
	from django.template import loader

	def index(request):
			template = loader.get_template('index.html')
			context = {}
			return HttpResponse(template.render(context, request))

It points to an index.html templates we need to create in register/register/templates/:

	{% extends 'base.html' %}

	{% block content %}
	{% if user.is_authenticated %}
					<p><strong>Glad to have you here!</strong></p>

					<p>You will receive an email with each new challenge.</p>

		<p>We will tweak this page to include more notification settings ...</p>
	{% else %}
					<p>You can <a href="{% url 'registration_register' %}">sign up here</a> to get a notification email for each new challenge</p>
	{% endif %}
	{% endblock %}

Here we extend the base.html template in the root templates folder. The TEMPLATES - DIR config in settings.py should make this magically work.

Let's collect static files into STATIC_ROOT using [collectstatic](https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#collectstatic):

	(venv) $ python manage.py collectstatic

And try the app: 

	(venv) $ python manage.py runserver

You should see this:

Try to sign up with an email, you should get an activation link that makes your registration final:

## Commit to version control

Normally I would be make granular commits as we go but I wanted to focus on Django.

First of all init a repo and copy in a .gitignore to make sure we don't commit irrelevant files:

	(in project root folder)
	(venv) $ git init
	(venv) $ wget https://raw.githubusercontent.com/pybites/django-registration/master/.gitignore

	# vi .gitignore to add register/register/staticfiles - dir structure changed for this tutorial

	(venv) $ git add .
	(venv) $ git commit -m "init commit"

## Deploy to Heroku

Now let's get our shiny app to the cloud. After all we did a lot of config in advance so it should be pretty easy now:

### Heroku login

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and login.

cd into register, the main app. It is important to add the following required files into that dir, so Heroku can find the wsgi.py file (I ended up with dir/dir/wsgi.py, you really want dir/wsgi.py or in our case register/wsgi.py)

	(venv) $ cd register

Nice: Heroku is very up2date!
 
	(venv) $ echo "python-3.6.2" > runtime.txt

The first line is not required but adds migrate as extra step during deployment, useful:

	(venv) $ cat Procfile
	release: python manage.py migrate
	web: gunicorn register.wsgi:application --log-file -

Let Heroku know what dependencies we need:

	(venv) $ pip freeze > requirements.txt

Commit these 3 files:

	(venv) $ git add .
	(venv) $ git commit -m "added heroku config files"

You can test the site locally. If doing so store your env variables in `.env`: 
	
	(venv) $ heroku local web

Crreate the app with a unique name:

	(venv) $ heroku apps:create registration
	▸    Name is already taken
	(venv) $ heroku apps:create bobregistration
	Creating ⬢ bobregistration... done
	https://bobregistration.herokuapp.com/ | https://git.heroku.com/bobregistration.git

The git remote should be added automatically but it did not in my case, easy enough to do it manually though:

	(venv) $ git remote add heroku https://git.heroku.com/bobregistration.git

Provision the postgres DB (likely can skip if sqlite) and set your env variables. You can do it via CLI but I am using the GUI:

Then just push your app:

	(venv) $ git push heroku master

TODO: getting an error -> fix + show console output here.

---

Keep Calm and Code in Python!

-- Bob

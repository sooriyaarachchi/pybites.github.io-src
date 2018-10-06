Title: Persistent Virtualenv Environment Variables with python-dotenv
Date: 2018-10-06 18:18
Category: packages
Tags: Python, tips, virtualenv, virtual-environment, packages, env, learning, howto
Slug: persistent-environment-variables
Authors: Julian
Summary: In this article I'm going to show you how to declare persistent environment variables in Python Virtual Environments with python-dotenv.
cover: images/featured/pb-article.png

I can't count the amount of times I've followed a tutorial or guide that's said something along the lines of "Store your API Keys in environment variables".

It's easy enough to do with `os.getenv` but the thing that drives me crazy is having to, 1) hardcode the environment variables as global variables in my OS or 2) redeclare them every time I initiate the terminal session.

In this article I'm going to show you (and to document for myself!) how to declare persistent environment variables in Python Virtual Environments with python-dotenv.


##Environment Variables in a Virtual Environment

With a UNIX based OS you'd traditionally declare your environment variables by explicitly defining them at the OS level. Take variables `CLIENT_ID` and `CLIENT_SECRET` as an example:

~~~~
#CLIENT_ID="01234509876"
#CLIENT_SECRET="julianandsilentbobstrikeback"
#
#echo $CLIENT_ID
0123450987
#
#echo $CLIENT_SECRET
julianandsilentbobstrikeback

~~~~

To do this within your Python Virtual Environment (venv) you'd do the same declarations as above after you've activated your venv. Doing this means your environment variables are within the virtual environment, not the global OS environment.

> Read more on [Python Virtual Environments here](https://pybit.es/the-beauty-of-virtualenv.html).

This is all well and good except that when you deactivate and reactivate the venv, the environment variables are lost and you'll need to redeclare them.


##Enter python-dotenv

`python-dotenv` is a Python module that allows you to specify environment variables in traditional UNIX-like ".env" (dot-env) file within your Python project directory. This includes in venvs!

Here's the flow:

1. Populate the `.env` file with your environment variables.
2. Import `python-dotenv` and call it at the start of your script.
3. Use whatever "getenv" method you use to import the environment variables, eg: `os.getenv()`.


##python-dotenv Example

###1. Create your `.env` file

~~~~
(venv)#vim .env
(venv)#cat .env
CLIENT_ID="1234509876"
CLIENT_SECRET="julianandsilentbobstrikeback"
(venv)#
~~~~


###2. Import and Call python-dotenv

I'm using a file called `routes.py` as my primary Python script here:

~~~~
(venv)#cat routes.py
from dotenv import load_dotenv

load_dotenv()
~~~~

I begin by importing `load_dotenv` from the `dotenv`.

It's then just as simple as running `load_dotenv()` to make the `.env` file accessible to your script as your source of environment variables.


###3. Access the Environment Variables

I've continued with `routes.py` by writing a function that uses `os.getenv` to pull and print the environment variables I specified in my `.env` file:

~~~~
from dotenv import load_dotenv
import os

load_dotenv()

client = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")

def printenvironment():
    print(f'The client id is: {client}.')
    print(f'The secret id is: {secret}.')

if __name__ == "__main__":
    printenvironment()
~~~~

<br>
Running this script returns the following:

~~~~
#python routes.py 
The client id is: 1234509876.
The secret id is: julianandsilentbobstrikeback.
#
~~~~


##PERSISTENCE AT LAST!

The original problem was that when you'd deactivate and reactivate the venv you'd lose the environment variables.

Watch the persistence in action!

~~~~
(venv)#deactivate
#
#
#source venv/bin/activate
(venv)#
(venv)#python routes.py 
The client id is: 1234509876.
The secret id is: julianandsilentbobstrikeback.
#
~~~~

Okay... I know. Anticlimactic. No! What am I saying?! Super handy and so time saver-y!


##.env Example File

Pro-tip: if you're committing to a public repo, make sure .env files are listed in the .gitignore file. **You don't want your environment variables being pushed to a public repo!**

That said, you'll want to let people know what environment variables to configure for themselves if they're going to clone your repo or use your script.

The nice way to do this is to create an "empty" .env.example file:

~~~~
#vim .env.example
CLIENT_ID=""
CLIENT_SECRET=""
~~~~


##Conclusion

This is one of those Python things I'll be taking with me to the grave. With the numerous apps and scripts I've created, managing these env variables has always been a pain.

But no more I say! I'll be using `python-dotenv` to manage everything.

---

Keep Calm and Code in Python!

-- Julian

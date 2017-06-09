Title: Using Python Requests on a Page Behind a Login 
Date: 2017-06-09 21:48
Category: Modules
Tags: requests, code, web scraping, python, 
Slug: requests-session
Authors: Julian
Summary: In this post I discuss using the requests module on web pages behind a login
cover: images/featured/pb-article.png

A great frustration in my web scraping journey has been finding a page tucked away behind a login. I didn’t actually think it was possible to scrape a page locked away like this so I didn’t bother Googling it. Bad Julian, bad!

Using the `requests` module to pull data from a page behind a login is relatively simple. It does however require a little bit of HTML know how.

For this article I’m going to demonstrate logging into [freecycle.org](https://www.freecycle.org) (totally check it out if you don’t know what it is!).

Full code is [here](https://github.com/pybites/100DaysOfCode/tree/master/051).


<br>
##POSTing data

First you need to understand how data is handled at the HTML page level. 

The login prompt on a web page is an HTML form. As such, when you enter your credentials and click submit, you’re sending your data to the authentication application behind the page. This is called a **POST**. You’re pushing, or *POSTing* your data.

What you’re doing with the requests module is automating this. Instead of you typing the data in yourself, your script will do it for you.

**GET** on the other hand is precisely the opposite. GET, as the name implies, *pulls* data. Very useful for requests right?


<br>
##Get Dirty, Start Digging

The next step is to start digging around the HTML code for the login page of the site. What we’re looking for is the HTML `form` code that our script will look for so it knows where to plug in your credentials.

- The login page for freecycle.org is [https://my.freecycle.org](https://my.freecycle.org). Inspect the HTML page using your browser of choice (I use Google Chrome).

- Next, start working your way through the HTML until you find the `form` HTML tag.

- Within the form tag look for the `method` argument and you’ll see it says “post”. This means we’re in the right place!

- Again, within the tag, you’ll see the `action` argument. The URL specified is what you want to note down. In this case it’s: https://my.freecycle.org/login. This URL is where the credentials are used once you enter them in.

- Now, drill down further into the `form` tag and look for the `<input>` tags. There should be at least two (username and password). The username input tag is generally of `type=text` and the password, `type=password`.

- Look within these `input` tags for a `name` argument. This is the *name* of this input field. This is also how `requests` is going to know *where* to “enter” your credentials.

- On the freecyle.org login page the username input field has `name` `username`. The password input field has `name` `pass`. Note these two names down.


<br>
##What are you Scraping?

At this point you’ll want to actually login to the website and figure out what you’re scraping.

Consider the following for your own situation:

- When you login to freecycle.org in a browser, the page you’re redirected to has the URL: https://my.freecycle.org/home/groups. This is **not** a limiting factor. That is, this is not the only page `requests` has access to for scraping goodness.

- I want to scrape a list of my active posts, the URL for the “My Posts” page is: https://my.freecycle.org/home/posts. This is precisely the URL I’ll be pointing `requests` at.

- Continue on as you normally would with `requests` to grab your data. Look for the relevant HTML tags and IDs.


<br>
##Talk is Cheap, Show me the Code!

Finally! Code time! With all of the data on hand, we can piece this baby together.

Assign your two URLs to variables:

~~~~
#This URL will be the URL that your login form points to with the "action" tag.
POST-LOGIN-URL = 'https://my.freecycle.org/login'

#This URL is the page you actually want to pull down with requests.
REQUEST-URL = 'https://my.freecycle.org/home/posts'
~~~~

Pythonic and self-explanatory. Let’s move on.

<br>
Now we want to set up a dict that contains our login information.

~~~~
payload = {
    ‘username’: ‘your_username’,
    'pass’: ‘your_password'
}
~~~~

The keys in the dict are the `name`s of the input fields collected earlier. Eg: `username` and `pass`. The values associated with each are (you guessed it!) your username and password details. It’d be a good idea to at the very least, store your password in an environment variable and call it in for use in the script.

<br>
Finally, we want to open our `requests` `session`. Yep! Requests will create its own session instance (useful for multiple requests to the same site):

~~~~
with requests.Session() as session:
    post = session.post(POST-LOGIN-URL, data=payload)
    r = session.get(REQUEST-URL)
    print(r.text)   #or whatever else you want to do with the request data!
~~~~

- We’ll use a `with` statement to open the request Pythonically.

- Line 2 **POSTS** the data to the login URL we noted down earlier. It requires `data` to be specified, in which case we pass it the `payload` dict we created. This is the part that enters our username and password!

- Line 3 is our traditional requests call using `session.get` to the URL we want to scrape.

- Line 4 is where you’ll continue on with your requests work. To keep it simple I’ll leave it at a `print` statement that will print the entire page.


<br>
##Conclusion

And we’re done! That’s it! You can now carry on requesting data from the site behind the login.

The next challenge is to get past those pesky CAPTCHA boxes. Don’t get us started on those!

For simple sites that just use a text login system though, this process works. The code is actually quite simple. Rather, it’s the preparation and digging that’s time consuming!

I haven’t attempted this with Scrapy or other modules yet so if you can do this another way I’d love to hear how!

Keep Calm and Code in Python!

-- Julian
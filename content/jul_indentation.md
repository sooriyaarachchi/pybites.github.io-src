Title: Don't Let Indentation Catch You Out
Date: 2016-12-30 19:51
Category: Learning
Tags: python, learning, beginners, tips, cleancode, best-practices
Slug: indentation_tips
Authors: Julian
Summary: Python indentation can be a cruel mistress. Let's get it right!
Status: published
cover: images/featured/indentation.png

Every programmer knows the frustration of writing code and hitting run only to have the compiler locate an error that you swear wasn't an error. (That is, I'm hoping it's not just me right?!)

One of the first things to learn with Python is the absolute **importance of indentation**.


## What is Indentation?

Okay I'll keep this quick. It's just important that I cover this for anyone new to programming.

Indentation is the white space at the front of your code. In all languages you'll see some sort of indentation such as this:

~~~~
def how_to_be_cool():
    wear_aviator_sunglasses()
~~~~

Notice the space in front of the second line.



## Python's Love Affair With Indentation

It took me a day or two to fully grasp how dependent Python was on indentation. It's actually part of the beauty of the language. In most other languages you'll be wrapping your code within curly braces {} which can grow tiresome.

Python, however, relies on indents. In the above code, the indent in front of line 2 tells the compiler that this code "belongs" to the *how_to_be_cool* function.

Check out the difference between Javascript and Python for the same code:

**Javascript**
~~~~
function how_to_be_cool() {
	wear_aviator_sunglasses();
}
~~~~

**Python**
~~~~
def how_to_be_cool():
    wear_aviator_sunglasses()
~~~~

Much simpler in Python! Anything that's indented by the same amount under the function will be considered part of the function. The general rule of thumb is to use 4 spaces.



## Hanging Indents for Nested Code

Indents for your nested statements is a little more flexible but there are definitely guidelines. Let's add a simple infinite while Loop to the above code and check out the indentation:

~~~~
def how_to_be_cool():
    while True:
        wear_aviator_sunglasses()
~~~~

The while loop is now in the first indent of 4 spaces and the sunglasses function call is indented by a further 4 spaces to indicate that it's now in the loop.

If I want to add code to the *how_to_be_cool* function after the while loop, I simply write code one indentation margin (4 spaces) "up". Check it out:

~~~~
def how_to_be_cool():
    while True:
        wear_aviator_sunglasses()
    time.sleep(5)
~~~~

Simple!



## How Indents Can Bite You in the Butt

This brings me to one of my biggest learning points with Python. **Always Watch Your Indents!**

I can't stress that enough. If you're not careful, you are bound to make mistakes and waste time debugging your code. Python expects proper marginalised indents. Unless you're continuing code from the previous line onto subsequent lines, your code needs to line up. If not, Python will most likely spit the dummy.

Of course, you won't always do it intentionally. While editing and fine tuning my own code I was doing so without removing previous indents and spaces. As a result I was left with unexpected spaces that caused my code to error out.

Here's an example of the above code with indentation that's just *slightly* out of whack:

~~~~
def how_to_be_cool:
    while True:
        wear_aviator_sunglasses()
     time.sleep(5)
~~~~

It may be quite noticeable here but when you've got 200 lines of code it'll be harder to catch. Of course, the compiler should tell you where the error is but it may not jump out at you at first. It sure didn't for me!



## Tabs V Spaces

I initially wrote this post assuming that tabs were mandatory in Python (as that's how I keep my code clean in other languages). [The official Python Style Guide](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces) actually says otherwise! 

Python.org recommends that we use only spaces and never tabs (unless it's to keep consistent with code already with tabs). Always something new to learn!



## Further Reading on Indentation

There's an extensive list of different indentation scenarios on the [Python Style Guide](https://www.python.org/dev/peps/pep-0008/#indentation). I found it to be quite enlightening! I recommend checking it out posthaste!



## Vim Settings to Make Your Life Easier

For the Vim lovers out there, adding the following to your *.vimrc* file will take care of a lot of your indentation woes:

~~~~
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix
~~~~

These settings will make the following 3 adjustments:

1. Change your tab to be only 4 spaces long instead of the usual 8.
2. Limit the length of your lines to be 79 characters as per [Python specifications](https://www.python.org/dev/peps/pep-0008/#maximum-line-length).
3. Save your files in a unix format (helpful for github sharing/interactions etc).

Thanks to RealPython.com for this info. They've actually got a heap of other handy settings for Vim + Python in their [original article](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/). Definitely worth checking out!


## Conclusion

For such a simple concept, indentation can be super complex which is why even the mighty Bob was caught out leaving only 2 spaces in his blocks of code (Sorry Bob!). I no longer feel bad for getting this wrong!

> edit Bob: I shamefully admit I used 2 spaces before, now that I comply with PEP8 using 4 spaces I am so much happier, and people reading my code probably too :)

Indentation is what makes Python beautiful but is also something that can ruin your afternoon so do yourself a favour, get those vim settings in place to automate it and keep it in the back of your mind that a stray space somewhere could be foiling your Python master plans!

Remember, Keep Calm and Code in Python!

-- Julian

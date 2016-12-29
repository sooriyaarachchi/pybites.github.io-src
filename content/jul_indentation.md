Title: Don't Let Indentation Catch You Out
Date: 2016-12-30 9:00
Category: Learning
Tags: python, learning, beginners, tips, cleancode, best-practices
Slug: Indentation_Tips
Authors: Julian
Summary: Python indentation can be a cruel mistress. Let's get it right!
Status: Draft


Every programmer knows the frustration of writing code and hitting run only to have the compiler locate an error that you swear wasn't an error. (That is, I'm hoping it's not just me right?!)

One of the first things to learn with Python is the absolute **importance of indentation**.

## What is Indentation?

Okay I'll keep this quick. It's just important that I cover this for anyone new to programming.

Indentation is the white space at the front of your code. In all languages you'll see some sort of indentation such as this:

~~~~
def how_to_be_cool:
	wear_aviator_sunglasses()
~~~~

Notice the tab in front of the second line.


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
def how_to_be_cool:
        wear_aviator_sunglasses()
~~~~

Much simpler in Python! Anything that's indented one tab under the function will be considered part of the function.


## Nested Indents

The same rules apply with regards to nested code. Let's add a simple infinite while Loop to the above code and check out the indentation:

~~~~
def how_to_be_cool:
	while True:
		wear_aviator_sunglasses()
~~~~

The while loop is now in the first indent margin and the sunglasses function call is indented such that it's now in the loop.

If I want to add code to the *how_to_be_cool* function after the while loop, I simply write code one indentation margin "up". Check it out:

~~~~
def how_to_be_cool:
	while True:
		wear_aviator_sunglasses()
	time.sleep(5)
~~~~

Simple!


## How Indents Can Bite You in the Butt

This brings me to one of my biggest learning points with Python. **Always Use Tab For Your Indents!**

I can't stress that enough. If you use spacebar to indent (8 spaces = 1 tab), you are bound to make mistakes and waste time debugging your code. Python expects proper marginalised indents. If you happen to only indent by 5 spaces, Python will execute assuming that poorly indented code isn't part of the function it belongs to and will most likely spit the dummy.

Of course, you won't always do it intentionally. While editing and fine tuning my own code I was doing so without removing previous indents and spaces. As a result I was left with unexpected spaces that caused my code to error out.

Here's an example of the above code with indentation that's just *slightly* out of whack:

~~~~
def how_to_be_cool:
      while True:
		wear_aviator_sunglasses()
	time.sleep(5)
~~~~

It's pretty noticeable here right? What about when you've got 200 lines of code? Of course the compiler should tell you where the error is but it may not jump out at you at first. It sure didn't for me!


## Conclusion

Again, I know this is simple stuff but it's totally applicable to everyone and something that can be easily overlooked.
Indentation is what makes Python beautiful but is also something that can ruin your afternoon.

Do yourself a favour, **always use tab** and keep it in the back of your mind that a stray space somewhere could be foiling your Python master plans!

And Remember, Keep Calm and Code in Python!

-- Julian

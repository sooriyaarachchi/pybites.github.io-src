Title: Copy and Paste with Pyperclip
Date: 2017-01-06 12:00
Category: Tools
Tags: python, tips, tricks, code, pybites
Slug: pyperclip
Authors: Julian
Summary: Use the Pyperclip module to copy and paste with the clipboard!
cover: images/featured/pb-article.png

A quick and easy one for you today.

While I was working through *Automate the Boring Stuff* (review [here](http://pybit.es/automate_the_boring_stuff_review.html)) I experienced a few "this is AMAZING!" moments. One of which was when I discovered the Pyperclip module.


## What is Pyperclip?

Pyperclip is a module you can import that allows you to copy and paste to and from the clipboard on your computer. It does this through the use of two functions: copy() and paste()... go figure!

It's simple but man did it blow my mind!



## Why so Awesome?!

Well...

1. I was still super new to Python so the idea that I could interact with the user to that level was insane to me. It was a new way of inputting data without actually asking for traditional "type this and hit enter" input.

2. It was exactly what I was looking for at the time! I wanted to automate the pasting of lists I had copied to the clipboard for a small tool I was writing.

3. The exercise in *Automate the Boring Stuff* had you paste() text from the clipboard into the program (ie, read in), manipulate said text, then copy() it back to the clipboard. In a split second you could insert a '*' in front of every line in a list! This opened my mind to a whole new way of thinking.



## Example

Okay enough talk. Let's get to it. Installation first:

~~~~
#pip install pyperclip
#pip list
pip (9.0.1)
pyperclip (1.5.27)
setuptools (28.8.0)
~~~~

Now we import it into our code and run it:

~~~~
>>> import pyperclip
>>> 
>>> pyperclip.copy('This is copied to the clipboard.')
>>> 
>>> pyperclip.paste()
'This is copied to the clipboard.'
>>>
~~~~

> Be warned though. Pyperclip copies and pastes just like anything else. That is, it doesn't get exclusive rights to the clipboard. The text you copy to the clipboard has every chance of being overwritten by anything else that happens to copy after your command has run.

In the above example we copied to the clipboard and then instantly pasted. In most situations you'll want to paste what the *user* has on their clipboard then manipulate that.

## Another example

The author of the tool (Al Sweigart) shows some more use cases in [chapter 6](https://automatetheboringstuff.com/chapter6/) of [Automate the Boring Stuff](http://pybit.es/automate_the_boring_stuff_review.html), for example how to add bullets to wiki markup:

> The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard. 

Of course the possibilities are endless. You could for example make a script that retrieves a link from the clipboard (I mean one you copied previously), retrieve the metadata for that link scraping it, and copying an enriched string (link + metadata) back to the clipboard. You could use this for example to (semi)auto-create posts to social media. You would use pyperclip for the get/put from/to clipboard.


## Conclusion

Pyperclip really opened my eyes to the power of Python. Direct interaction with the user is awesome. 

However, it is scary to think just how easy it is to write to and from the users clipboard without their knowledge. These functions (as per anything) can be called without any user knowledge whatsoever. In a fraction of a second we can paste the output of their clipboard to a file of our choosing! It's creepy to think of how easily this can be used maliciously!

That's coding though I guess! [With great power...](https://youtu.be/b23wrRfy7SM?t=12)

Keep Calm and Code in Python!

-- Julian

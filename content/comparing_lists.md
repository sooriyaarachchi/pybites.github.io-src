Title: Comparing Lists with Difflib
Date: 2017-03-08 10:00
Category: Learning
Tags: python, learning, beginners, tips, cleancode, bestpractices, pythonic
Slug: comparing_lists
Authors: Julian
Summary: Learn to compare blocks of text with the difflib module.
cover: images/featured/pb-article.png

I love finding new things, especially when they end up saving you a boat load of time and effort! I was looking for a way to compare two lists as the code I had seemed quite clunky. Surely there had to be a better way out there! That's when I discovered difflib.


##The Julian Way

I'll show you how I was approaching the problem first. Don't judge me!

First, the two blocks of text (made these lists up on the spot):

~~~~
>>> text1 = """Julian's to-do list:
1. Be awesome.
2. Pybites.
3. Enjoy a beer."""
>>> 
>>> text2 = """Bob's to-do list:
1. Be awesome!
2. PyBites.
3. Enjoy a beer."""
>>>
~~~~

I then split the these blocks up into strings using *splitlines()*. This returns a list containing each line:

~~~~
>>> text1_split = text1.splitlines()
>>> text2_split = text2.splitlines()
~~~~

This is where I got stuck. I came up with a for loop that checked to see if items from the *text1_split* list were in the *text2_split* list. There's an if statement for the checking:

~~~~
>>> for i in text1_split:
	if i in text2_split:
		print("'%s' is in both lists!" % (i))
	else:
		print("'%s' is NOT in both lists!" % (i))

		
'Julian's to-do list:' is NOT in both lists!
'1. Be awesome.' is NOT in both lists!
'2. Pybites.' is NOT in both lists!
'3. Enjoy a beer.' is in both lists!
>>>
~~~~

The problem is that it doesn't tell me what's in *text2_split*. All it's confirming is whether the items in *text1_split* exist in *text2_split*. 

The code was already getting out of hand. From here I'd need to add code to tell me what's in *text2_split* if there isn't a match and what the differences are. 
Enter difflib.


##Difflib to the Rescue!

Before I show you the command, I'll just say that difflib is actually quite expansive, ie, there's a lot you can do with it. This post is just about the *Differ()* class.

As before, you have to split the blocks of text into a list of strings/lines:

~~~~
>>> text1_split = text1.splitlines()
>>> text2_split = text2.splitlines()
~~~~

I then call *Differ().compare()* to do the comparison. I store the result of the command in the *diff* variable. Finally, I print the output, joining the lines with a new line to make it readable.

~~~~
>>> diff = difflib.Differ().compare(text1_split, text2_split)
>>> print('\n'.join(diff))
- Julian's to-do list:
? ^^^^^^

+ Bob's to-do list:
? ^^^

- 1. Be awesome.
?              ^

+ 1. Be awesome!
?              ^

- 2. Pybites.
?      ^

+ 2. PyBites.
?      ^

  3. Enjoy a beer.
~~~~

Look familiar? If you're a Linux/Unix fan you'll have likely come across the *diff* command, in which case you'll have no problem reading this!

What you're seeing here is the differences between each list.

The key to reading the above:

'- ' indicates the difference is in the first list. In this case, the letters "Julian".

'+ ' indicates the difference is in the second list. In this case, the letters "Bob".

'? ' draws your attention to anything that doesn't appear in either list. It appears under every line here (except the last) because the new line we inserted wasn't originally there.

'  ' (a blank space) indicates that this line is a perfect match and is in both lists. In this case, line item "3. Enjoy a beer.".

The ^ (caret) symbol appears underneath the differing characters. Note the ^ under the lower and upper case B in the second line item.



##Conclusion

This is only the tip of the iceberg as Difflib is pretty big. In fact, we used the difflib.SequenceMatcher class in our [Code Challenge 03 - PyBites blog tag analysis](http://pybit.es/codechallenge03_review.html) to look for similarities between our blog tags.

It's one of those handy stdlib modules you stumble across that can change how you code. I think it's brilliant!

Read more on difflib [here](https://docs.python.org/3/library/difflib.html) or use help(difflib) from the Python shell.

Keep Calm and Code in Python!

-- Julian

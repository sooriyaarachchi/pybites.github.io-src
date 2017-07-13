Title: The Importance of Refactoring Code
Date: 2017-07-13 19:02
Category: Concepts
Tags: python, beginner, learning, examples, code, refactoring
Slug: refactoring
Authors: Julian
Summary: In this quick post I discuss why refactoring code is one of the most important parts of the learning process.
cover: images/featured/pb-article.png

With the completion of our [100 Days of Code Challenge](https://pybit.es/special-100days-of-code.html), this week I found myself with a bit more free time than usual. I decided to look back on some of my older code and… wow. Refactoring time!

##Refactoring?!

I remember when Bob first used the term. It brought back bad memories of maths!

Refactoring code is the process of making amendments, changes or improvements to your existing code. The end program or application will still operate in the same way, it’s just that the underlying code will be cleaner, leaner or faster.


<br>
##Why Bother?

There are many reasons why this is useful, some of which I’ve experienced myself lately:

1. Most importantly, it makes you feel good!! Seriously, how good does it feel to look back at code you wrote just 6 months ago and think to yourself, “What the heck was I thinking?!”. Seeing the improvement in your coding ability is so important to keeping you on the coding path. If you don’t see an improvement, you won’t be motivated to keep learning!

2. Your code becomes more refined. Check out the examples below. Refactoring just one line of code can make your code more elegant and professional. Also, it doesn’t hurt to have a lower line count!

3. Your projects will grow. I had an extremely simple CLI based app I wrote a year ago that I believed was “finished”. After revisiting and refactoring the code, I started to see how I could add further functionality to it.

4. Refactoring code is an invaluable skill. If you critique and improve your own code enough then you’ll be comfortable and savvy enough to refactor code written by your peers and the wider community.

5. You’ll tend to stop making the same “mistakes” in your current, new code. By going back and refactoring your older code you’ll catch on to any unPythonic tendencies you may have, like the ones below.

6. Finally, I believe doing so can help to build relationships! Refactoring code is one of the ways Bob and I maintain our friendship. We share any non-proprietary code that we write with one another so the other can refactor and provide input. If you can get this sort of thing happening with your peers at work or in the community you’ll be better off for it!


<br>
##Refactoring Examples

Okay finally, here we go! Here are some specific lines of the code I revisited and refactored this week. Don’t judge me!


###Unnecessary Code in a for Loop
~~~~
for i in range(len(durations)):
~~~~

I found code where I was using `range` and `len` to get the limit of my `for` loop. It’s a simple one but something I was used to doing with C type programming. Thanks to Python’s awesomeness, I changed it to:

~~~~
for i in durations:
~~~~

<br>
###String Formatting Woes
~~~~
print('The course takes ' + str(total_hours) + ' hours to complete.')
~~~~

Ouch! Again, a simple fix and most definitely a remnant from having learned other languages. Refactored!

~~~~
print(‘The course takes {} hours to complete’.format(total_hours))
~~~~

<br>
###camelCasing

I found a heap of variables and functions written in camel case. *shudder*. They’ll no longer be a problem.

~~~~
quotesListDoc
userInput
quotesList
currentTime
~~~~

<br>
###Manually opening and closing

While not particularly terrible, I found it was much more Pythonic to use a `with` statement to handle the opening and closing of a text file.

~~~~
quotesListDoc = open(“list.txt", "a")
quotesListDoc.write('\n' + time.strftime("%c") + '\n')
    for i in range(len(KIDQUOTES)):
        quotesListDoc.write(KIDQUOTES[i] + '\n')
quotesListDoc.close()
~~~~

I’ll just refactor the whole damn thing.

~~~~
with open(‘list.txt’, ‘a’) as quotes_doc:
    quotes_doc.write(‘\n’ + time.strftime(“%c”) + ‘\n’)
    for i in quotes:
        quotes_doc.write(quotes[i] + ‘\n’)
~~~~

<br>
###Including print in input()

I had a nasty habit of using print() to write my question or statement when I was asking for input().

~~~~
print('Hit Y to continue or N to add another issue. Y/N')
userInput = input()
~~~~

Refactor!

~~~~
user_input = input(‘Hit Y to continue or N to add another issue. Y/N: ‘)
~~~~


<br>
##Conclusion

While most definitely simplistic, the examples above demonstrate how important refactoring is. When I first wrote these snippets, I was using the best way I thought possible.

I just didn’t know any better.

Having gone back and refactored it I’m absolutely stoked to see how far I’ve come! Not only does the code look better but I’m also able to see where I can make future improvements.

The code for writing quotes to a text file. A text file? An sqlite db would be way cooler! Realisations like this make me happy and more motivated than ever to continue learning.

Now go look at some of your earlier code and see what you can refactor!

Keep Calm and Code in Python!

-- Julian

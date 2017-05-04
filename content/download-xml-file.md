Title: How to Download an XML File with Python
Date: 2017-05-04 20:46
Category: Learning
Tags: tutorial, learning, webscraping, requests, xml, beginners, python
Slug: download-xml-file
Authors: Julian
Summary: In this post I detail how to download an xml file to your OS and why it’s not as simple as you’d think
cover: images/featured/pb-article.png

Really? An article on downloading and saving an XML file? “Just use requests mate!”, I hear you all saying. Well, it’s not that simple. At least, it wasn’t as straight forward as that for a beginner like me. Here’s why.


##Parsing is Different to Saving

For sure, experts and beginners alike will have used requests to pull down the contents of a web page. Generally it’s for the purpose of parsing or scraping that page for specific data elements.

What if you wanted to actually *save* that web page to your local drive? Things get slightly different. You’re no longer just reading a text rendered version of the page, you’re trying to save the actual page in its original state.

This is what I found slightly confusing. I wasn’t dealing with a `text = r.text` situation anymore, I was trying to maintain the original format of the page as well, tabs and all.


##Why XML?

I’m talking XML here because I was/am trying to download the actual XML file for an RSS feed I wanted to parse offline. For those of you playing at home, this is for our [PyBites Code Challenge 17](http://pybit.es/codechallenge17.html) (hint hint!).


##Why Download when you can just Parse the feed itself?

Good question! It’s about best practice and just being nice.

In the case of our code challenge (PCC17), how many times are you going to run your Py script while building the app to test if it works? Every time you run that script with your `requests.get` code in place, you’re making a call to the target web server.

This generates unnecessary traffic and load on that server which is a pretty crappy thing to do!

The nicer and Pythonic thing to do is to have a separate script that does the request once and saves the required data to a local file. Your primary scraping or analysis script then references the local file.


##Get to the code already!

Alright, check it out:

~~~~
import requests

URL = "http://insert.your/feed/here.xml"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)
~~~~


It all looks pretty familiar so I won’t go into detail on the usual suspects.

What I’m doing in this code is the following:

- Pulling the xml *content* down using `requests.get`.
- Using a `with` statement to create a file called `feed.xml`. (If the file exists it’ll be overwritten).
- Writing the **contents** of the requests response into the file `feed.xml`.

Here’s why it was a learning exercise for me:

As I open/create the feed.xml file, I’m using the “Mode” `wb`. This means I’m opening the file for writing purposes but **can only write to it in a binary format**.

If you fail to choose the binary mode then you’ll get an error:

~~~~
Traceback (most recent call last):
  File "pull_xml.py", line 12, in <module>
    file.write(response.content)
TypeError: write() argument must be str, not bytes
~~~~

This confused the hell out of me and resulted in me wasting time trying to convert the requests response data to different formats or writing to the external file one line at a time (which meant I lost formatting anyway!).

The binary mode is required to write the actual content of the XML page to your external file in the original format.


Speaking of content. Notice in the final `write` statement I’m using `response.content`? Have any idea how long I spent thinking my use of the usual `response.text` was the only way to do this? Too damn long!

Using the `content` option allows you to dump the entire XML file (as is) into your own local XML file. Brilliant!

> Note for beginners: If you’re reading other people’s code, be prepared to see `with` statements where files are opened `as f`. The same applies to the `requests` module. The line will generally read `r = requests.get(URL)`. I’ve used full form names for the sake of this article thus the words *file* and *response* in my code.


##Conclusion

This is one of those things that we all just get used to doing. Pulling a feed down and saving it to a file is something Bob has done a thousand times so no longer has to give it any extra thought.

For me, however, this took an entire night* of playing around because I’d never done it before and was assuming (silly me!) that the parsing code I've been using `requests` for was all I needed.

I also found that I had to scour a ton of StackOverflow posts and other documentation just to get my head wrapped around this concept correctly.

So with this finally cleared up, it’s time to go attack some feeds!

Keep Calm and Code in Python!

Julian

*Not really an entire night. I do need my beauty sleep!

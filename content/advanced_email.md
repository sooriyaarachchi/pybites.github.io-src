Title: Send Advanced Emails with Python MIME Submodules
Date: 2017-02-01 18:51
Category: Tools
Tags: python, tips, tricks, code, pybites, email, automation, MIME
Slug: python-MIME
Authors: Julian
Summary: Learn how to send richer emails with Python and the MIME Submodules
Status: Draft
cover: images/featured/python-MIME.png

In my earlier post on [sending basic emails with Python smtplib](http://pybit.es/python-smtplib.html) I outlined the bare minimum required to send an email with Python.

While functional, it does however lack more advanced features which I'll touch on in this post. We'll be using the MIME email submodules to create a richer email.


##What is MIME?

For those who are unaware, MIME (Multipurpose Internet Mail Extensions) is a standard that essentially makes emails more functional. As per the [Wikipedia Article](https://en.wikipedia.org/wiki/MIME):

>Multipurpose Internet Mail Extensions (MIME) is an Internet standard that extends the format of email to support:
- Text in character sets other than ASCII
- Non-text attachments: audio, video, images, application programs etc.
- Message bodies with multiple parts
- Header information in non-ASCII character sets



##The Setup

You'll need to import *smtplib* as expected but also the MIME submodules "MIMEMultipart" and "MIMEText":

~~~~
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
~~~~


##Data Entry

Next we'll add the usual header detail to the email. I aimed to make this as Pythonic as possible:

~~~~
from_addr = 'pybitesblog@gmail.com'
to_addr = ['bob@rocks.com', 'julian_is@awesome.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = 'Julian Web Scraper'
~~~~


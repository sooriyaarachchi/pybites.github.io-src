Title: Hiding BCC Recipients in Python MIME Emails
Date: 2017-09-06 18:53
Category: Tools
Tags: python, tips, tricks, code, pybites, email, automation, MIME, bcc
Slug: python-MIME-bcc
Authors: Julian
Summary: How to actually hide the BCC recipients when sending an email with Python MIME.
cover: images/featured/pb-article.png

A few of the programs I’ve created rely on an automated emailer script to notify myself and others of updates. The script uses Python MIME submodules. An issue I’ve been having to date has been keeping the recipient email addresses anonymous.

> If you’re not familiar with Python MIME for sending emails, I’d suggest you start with my two earlier articles: [Send emails with Python smtlib](https://pybit.es/python-smtplib.html) and [Send Advanced Emails with Python MIME Submodules](https://pybit.es/python-MIME.html).


##The Problem - BCC

When sending emails where I’m happy for all email addresses to be visible to recipients (such as to myself and Bob), the code looks like the following:

~~~~
from_addr = 'pybitesblog@gmail.com'
to_addr = ['bob@rocks.com', 'julian_is@awesome.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = 'Test Automation Email'
~~~~

This is the header information code. When the email sends, both Bob and I will be able to see one another on the email.

After some reading and searching online, my understanding was that to make the recipients anonymous, I could use the BCC field as follows:

~~~~
from_addr = 'pybitesblog@gmail.com'
to_addr = ‘pybitesblog@gmail.com’
recipients = ['bob@rocks.com', 'julian_is@awesome.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Bcc'] = ", ".join(recipients)
msg['Subject'] = 'Test Automation Email'
~~~~

Note the differences. I’ve set the `To` address to be the same as the `from_addr` and created a new item `['Bcc']` which then joins the emails listed in `recipients`.

This code actually works. The problem is that I don't get the expected functionality of BCC (recipients aren’t listed). That is, Bob can see that I was BCC’d on the email and vice versa! In the email he receives, the header actually shows “bcc” and shows my email address, completely defeating the purpose!


<br>
##The Solution

Further research was required. As I’ve mentioned, we’re building the header information of the email when we use the `msg['To']` and other options for MIME.

It turns out anything you put in the header is, by design, visible to the recipient. Any email address I assign to `msg['Bcc']’ is again, by design, supposed to be visible to all recipients.

The workaround I’ve found that works for me is to completely omit my list of recipients from the MIME header information altogether and instead include it in the `sendmail()` function.
The current sendmail parameters are:

~~~~
smtp_server.sendmail(from_addr, to_addr, text)
~~~~

With the workaround it’s:

~~~~
from_addr = 'pybitesblog@gmail.com'
to_addr = ‘pybitesblog@gmail.com’
recipients = ['bob@rocks.com', 'julian_is@awesome.com']

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test Automation Email'

smtp_server.sendmail(from_addr, [to_addr] + recipients, text)
~~~~

> Note: You can find the full emailer script in [this article](https://pybit.es/python-MIME.html).

The idea is that the only information **visible to the recipient** when they receive the email is the information we populate MIME `msg` with.

The information in sendmail is not visible to recipients so any addresses we decide to tack on to the “To” argument of sendmail remain hidden.

And THAT is the behaviour I wanted all along!

Keep Calm and Code in Python!

-- Julian

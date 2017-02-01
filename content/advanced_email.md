Title: Send Advanced Emails with Python MIME Submodules
Date: 2017-02-01 11:30
Category: Tools
Tags: python, tips, tricks, code, pybites, email, automation, MIME
Slug: python-MIME
Authors: Julian
Summary: Learn how to send richer emails with Python and the MIME Submodules
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

Next we'll add the missing header detail to the email. I aimed to make this as Pythonic as possible:

~~~~
from_addr = 'pybitesblog@gmail.com'
to_addr = ['bob@rocks.com', 'julian_is@awesome.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = 'Test Automation Email'
~~~~

Breaking that down line by line:

1. Assign your from/sender email address to a variable.

2. Assin your recipient address or addresses to a variable.

3. Assign the MIMEMultipart function to variable.

4. Assign your sender email address variable to the 'From' value in MIME.

5. Assign your recipient addresses to the 'To' value in MIME. Note the .join function is used here to concatenate the email addresses with a comma.

6. Specify your Subject Line and add it to MIME.


Now for the meat. Add the text for the body of your email and again add it to MIME:

~~~~
body = "Hello Everyone!"

msg.attach(MIMEText(body, 'plain'))
~~~~

I've added the data in the body variable to MIMEText in plain text format. You can specify HTML if you wish.


##Send the Email

I'll be reusing the code from the simple email article here with a small addition. First the standard code:

~~~~
smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #Specify Gmail Mail server

smtp_server.ehlo() #Send mandatory 'hello' message to SMTP server

smtp_server.starttls() #Start TLS Encryption as we're not using SSL.

#Login to gmail: Account | Password
smtp_server.login(' pybitesblog@gmail.com ', ' GMAIL APPLICATION PASSWORD ')
~~~~


The additional code is in the sendmail function. We now need to specify the text that we're sending. That is, we take all of the data that was added to the MIMEMultipart function (*msg* variable) and we use it to populate the email:

~~~~
text = msg.as_string()

#Compile email: From, To, Email body
smtp_server.sendmail(from_addr, to_addr, text)
~~~~

And finally, best practice, we close off the SMTP connection and in this case, print a message to indicate the email was sent:

~~~~
smtp_server.quit()
print('Email sent successfully')
~~~~



##Conclusion
Using this framework you can start to send more and more detailed emails. MIME allows you to send attachments which opens all sorts of doors.

Check out the [Python 3 Docs on Email](https://docs.python.org/3/library/email-examples.html) to see some other detailed examples. I like the idea of the HTML message with an alternative plain text version. Very cool!

Keep Calm and Code in Python!

-- Julian

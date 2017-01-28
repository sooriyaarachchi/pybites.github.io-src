Title: Send Emails with Python smtplib
Date: 2017-01-26 19:25
Category: Tools
Tags: python, tips, tricks, code, pybites, email, automation
Slug: python-smtplib
Authors: Julian
Summary: Learn how to send emails using Python
cover: images/featured/python-smtplib.png

I was recently given a [Raspberry Pi](https://www.raspberrypi.org) as a gift and figured it'd make a cool host for cron jobs. I've always wanted to set up an email notification service for myself so I started playing around with *smtplib* in Python.


##Set up an Application Password with Gmail

It was surprisingly simple to send a basic email using my Gmail account. The complexity came from Google's 2-step Verification security settings. If using Gmail, you'll need to [set up an Application Password](https://support.google.com/accounts/answer/185833?hl=en) for the machine you're running your Py script from.

> Once generated, the App Password will be your Gmail Password for this script.


##Sending a Basic Email

The first thing you should try is sending the simplest of emails. Just plain text.

There are a few steps, which I'll detail one by one:

1. Import the smtplib module.

2. Using smtplib, specify the SMTP server and port you'll be accessing. In this example I'm using Gmail's servers.

		import smtplib

		smtp_server = smptlib.SMTP('smtp.gmail.com', 587)

3. The SMTP server you're connecting to requires a sort of 'handshake' for the service to work properly. This is done using the .ehlo() function of smtplib.

		smtp_server.ehlo()

4. As Google doesn't use SSL, we need to kick off TLS Encryption manually.

		smtp_server.starttls()

5. Now for the login. Keep in mind at this point, you'll use the App Password you obtained earlier instead of your usual Gmail password.

		smtp_server.login('pybitesblog@gmail.com', '<App Password>')

6. Next we send the actual email message. The first email address is the address you're emailing from, the second is the recipient.

		smtp_server.sendmail('pybitesblog@gmail.com', 'recipient@gmail.com', 'Subject: Happy Australia Day!\nHi Everyone! Happy Australia Day! Cheers, Julian')

	>Things to note in the above. The \n is mandatory. It's what separates your Subject line from the body of the email. Note: if you're running this in IDLE, when the email is sent successfully, you'll see '{}' characters appear as the return message. If part of a script, you can always add a print statement or other to show this instead.

7. Finally, disconnect from the SMTP server when complete.

		smtp_server.quit()

And we're done! Here's the/my final code:

	import smtplib

	smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.login('pybitesblog@gmail.com', '<App Password>')

	smtp_server.sendmail('pybitesblog@gmail.com', 'recipient@gmail.com', 'Subject: Happy Australia Day!\nHi Everyone! Happy Australia Day! Cheers, Julian')

	smtp_server.quit()
	print('Email sent successfully')


##Next Steps

Clearly this is as basic as it gets. Moving forward you'll want the ability to send more detailed emails with some essence of formatting.

To do this you'll need to import the MIME (Multipurpose Internet Mail Extensions) modules into your script.

I want to expand on this current email example and will do so my next post. It also allows us to make the code a little more Pythonic!


Keep Calm and Code in Python!

-- Julian

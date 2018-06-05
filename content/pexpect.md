Title: PyBites Module of the Week - Pexpect
Date: 2017-07-27 21:31
Category: Modules
Tags: python, tips, code, pybites, pexpect, automation 
Slug: pexpect
Authors: Julian
Summary: A brief overview of the pexpect module
cover: images/featured/pb-article.png

This week I discovered the [Pexpect](https://pexpect.readthedocs.io/en/stable/index.html) module. Where have you been all my life?!

<br>
##What is Pexpect?

Pexpect is a cool automation module. Its main function is to automate interactive processes that provide predictable output. Think apps like telnet, ssh, git and so forth.
We automate these by telling pexpect what to expect from the application and then what to send back.

Pexpect essentially takes your place as a human and starts interacting with the application on your behalf!

The easiest way to explain this is to show you.

<br>
##Key Functionality

There are two main uses for Pexpect that I’ll touch on in this article: `spawn` and `run`.

###The Spawn Class

`pexpect.spawn()` is used to start your application off. The parameter you pass to it is the command you as a human overlord would type into your OS CLI. Eg:

~~~~
child = pexpect.spawn(‘ssh user@192.168.1.1’)
~~~~

Using this example, pexpect will kick off an ssh connection the host. We then have to tell pexpect what to *expect* back.

~~~~
pexpect.expect(‘user@10.1.1.10\’s password:’)
~~~~

You can see that I’m literally telling pexpect what *it* should see when it initiates the first ssh command. I want pexpect to log into this box for me so I’ll need it to pass on my password (never hardcode your password into a script!):

~~~~
pexpect.sendline(‘password’)
~~~~

Pexpect has just submitted my password which results in the ssh connection being successful. I then go back and forth over and over until it’s accomplished the task.

It’s quite a manual process and seems a bit “hacky” but it’s totally cool!


<br>
###The Run Function

The `run` function is a little less exciting. It does what its name implies, run’s a command.

It’ll return the output of said command (if any).

It’s useful for things like kicking off a process or just starting or stopping a service. Pretty much anything that doesn’t really need the depth of the spawn class. For example:

~~~~
from pexpect import *
run(‘service dhcp restart’)
run(‘cd /repo && git pull)
~~~~

Standalone this isn’t mind blowing given we have `os.system` and even crontab but I love having multiple options when writing a script!


<br>
##Example

As a one off, I wrote this script to ssh into my home NAS and manually kick off my [drink water reminder emailer](https://github.com/pybites/100DaysOfCode/tree/master/033):

~~~~
import pexpect
import time

child = pexpect.spawn('ssh user@192.1.1.0’)
time.sleep(2)

child.expect('user@10.1.1.10\'s password:')
time.sleep(2)

child.sendline(‘password’)
time.sleep(2)

child.expect('# ')
child.sendline('cd /opt/development/drink_water && /usr/bin/python3 water_reminder.py')

child.expect('# ')
child.sendline('exit')

print(‘success!’)
~~~~

<br>

- I’ve put some quick `sleep`s in just to pause the script to allow time for the previous command to return.

- Note the inclusion of the shell prompt `#` itself. This is actually necessary and indicates the return of the previous command.


<br>
##Conclusion

While some of these use cases are definitely solvable using other functions and modules I’m still impressed by the possibilities of Pexpect. It’s quite flexible given I’m able to code in the return expectation.

I could have `if` statements to account for different kinds of return values (true or false etc). If the `expect` is different to what I’m… expecting (ha!), then I’d re-run the previous command or just exit with a fail. Lot’s of interesting things to try!

And yes, I know, a lot of this has already been solved by cron. I love cron so I won’t argue with you. I will say that not everything is an OS with cron. Start thinking home automation and suddenly Pexpect seems a little more usable!

Do you use Pexpect for anything cool? Let me know! I’m thinking this would be good fun to use with my Raspberry Pi!

Keep Calm and Code in Python!

-- Julian

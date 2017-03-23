Title: Module of the Week - ipaddress
Date: 2017-03-23 20:12
Category: Modules
Tags: python, tips, code, pybites, ipaddress, sysadmin
Slug: ipaddress
Authors: Julian
Summary: Intro to the ipaddress Python module.
cover: images/featured/pb-article.png
Status: Draft

While playing around with code for our [post on generators](http://pybit.es/generators.html) we discovered the ipaddress Python module! Such a handy little module!

##What does it do?

The ipaddress module simplifies various IP address related tasks. I’m going to outline some of the handier abilities below.

It may seem a little redundant to have a module dedicated solely to IP address related tasks but believe me when I say it can save you a heap of time as an admin and programmer.


##Create an IPv4 or IPv6 address

The ipaddress module allows you to automatically create an IPv4 or IPv6 address without having to specify the type of address.

Just call .ip_address on ipaddress to let the modules figure it out for you:

~~~~
>>> ipaddress.ip_address('192.168.0.1')
IPv4Address('192.168.0.1’)
>>>
>>> ipaddress.ip_address('fe80:0:0:0:200:f8ff:fe21:67cf')
IPv6Address('fe80::200:f8ff:fe21:67cf')
>>>
~~~~

Super simple!


##Defining your host interface

To describe your particular host interface on a network, you call .ip_interface. Note that this uses the now normal notation: ‘192.168.0.1/24’.

~~~~
>>> ipaddress.ip_interface('192.168.0.1/24')
IPv4Interface('192.168.0.1/24')
>>>
~~~~



##Checking your ipaddress object

Now, as Python rocks, we can then assign these values to an object/variable and play with them:

~~~~
>>> #Is it IPv4 or IPv6?
>>> ip = ipaddress.ip_address(‘192.168.0.1’)
>>> ip.version
4
>>>
~~~~


##What’s the netmask?

I hate trying to remember netmasks and how the differing notations match up. I tend to stick with the loveable IP format of 255.255.255.0 whereas others I know love to use the hate-filled 192.168.0.1/24 method. (There, I said it!).

Now I never have to plug my netmasks into a shady online calculator again:

~~~~
>>> net0
IPv4Network('192.168.0.0/24')
>>> net0.netmask
IPv4Address('255.255.255.0')
>>>
~~~~

Kaloo Kalay!


##Defining and checking a network

You can also define an entire network as per the following. I’ll show you why this is awesome in a second:

~~~~
>>> #Define the network first
>>> net0 = ipaddress.ip_network('192.168.0.0/24')
>>>
>>> #Now check to see how many addresses are valid for this network
>>> net0.num_addresses
>>> 256
~~~~



##List out the IP addresses for any given network

This is hands down my favourite feature of the ipaddress module for two reasons:

1. If it hasn’t been a standard Class C (/24) network, I’ve struggled to figure out the valid IP addresses for the network.

2. Creating a list of IP addresses for a given subnet has been a tedious process of iteration.

Here’s how the ipaddress module shows me some love:

~~~~
>>> net0 = ipaddress.ip_network('192.168.0.0/24')
>>> 
>>> for i in net0.hosts():
...     print(i)
... 
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
192.168.0.6
192.168.0.7
192.168.0.8
192.168.0.9
<snip>
192.168.0.253
192.168.0.254
>>>
~~~~

*Drool*

We can then pop this output into a list and manipulate it as we see fit:

~~~~
>>> iplist = []
>>> 
>>> for i in net0.hosts():
...     iplist.append(i)
... 
>>>
>>> f'Bob can take IP {iplist[57]}'
'Bob can take IP 192.168.0.58'
>>>
~~~~



##Playing nice with other modules

As you play around with the ipaddress module you’ll find that the objects won’t play nice with other modules until converted to strings or integers. As per [Section 21.28.2.2](https://docs.python.org/3/library/ipaddress.html) on the official Python documentation.

~~~~
>>> ip = ipaddress.ip_address('192.168.0.1')
>>> str(ip)
'192.168.0.1'
>>>
>>> int(ip)
3232235521
>>>
~~~~


##Conclusion

It may not be the most exciting module out there but as someone who deals with many servers on a daily basis and loves to script these interactions, the ipaddress module is invaluable to me.

Even if it’s just to convert netmask notation…

Keep Calm and Code in Python!

— Julian


Title: Give Generators Some Love
Date: 2017-02-01 11:30
Category: Tools
Tags: python, tips, tricks, code, pybites, generators, iteration
Slug: generators
Authors: Julian
Summary: Learn what a Generator is and check out some different examples.
cover: images/featured/pb-article.png
Status: Draft

Playing around with context managers for last week’s [Challenge 09](http://pybit.es/codechallenge09.html) introduced me to Python Generators and I’ll be forever grateful. They’re exactly what I didn’t know I needed!

First, for the uninitiated, what is a Generator? (If you’re already across Generators, feel free to skip this next part!).


##What is a Generator?

Well, there’s actually not much to it. A generator is just a function that generates values specifically when called with *next()*. Take this absolutely simple generator for example:

~~~~
>>> def num_gen():
...     yield 1
...     yield 2
...     yield 3
... 
>>> 
>>> demo_gen = num_gen()
>>> next(demo_gen)
1
>>> next(demo_gen)
2
>>> next(demo_gen)
3
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
~~~~

As you can see, we have a function *num_gen()* which uses *yield* to return the numbers 1, 2 and 3.

Normally you’d return these numbers via some sort of loop or with 3x print() functions which would print the numbers 1, 2 and 3 all at once.

With a generator however, the numbers are only returned when called using the *next()* function. Here’s what the code does:

1. We take *num_gen()* and assign it to a variable *demo_gen* to make this easier on us.

2. We use the *next()* function on *demo_gen* to request the “next” iteration of the demo_gen function. This results in **the first yield only** being returned.

3. Notice we then have to run *next(demo_gen)* two more times to see the next iteration in the code.

4. Once we’ve exhausted all of the yields within *num_gen()* running *next()* again results in a *StopIteration* error.

> The StopIteration error appears because there are no more yield statements in the function. Calling next on the generator after this does not cause it to loop over and start again.


##Generator Performance Gains

One of the main reasons for using a generator is to avoid having performance issues. For this example it isn’t an issue to work with our 3 numbers in memory but what if we were to be dealing with lists of millions of numbers? 

The performance hit for building lists of millions of numbers within memory isn’t mind blowingly bad but it’s definitely not a great practice.

Generators on the other hand get around the memory hogging by only loading the code into memory that’s returned by *yield*. That is, you’re not processing and storing the entire chunk of code/function in memory, just the next iteration you’re requesting with *next()*.



##Using a For Loop in a Generator

You can use Generators in all sorts of ways. Here’s one that uses a For Loop to double the value of the number I throw into the generator. I can specify how many times the loop is going to run too:

~~~~
>>> def double_nums(num, loops=5):
...     for i in range(loops):
...         num += num
...         yield num
... 
>>> 
>>> demo_gen = double_nums(2)
>>> 
>>> next(demo_gen)
4
>>> next(demo_gen)
8
>>> next(demo_gen)
16
>>> next(demo_gen)
32
>>> next(demo_gen)
64
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
~~~~


##Using a While Loop within a Generator

Now let’s say we want it to indefinitely double every number but only when we want to. The generator is necessary otherwise you’d run out memory and crash your machine.

~~~~
>>> def num_gen(num):
...     while True:
...         num += num
...         yield num
... 
>>> 
>>> 
>>> demo_gen = num_gen(2)
>>> 
>>> next(demo_gen)
4
>>> next(demo_gen)
8
>>> next(demo_gen)
16
>>> next(demo_gen)
32
>>> next(demo_gen)
64
>>> next(demo_gen)
128
…
~~~~

This code will continue doubling the number but only when *next()* asks for the number. Nothing is sitting in memory waiting to just return a number.



##Using a List within a Generator

Of course, you can also choose to use a list. It’s overkill to use a generator for the following example but again, on a larger scale it’d be much more appropriate. This prints out the names of some of my favourite games:

~~~~
>>> games_list = ['Warcraft', 'Battlefield', 'Need4Speed', 'Donkey Kong 2']
>>> 
>>> demo_gen = print_games(games_list)
>>>
>>> next(demo_gen)
'Warcraft'
>>> next(demo_gen)
'Battlefield'
>>> next(demo_gen)
'Need4Speed'
>>> next(demo_gen)
'Donkey Kong 2'
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
~~~~



##Use a Generator with HTML (BOB PLEASE ADD DESCRIPTION BELOW. THANKS!)

<DESCRIPTION HERE>

~~~~
>>> def gen_html(self):
...     li = '<li><a href="{}">{}</a></li>'
...     yield '<ul>'
...     for item in self.entries:
...         title = item['title']
...         url = item.get('link')
...         if not url:
...             url = item['id']
...         yield li.format(url, title)
...     yield '</ul>'
... 
>>> 
~~~~



##Using a Generator to SSH to Multiple Hosts Idea

I came up with a [useful SSH script](https://github.com/pybites/challenges/blob/solutions/09/with_ssh.py) for last week’s context manager challenge.

It works great but is only for one host.

A cool idea from here (that I’ll probably use for work now that I think about it!) would be to take the script and refactor parts of it such that we use a generator to connect to multiple hosts. Perhaps to run a health check command?

The catch would be the authentication, though it shouldn’t be an issue if your credentials are the same for each server you’re connecting to.

If that can be worked around then all you’d need to do is pass a list of host IPs/hostnames to the generator. Every time you run *next()* against the generator you should get the next host in the list.

Simplistically but potentially it could look like this:

~~~~
host_list = [‘192.168.0.1’, '192.168.0.2’, '192.168.0.3’, '192.168.0.4’]

def check_hostname(host_list):
    for host in host_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
            yield ssh_stdout.readlines()
        finally:
            ssh.close()


gen = check_hostname(host_list)

for i in (range(5)):
    print(next(gen))
    f'Hit Enter to try the next host.'; input()
~~~~

The for loop to iterate through the generator could be a while loop but you get the idea. The output for this would look something like this:


~~~~
$ python gen_ssh_script.py
[‘Host1\n’]

[‘Host2\n’]

[‘Host3\n’]

[‘Host4\n’]

Traceback (most recent call last):
  File "gen_ssh_script.py", line 23, in <module>
    print(next(gen))
StopIteration
~~~~

This is extremely rough of course - I’m just playing around as I write this post! (Half the fun right?!).


##Conclusion

Generators are extremely useful for keeping memory usage low. Not a huge deal for your run of the mill script at home or on your laptop but definitely worth keeping in your coding arsenal.

> There are many ways to skin a… actually, we’re animal lovers here. There are many ways to code a solution! As I wrote the SSH script above I was thinking it’d be much easier to do it differently (not force the generator) but I wanted to for the sake of this post.

Do you use generators in any creative ways? Maybe you can *generate* some interest with your solutions…  pun intended! [I’m here all week!](https://www.youtube.com/watch?v=bcYppAs6ZdI).

Keep Calm and Code in Python!

— Julian

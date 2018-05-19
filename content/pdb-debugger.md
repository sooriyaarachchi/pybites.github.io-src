Title: How to Use Pdb to Debug Your Code
Date: 2017-10-24 13:00
Category: Modules
Tags: pdb, debugging, troubleshooting, bugs, modules
Slug: pdb-debugger
Authors: Bob
Summary: The larger part of our coding time is spent reading and debugging code already written. For this Python's [pdb](https://docs.python.org/3.7/library/pdb.html) is an unmissable module in your Python toolbox. In this article I show you the most common options and some practical examples.
cover: images/featured/pb-article.png

The larger part of our coding time is spent reading and debugging code already written. For this Python's [pdb](https://docs.python.org/3.7/library/pdb.html) is an unmissable module in your Python toolbox. In this article I show you the most common options and some practical examples.

## How to invoke the debugger?

You can invoke it as a script which puts you right at the start:

	$ python -m pdb buses.py
	> /Users/bbelderb/code/buses.py(1)<module>()
	-> from urllib.request import urlopen
	(Pdb)

More commonly you want to break into the debugger from a running program. To do this use this one-liner at the location where you want to start debugging:

	> import pdb; pdb.set_trace()

> Note that Python 3.7 improves this adding a new built-in function called `breakpoint()` - see [PEP 553](https://www.python.org/dev/peps/pep-0553/)

## Common switches

[There are many](https://docs.python.org/3.7/library/pdb.html#debugger-commands)! 

You probably will use only a few though and pdb lets you conveniently use their one letter shortcuts. 

* Stepping through a program:

	- __n__(ext) -> Continue execution until the next line in the current function is reached or it returns.
	- __s__(tep) -> Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).
	- __r__(eturn) -> Continue execution until the current function returns.
	- __u__(p) and __d__(own) -> Move the current frame count (default one) levels up/down in the stack trace (to an older/newer frame).
	- __c__(ont(inue)) can be useful if you have multiple breakpoints, it continues execution until a next breakpoint is encountered.
	- __unt__(il) [lineno] -> Without argument, continue execution until the line with a number greater than the current one is reached. -> useful to get out of a for loop.
	- __b__(reak) [lineno] and __cl__(ear) to set / clear a break point in the current file (it even accepts a condition).

> The difference between next (n) and step (s) is that step stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.

* Print context

	- First of all at the pdb prompt you can type any variables of the program (including builtins like `locals()`), or set new variables.
	- __l__(ist) -> List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing.
	- __w__(here) -> Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands. -> handy for web frameworks
	- __bt__ -> Get a stack trace of the functions that have been called so far.
	- __pp__ expression -> Like the p command, except the value of the expression is pretty-printed using the pprint module -> very useful for nested data structures.

* Other: 
	- Cntrl + d or __q__(uit) to leave the debugger and stop execution.
	- Use __h__(elp) or ? to list all commands.

> Single letter variables are bad for code readability, but the clash with common pdb shortcuts is another reason to avoid them at all costs.

## Hello World example

OK enough theory let's write some code:

	def sum(val1, val2):
		val2 = 0
		newval = val1 + val2
		return newval

	values = range(1, 11)
	total = 0

	import pdb; pdb.set_trace()

	for val in values:
		val = sum(val, 1)
		total += val

	assert total == 65

Yes it's silly and the bug is obvious, but the goal is to show pdb.

As you see I already set the breakpoint. When I run this code it drops into the debugger. It shows me the next line to be executed:

	> /Users/bbelderb/code/sum.py(11)<module>()
	-> for val in values:
	(Pdb)

I can print variables:

	(Pdb) values
	range(1, 11)

Stepping through the for loop:

	> /Users/bbelderb/code/sum.py(11)<module>()
	-> for val in values:
	(Pdb) n
	> /Users/bbelderb/code/sum.py(12)<module>()
	-> val = sum(val, 1)
	(Pdb) val
	1
	(Pdb) n
	> /Users/bbelderb/code/sum.py(13)<module>()
	-> total += val
	(Pdb) val
	1
	(Pdb) n
	> /Users/bbelderb/code/sum.py(11)<module>()
	-> for val in values:
	(Pdb) n
	> /Users/bbelderb/code/sum.py(12)<module>()
	-> val = sum(val, 1)
	(Pdb) val
	2
	(Pdb) l
	8
	9  	import pdb; pdb.set_trace()
	10
	11  	for val in values:
	12  	    val = sum(val, 1)
	13  ->	    total += val
	14
	15  	assert total == 65
	[EOF]

You can move the breakpoint to the function but as it is little code I just use __s__(tep):

	> /Users/bbelderb/code/sum.py(11)<module>()
	-> for val in values:
	(Pdb) n
	> /Users/bbelderb/code/sum.py(12)<module>()
	-> val = sum(val, 1)
	(Pdb) s
	--Call--
	> /Users/bbelderb/code/sum.py(1)sum()
	-> def sum(val1, val2):
	(Pdb) s
	> /Users/bbelderb/code/sum.py(2)sum()
	-> val2 = 0
	(Pdb) s
	> /Users/bbelderb/code/sum.py(3)sum()
	-> newval = val1 + val2
	(Pdb) val1
	3
	(Pdb) val2
	0
	(Pdb) n
	> /Users/bbelderb/code/sum.py(4)sum()
	-> return newval
	(Pdb) newval
	3

It is obvious that val2 gets explicitly set to 0, but if it was less obvious inspecting the variables might be all you need.

## Real World example

Another example I found [on SO](https://stackoverflow.com/q/44680650). I shortened the code a bit to keep it simple:

	from urllib.request import urlopen
	from xml.etree.ElementTree import parse

	def getbuses():
		u = urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
		data = u.read()
		f = open('rt22.xml', 'wb')
		f.write(data)
		f.close()
		doc = parse('rt22.xml')
		running_buses = {}
		for bus in doc.findall('bus'):
			idbus = int(bus.findtext('id'))
			lat = float(bus.findtext('lat'))
			lon = float(bus.findtext('lon'))
			direction = str(bus.findtext('d'))
			running_buses[idbus] = {lat, lon, direction}
		return running_buses

	def print_routes(running_buses):
		print('Running buses on route 22:\n')
		for b, (lat, lon, direction) in running_buses.items():
			print('Bus number: {}'.format(b))
			print('- Latitude: {}'.format(lat))
			print('- Longitude: {}'.format(lon))
			print('- Direction: {}'.format(direction))

	def main():
		running_buses = getbuses()
		print_routes(running_buses)

	if __name__ == '__main__':
		main()

The leads to weird results:

	Bus number: 1906
	- Latitude: 41.9041748046875
	- Longitude: -87.63142395019531
	- Direction: North Bound
	Bus number: 1932
	- Latitude: 41.968283335367836
	- Longitude: South Bound
	- Direction: -87.66738806830512
	Bus number: 1910
	- Latitude: -87.67295837402344
	- Longitude: 42.01838684082031
	- Direction: North Bound

This is again a pretty simple use case for pdb:

	> /Users/bbelderb/code/debug.py(14)getbuses()
	-> for bus in doc.findall('bus'):
	(Pdb) n
	...
	> /Users/bbelderb/code/debug.py(19)getbuses()
	-> running_buses[idbus] = {lat, lon, direction}
	(Pdb) idbus
	1906
	(Pdb) lat
	41.90836715698242
	(Pdb) lon
	-87.63148498535156
	(Pdb) direction
	'North Bound'
	(Pdb) n

The variables seem correct, but if I print the data structure I see they appear in a different order: 

	> /Users/bbelderb/code/debug.py(14)getbuses()
	-> for bus in doc.findall('bus'):
	(Pdb) running_buses
	{1906: {'North Bound', 41.90836715698242, -87.63148498535156}}
	(Pdb)

As explained in the SO thread it's because of the use of set instead of a tuple, former does not keep order.

I realize this example does not show much pdb magic so maybe if we do A. a code challenge where you use it upon your next debugging exercise or B. record a video when we are hunting down a nasty bug ourselves. To be continued ...

![learning to debug with pdb is an essential Python developer skill]({filename}/images/banners/pb_pdb.png)

## Conclusion and resources

As you can see this is an essential skill for any developer. Print and unittest can get you far, but moment inevitably comes you have to catch bugs *in the act*.

For more info check out [the docs](https://docs.python.org/3.7/library/pdb.html) or Doug Hellmann's [PyMOTW series](https://pymotw.com/2/pdb/) which has a very extensive coverage of pdb.

But that might be a lot of reading. You can also get a concise overview watching Clayton Parker's PyCon talk: [So you think you can PDB?](https://www.youtube.com/watch?v=P0pIW5tJrRM) It shows a lot of good examples and it peaked my interest to try out [pdb++](https://pypi.python.org/pypi/pdbpp/).

---

Keep Calm and Code in Python!

-- Bob

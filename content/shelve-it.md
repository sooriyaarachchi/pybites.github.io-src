Title: Shelve It!
Date: 2017-02-14 20:30
Category: Learning
Tags: shelve, python, tips, tricks, code, pybites, database
Slug: shelve-it
Authors: Julian
Summary: Shelve basics and a question on how best to manage the DB.
cover: images/featured/shelve-it.png
Status: Draft

When Bob first spoke about Python Shelves a while ago, I thought he'd gone bonkers. This was mainly because he was talking about his "Python shelve" storing book data in a script he was writing. 

"How the heck did you get a bookshelf in Python?!", I wondered. Little did I know he was talking about an awesome persistent storage option.

My first foray into Python shelves was actually rather painless (for me). I was impressed by how simple they were. It was pretty much the same process as opening and working a text file.


##Shelve It!

A quick overview for the uninitiated.

~~~~
import shelve

db = shelve.open('data')

name = 'Julian'
db['db_names'] = name

db.close()
~~~~

Break it down!

1. We import the shelve module.

2. *shelve.open('data')* opens (or creates in this case as it doesn't exist yet) a database .db file called *data*. This is assigned to the *db* variable.

3. Create a variable *name* and it assign it the name Julian (so vain!).

4. The interesting part. We now assign the *name* variable (containing 'Julian')to the key *db_names* within the *db* shelf.

5. We close off our access to the *db* shelf.

At this point, the *name* variable has been stored in a shelf called *data.db*. This .db file, by default, is located in the same directory that your script was run from.


##UnShelve It!

It's not actually called unshelving. Just roll with it.

To read the data back in, we do the following:

~~~~
import shelve

db = shelve.open('data')

name = db['db_names']

print(name)

db.close()
~~~~

The read in of the data here is the 3rd line of code. In this line we take the object stored in *db_names* within the *db* shelf and assign it to *name*. The string in *name* (Julian) is then printed.


##Noteworthy

The above is super basic of course. Shelves become really handy when we start storing lists and dicts in them.

There is a catch though. Any data you read in from the shelf is not automatically updated in the shelf if changed by your script. Using the above script, after reading in *db_names*, if we were to change the name variable to contain 'Bob' instead of 'Julian', that update would not be pushed back to the *db* shelfThere is a catch though. Any data you read in from the shelf is not automatically updated in the shelf if changed by your script. Using the above script, after reading in *db_names*, if we were to change the name variable to contain 'Bob' instead of 'Julian', that update would not be pushed back to the *db* shelf.

To enable automatic writing to the shelf you can open the shelf with "writeback" enabled:

~~~~
db = shelve.open('data', writeback=True)
~~~~

While this can be super handy, it can be a bit of a memory hog if you're not careful. The data that needs to be changed is stored in cache while your program runs. It's actually only written to the shelf.db file when the shelf file is closed with *.close()*.


##A Question On Opening and Managing Shelf Data

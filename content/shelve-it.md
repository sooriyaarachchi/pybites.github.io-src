Title: Shelve It!
Date: 2017-02-14 00:48
Category: Learning
Tags: shelve, python, tips, tricks, code, pybites, database
Slug: shelve-it
Authors: Julian
Summary: Shelve basics and a question on how best to manage importing the DB.
cover: images/featured/shelve-it.png

When Bob first spoke about Python Shelves a while ago, I thought he'd gone bonkers. This was mainly because he was talking about his "Python shelve" storing book data in a script he was writing. 

"How the heck did you get a bookshelf in Python?!", I wondered. Little did I know he was talking about an awesome, persistent storage option.

My first foray into Python shelves was actually rather painless (for me). I was impressed by how simple they were. They were almost as simple as opening and working text files.


##Creating a Shelf File

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

3. Create a variable called *name* and it assign it the name Julian (so vain!).

4. The interesting part. We now assign the *name* variable (containing 'Julian') to the key *db_names* within the *db* shelf.

5. We close off our access to the *db* shelf.

At this point, the *name* variable has been stored in a shelf called *data.db*. This .db file, by default, is located in the same directory that your script is run from.


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

The above is super basic of course. Shelves become really useful when we start storing lists and dicts in them.

There is a catch though. Any data you read in from the shelf is not automatically updated in the shelf if changed by your script. Using the above script, after reading in *db_names*, if we were to change the name variable to contain 'Bob' instead of 'Julian', that update would not be pushed back to the *db* shelf.

To enable automatic writing to the shelf you can open the shelf with "writeback" enabled:

~~~~
db = shelve.open('data', writeback=True)
~~~~

While this can be super handy, it can be a bit of a memory hog if you're not careful. Any changes being made during execution are stored in cache until the shelf file is closed with *.close()*. This is when they're written to the shelf file.


##The Wall I Hit with Shelves

My biggest hurdle with regards to shelves was how to manage a script that was importing the shelf data when it was only being run for the first time. That is, before the db file had even been populated with data.

If I try to run the above code to read in data before *db_names* even exists, I'll get an error.

I wasn't actually too sure how to approach this. Should I:

1. Have some sort of configuration/setup script that runs separately before running the main program?

2. Have a bunch of if statements?

3. Implement a cli based menu system that allows the user to choose when to add items?

As with all things Python, I found I was *try*-ing (pun intended!) too hard. It was as simple as using *try*:

~~~~

name = []

while True:
    try:
        with shelve.open('data') as db:
            name = db['db_names']
            break
    except:
        print("Please enter a  name to begin: ")
        name.append(input())
        break 
~~~~

It works too!

This situation got me thinking though. There's more than one way to skin a... *ahem*... potato?

How would you Pythonistas handle this? What sort of approach do you take when it comes to dealing with shelves?

For now I'll stick with *try* but I'm keen to know what you think.

Keep Calm and Code in Python!

-- Julian

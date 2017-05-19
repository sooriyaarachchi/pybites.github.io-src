Title: How to Create Your Own Steam Game Release Notifier
Date: 2017-05-19 19:53
Category: Learning
Tags: learning, code, programming, python, sqlite3, xml, email, automation, tools, feedparser, game
Slug: steam-notifier
Authors: PyBites
Summary: In this post we demonstrate ways in which you can parse common data formats used in Python.
cover: images/featured/pb-article.png

If you’ve been following our [100 Days of Code Challenge](http://pybit.es/special-100days.html) you’ll have noticed that I’ve been contributing snippets of code relating to the [Steam](http://store.steampowered.com/) gaming platform and store.

When people ask us what the best way to learn Python is, we always tell them to get their hands dirty and to [learn by doing](http://pybit.es/learn-by-doing.html). Idea wise, we tell people to scratch their own itch. That’s exactly what I’ve been doing between code challenges, work and family life. I made my own Steam Game Notifier that emails me the latest Steam game releases!

Steam does have its own RSS feed which I could have just loaded in an RSS app but there’s no fun in that! I wanted the challenge of coding up a solution myself. This post will break down the code and describe the solution.

[Full code here](https://github.com/pybites/blog_code/tree/master/steam_notifier).

<br>
##Splitting the Code Up

Looking at the above code link you’ll notice there are four Python scripts that make up the program:

- **email_list.py:** Stores the email addresses of recipients for this tool.
- **emailer.py:** The script that sends the email. It reads in the emails stored in email_list.py.
- **pull_xml.py:** This script pulls down the newreleases.xml file from the Steam servers and saves it to the local directory.
- **xml_steam_scraper.py:** The main script. This parses the XML file and manipulates the database.

<br>
##pull_xml.py

We’ll attack this in executional order. First up is `pull_xml.py`.

This is a very simple `requests` pull. It requests the newreleases.xml file from Steam and saves the contents to the local directory. The main thing to note in the code is the `wb` open mode:

~~~~
with open('newreleases.xml', 'wb') as f:
    f.write(r.content)
~~~~

The `wb` (write binary) mode is required to correctly write the XML data to a local file called new releases.xml.

<br>
##xml_steam_scraper.py

Now for the meat. I’ll cover the noteworthy parts as it should hopefully help anyone learning Python.

<br>
~~~~
Game = namedtuple('Game', 'title url')
~~~~

Here we have a `namedtuple` from the `collections` module. Read this [docs.python doc](https://docs.python.org/3/library/collections.html#collections.namedtuple) if you’re new to these. Essentially we’re creating a tuple subclass named `Game`. It has two fields associated with it: `title` and `url` (more on this later).

<br>
~~~~
def check_create_db():
    with sqlite3.connect(DB_NAME) as connection:
        c = connection.cursor()
        try:
            c.execute("""CREATE TABLE new_steam_games
                (Name TEXT, Link TEXT, Emailed TEXT)
					""")		
        except:
            pass
~~~~

This entire function handles the database creation we’re using for this program. The `sqlite` code will create the DB `steam_games.db` (as per the declaration at the top of the code) if the DB doesn’t exist. If it does exist, it just continues on.

<br>
~~~~
c.execute("SELECT Name from new_steam_games")
db_games_list = c.fetchall()
~~~~

Within the `pull_db_data()` function you’ll see this line. This code will pull the `Name` data from the `steam_games.db` file and populate the `db_games_list` list with the data.

<br>
~~~~
#Ignore my intentionally awesome function names
def parse_that_feed_baby():
    feed_list = []
    feed = feedparser.parse(FEED_FILE)
    for entry in feed['entries']:
        game_data = Game(title=entry['title'], url=entry['link'])
        feed_list.append(game_data)
    return feed_list
~~~~

This is where I use `feedparser` to interrogate the `newreleases.xml` file. We also see the usage of that `namedtuple` `Game`. The fields we specified earlier are being assigned “entries” pulled from the XML file with feedparser.

The `title` field is given the XML “title” of the game; the `url` field is given the link to the game.

This is done for every individual “entry” (game) in the XML file using the `for` loop. It’s all appended to `feed_list`.

<br>
~~~~
def check_for_new(feed_list, db_games):
    new_games_list = []
    for data in feed_list:
        if (data.title,) not in db_games:
            new_games_list.append(data)
    return new_games_list
~~~~

This function creates an empty list called `new_games_list`. It then checks whether `data.title` (`.title` being the field from the namedtuple) is **not** in the existing games database `db_games`. I’m essentially doing a name match. Eg: Does the game name from the feed list exist in the list of games already in the database.

If the name **isn’t** in the existing DB, then we add it to the `new_games_list` list.

<br>
~~~~
c.executemany("INSERT INTO new_steam_games VALUES (?, ?, 0)", new_games)
~~~~

Finally, at the end of the `main()` function, we add the **new games** to the DB. The 2x ?s are placeholders for the data in the `new_games` list. The 0 at the end will be explained in a moment.


<br>
##DB Table Layout and Emailed Flag

The DB we create at the start of the script has 3x columns: `Name`, `Link`, and `Emailed`, all of which are `TEXT` types.

`Name` and `Link` are self explanatory but why `Emailed`?

I needed a way to determine whether a row (game) had been emailed out already. I decided to go with a boolean flag, i.e., Yes/No, True/False, 0/1.

When new games are added to the DB at the end of the code, they’re added with a 0 in the 3rd column (`Emailed`). This indicates that they are new and have **not** been emailed.

<br>
##emailer.py

I’ve covered sending advanced emails using Python MIME in a [previous article](http://pybit.es/python-MIME.html) so have a read through of that for the basics if you’re not sure what you’re looking at here.

The important code is this:

~~~~
with sqlite3.connect(DATA_FILE) as connection:
    c = connection.cursor()
    c.execute("SELECT Name, Link FROM new_steam_games WHERE Emailed='0'")
    for item in c.fetchall():
        body += item[0] + ': ' + item[1] + '\n'
    c.execute("UPDATE new_steam_games SET Emailed='1'")
~~~~

In this code I grab the data from the database that has a “0” in the `Emailed` column. (Pulling the new games!).

I then add the name, `item[0]`, and link, `item[1]` to the body of the email using a `for` loop. This will add the new games one by one.

After this, the games are then flagged as being emailed by changing the `Emailed` flag to “1”. This will ensure that the next time the emailer is run, the same games don’t get emailed again.

<br>
##Automate it!

Done! What next? Add it to a cron job and automate the sucker!

I’ve got the pull, the feedparse and emailer all running on separate cron jobs, one after the other (2 mins apart).

The pull writes over newreleases.xml with fresh data; feedparser updates the DB with fresh data (if any) and the emailer sends out any new games.

An example crontab entry could be:

~~~~
30 20 * * * cd /opt/development/steamscraper && /usr/bin/python3 pull_xml.py
~~~~

<br>
##Improvements

I’m seeing plenty of room for improvement just writing this article! The curse of the programmer!

- What happens if there isn’t a new game to email out? Does it break or just send an empty email? (No idea at the time of writing!). The script should either not send an email or (easier) just email a “No new games” message.

- In the xml_steam_scraper.py script I access the sqlite DB using a `with` statement **three** times. This seems unpythonic to me. I need to figure out a better way to talk to the DB throughout the script. I could do a `connect` at the start and then a `close` at the end of `main()` but is it Pythonic to leave the DB connection open for the entirety of the script?

- I could have some nicer text (a header maybe?) in the email rather than just a plain text dump of the Names/URLs.

- What happens if the emailer fails *after* I’ve already changed the `Emailed` DB flag to 1? The new games will **not** have been mailed out but the DB will have potentially been updated to reflect that they have been. I could probably move the update to the end of the script to avoid this.

- Create funnier function names (just on my copy of the code of course!).

<br>
##Learning

I’m stoked that this thing actually WORKS! And boy did I learn a lot! In this program alone I’ve tackled so many different concepts:

- feedparser (web scraping)
- sqlite (persistent storage)
- with statements
- smtplib (emailers)
- requests (more web scraping)
- collections (namedtuples)

The biggest hurdle for me was figuring out how to store the data in the DB and determine whether an entry had been emailed or not. That took me *ages*!

Very happy with the final result, regardless of its Pythonicness (roll with the word). I’ll keep refactoring as I go but for now I’ll enjoy the satisfaction of automatically emailing myself games to buy!

If you have any feedback or improvements *please* let me know. It’s the best way to learn!

Keep Calm and Code in Python!

-- Julian

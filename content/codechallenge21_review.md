Title: Code Challenge 21 - Electricity Cost Calculation App - Review
Date: 2017-06-05 11:15
Category: Challenges
Tags: codechallenges, calculation, electricity, Flask, Django, cli, data, BeautifulSoup, Python Anywhere, Pythonista 3
Slug: codechallenge21_review
Authors: PyBites
Summary: In this article we review this week's [code challenge #21](http://pybit.es/codechallenge21.html) for which we got some nice PRs.
cover: images/featured/pb-challenge.png

In this article we review this week's [code challenge #21](http://pybit.es/codechallenge21.html) for which we got some nice PRs.

This was a relatively easy challenge but building it out to something cool had its challenge. We are stoked to receive solutions with similar functionality yet using different technologies.

## Submissions

We merged 4 PRs onto our [Community branch](https://github.com/pybites/challenges/tree/community):

* Martin made [a nice app](https://github.com/pybites/challenges/tree/community/21/clamytoe) for iPhone use with Pythonista 3. We really like how you guys provide screenshots and other meta data.

* Dante made a cool Flask app: [wattapp](https://github.com/pybites/challenges/tree/community/21/dseptem/wattapp). Features include: simple interface, history of energy consumption and an option to clear items. Check it out to learn about useful Flask extensions like Flask-SQLAlchemy and Flask-WTF for forms.

* And we got some Django! Wonderfulboyx made an energy app that lets us add devices and companies, then do the calculation based on inputs. It also saves the history. It's hosted [here](http://wonderfulboyx.pythonanywhere.com/).

* PyBites: we made a simple [cli app](https://github.com/pybites/challenges/tree/community/21/bbelderbos) that loads in real data from the web: kwh per country and estimated wattages per device (parsing this was a challenge, html tables arg!). It's not done yet, we still need to cache the data and write some more tests. We found out that energy in expensive in Spain!

---

Everytime a PR comes in we cheer with joy, humbled by the fact we see you are stretching yourselves by taking our challenges (we do too!). Keep up the good work, the stuff you are building is amazing!

Remember there is no deadline, you can PR your code anytime. Just remember to isolate (branch) your changes and submit against our Community branch (as per instructions).

When we merge your work onto our Challenges branch the PR auto-closes but you can still add comments to it. For new revisions, just open a new PR.

Come code with us forking [our challenges repo](https://github.com/pybites/challenges). Have fun!

---

Keep Calm and Code in Python!

-- Bob and Julian

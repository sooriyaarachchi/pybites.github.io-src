Title: Code Challenge 46 - Add Continuous Integration (CI) to Your Project
Date: 2017-12-11 12:00
Category: Challenge
Tags: CI, Jenkins, Heroku, Travis, Semaphore, automation, deployment, Docker, Better Code Hub, SIG
Slug: codechallenge46
Authors: PyBites
Summary: Hi Pythonistas, becoming a Python developer is partly about knowing your tools. Managing your environment, testing and continuous integration are unmissable skills when you start working on bigger projects with a team. So we decided to dedicate a code challenge to deployment. Take an existing projects or make a demo app from scratch, the goal is to build an automated pipeline. Will you be the next guy or girl at work receiving kudos for setting up a Jenkins server? Have fun!
cover: images/featured/pb-challenge.png

> It's not that I'm so smart, it's just that I stay with problems longer. - A. Einstein

Hi Pythonistas, becoming a Python developer is partly about knowing your tools. Managing your environment, testing and continuous integration are unmissable skills when you start working on bigger projects with a team. So we decided to dedicate a code challenge to deployment. 

Take an existing projects or make a demo app from scratch, the goal is to build an automated pipeline. Will you be the next guy or girl at work receiving kudos for setting up a Jenkins server? Have fun!

## CI Defined

CI is great to streamline and automate deployment of your software, saving time and quickly finding regression bugs. It enforces quality of your software. For a broader definition check out Martin Fowler's [Continuous Integration article](https://martinfowler.com/articles/continuousIntegration.html):

> Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily - leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly. 

## The Challenge

1. Choose one of your existing projects or start a small demo project.

2. If you have tests, good move on to the next step, if not add them now - [overview testing](http://docs.python-guide.org/en/latest/writing/tests/) / if you go with pytest consider taking [Code Challenge 39 - Writing Tests With Pytest](https://pybit.es/codechallenge39.html) too.

3. Choose a tool to automate your build. We played a bit with [Travis CI](https://travis-ci.org) and it's nice. Alternatively there is [Semaphore](https://semaphoreci.com/) or what about [Jenkins](https://jenkins-ci.org/)? We want you to be free. You can check out the [Hitchhiker's guide](http://docs.python-guide.org/en/latest/scenarios/ci/) or Full Stack Python's [CI](https://www.fullstackpython.com/continuous-integration.html) and [Jenkins](https://www.fullstackpython.com/jenkins.html) reference pages and choose the tool you feel most comfortable with.

4. Open a PR against our repo with a *username*/README.md file detailing what you did, ideally with a screenshot of an automated build. We are happy to share it with our community [in our monthly review post](https://pybit.es/pages/challenges.html).

5. Bonus: Rob van der Leek (SIG) wrote a great article: [How to build a modern CI/CD pipeline](https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b). You get bonus karma if you additionally use Docker and Better Code Hub.

Good luck and if any issues or brainstorming, there is ...

## Pybites Slack

You like these challenges? We have published [quite a few](https://github.com/pybites/challenges) and we're not planning to stop anytime soon!

You really like them and plan on submitting (PR'ing) your work? Then consider joining our private Slack channel sending us [an email](mailto:pybitesblog@gmail.com). This way you get the unique opportunity to learn from other passionate Pythonistas and share your experience.

## Get Credit

As always you can PR your work to our Community branch of our [Challenges repo](https://github.com/pybites/challenges). We will include it in our review post. Our PR template also lets you reflect a bit on your learning and provide some feedback how we can keep this interesting for you. See detailed instructions [here](https://github.com/pybites/challenges/blob/master/INSTALL.md).

We are working on a Code Challenge Platform to facilitate this process, stay tuned ...

---

## About PyBites Code Challenges

Our goal is to learn and teach you Python [through practical exercises](https://pybit.es/learn-by-doing.html). We are almost a year in now and the progress we've seen in our Python learning, as well as that of our growing community, is absolutely amazing! Besides, learning a programming language is way more fun as a community!

For any feedback [tweet us](https://twitter.com/pybites) or [drop us an email](mailto:pybitesblog@gmail.com). If you have a cool idea for a challenge please open [an issues against our Challenges repo](https://github.com/pybites/challenges/issues) and we can discuss it there. 

Thanks for your support.

---

Keep Calm and Code in Python!

-- PyBites

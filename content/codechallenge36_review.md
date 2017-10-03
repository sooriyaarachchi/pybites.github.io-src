Title: Code Challenge 36 - Create an AWS Lambda Function - Review
Date: 2017-10-03 11:00
Category: Challenges
Tags: codechallenges, AWS, lambda, lambda function, guest, automation, microservices
Slug: codechallenge36_review
Authors: PyBites
Summary: In this article we review last week's [Create an AWS Lambda Function](http://pybit.es/codechallenge36.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Create an AWS Lambda Function](http://pybit.es/codechallenge36.html) code challenge. 

### Submissions

* [mjhea0](https://github.com/mjhea0): for this challenge, I created [a tutorial](https://realpython.com/blog/python/code-evaluation-with-aws-lambda-and-api-gateway/) that details how to use AWS Lambda and API Gateway to created a code evaluation API. [Live demo](https://realpython.github.io/aws-lambda-code-execute/).

* [bbelderbos](https://github.com/bbelderbos): as per Real Python's article I set up my Lambda function to receive payload via API Gateway. The lambda retrieves a PR number (id) via a POST request and retrieves the associated .py files via the GH API. It stores them in /tmp and runs PEP8 against them. If good it returns 'ok', else it shows the violations. 

	TODOS: add a webhook for our Challenges repo to run this automatically. It would be nice to run unittests on test_*.py files. You could actually turn this into a simple CI which when done I will write an article about. Project [here](https://github.com/bbelderbos/first-aws-lambda).

### Hacktoberfest

Make sure you sign up for [Hacktoberfest](https://hacktoberfest.digitalocean.com/sign_up/register) so each Code Challenge PR you do counts towards earning some cool swag! You can check your progress [here](https://hacktoberfestchecker.herokuapp.com).

---

Keep Calm and Code in Python!

-- Bob and Julian

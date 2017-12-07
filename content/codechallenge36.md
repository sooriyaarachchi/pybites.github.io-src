Title: Code Challenge 36 - Create an AWS Lambda Function
Date: 2017-09-12 11:30
Category: Challenge
Tags: codechallenges, AWS, lambda, lambda function, guest, automation, microservices
Slug: codechallenge36
Authors: Michael Herman
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! We are delighted to have Michael Herman ([Real Python](https://realpython.com)) back to deliver this week's challenge. Prepare to learn some useful new skills and above all have fun!
cover: images/featured/pb-challenge.png

> Life is about facing new challenges - Kostya Tszyu

Hi Pythonistas, a new week, a new 'bite' of Python coding! We are delighted to have Michael Herman ([Real Python](https://realpython.com)) back to deliver this week's challenge. Prepare to learn some useful new skills and above all have fun!

Enter Michael.

## AWS Lambda

Amazon Web Services (AWS) Lambda is an on-demand compute service that allows you to run code in response to events or HTTP requests. In other words, you can run scripts and apps without having to provision or manage servers in an infinitely-scalable environment where you pay only for usage.

As of writing, Lambda supports code written in JavaScript (Node.js), Python, Java, and C#.

## The challenge

Create an AWS Lambda function that is triggered by an event and then performs an action.

For example:

| Event                        | Action                   |
|------------------------------|--------------------------|
| Image added to S3            | Image is processed       |
| HTTP Request via API Gateway | HTTP Response            |
| Log file added to Cloudwatch | Analyze the log          |
| Scheduled event              | Backing up files         |
| Scheduled event              | Synchronization of files |

For more, check out the  [Examples of How to Use AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/use-cases.html) guide.

## Resources

* [Getting Started with AWS Lambda ](http://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
* [How to Create Your First Python 3.6 AWS Lambda Function](https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html)
* [AWS Lambda - Full Stack Python](https://www.fullstackpython.com/aws-lambda.html)
* [Build a Python Microservice with Amazon Web Services Lambda & API Gateway](http://www.giantflyingsaucer.com/blog/?p=5730)
* [Introduction to AWS Lambda with Python](https://www.slideshare.net/adaplo/introduction-to-aws-lambda-with-python)

## Get credit!

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our start-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

---

Keep Calm and Code in Python!

-- [Michael](pages/guests.html#michaelherman) 

# HeavyWater Machine Learning Problem

### Purpose

The purpose of this problem is to evaluate your abilities in several dimensions at once.

  1. Do you understand the principles of ML/AI/data science/<insert fancy other term here>
  1. Can you build something that works
  1. Do you have a grasp of the tool chain from code on your local to code in production
  1. Can you explain your design and thinking process
  1. Are you excited by learning and challenges


### Problem Statement

We process documents related to mortgages, aka everything that happens to originate a mortgage that you don't see as a borrower. Often times the only access to a document we have is a scan of a fax of a print out of the document. Our system is able to read and comprehend that document, turning a PDF into structured business content that our customers can act on.

This dataset represents the output of the OCR stage of our data pipeline. Since these documents are sensitive financial documents we have not provided you with the raw text that was extracted. Instead we have had to obscure the data. Each word in the source is mapped to one unique value in the output. If the word appears in multiple documents then that value will appear multiple times. The word order for the dataset comes directly from our OCR layer, so it should be _roughly_ in order.

Here is a sample line:

```
CANCELLATION NOTICE,641356219cbc f95d0bea231b ... [lots more words] ... 52102c70348d b32153b8b30c
```

The first field is the document label. Everything after the comma is a space delimited set of word values.

The dataset is included as part of this repo.

### Your Mission

Should you choose to accept it ...

Train a document classification model. Deploy your model to a public cloud platform (AWS/Google/Azure/Heroku) as a webservice, send us an email with the URL to you github repo, the URL of your publicly deployed service so we can submit test cases and a recorded screen cast demo of your solution's UI, its code and deployment steps. Also, we use AWS so we are partial to you using that ... just saying.


### Measurement Criteria

We will measure your solution on the following criteria:

  1. Does your webservice work?
  1. Is your hosted model as accurate as ours? Better? (think confusion matrix)
  1. Your code, is it understandable, readable and/or deployable?
  1. Do you use industry best practices in training/testing/deploying?
  1. Do you use modern packages/tools in your code and deployment pipeline like [this](https://stelligent.com/2016/02/08/aws-lambda-functions-aws-codepipeline-cloudformation/)?
  1. The effectiveness of your demo, did you frame the problem and your approach to a solution, did you explain your thinking and any remaining gaps, etc?
  1. Are we able to run your testcases against your webservice? Can we run them against our webservice?


### A few more details

Webservice spec:

- RESTful API
- Respect content-type header (application/json and text/html minimum other bonus)
- Discoverable from root path
- URL encoded GET parameter "words" returns predicted document type (confidence is a bonus) in field "prediction" and "confidence"
- HTML pages should be readable by a human and allow for action, aka input field and submit buttons etc.
- Even a broken clock is right twice a day. A working webservice is a good first goal. It could return the highest likelihood doc class.

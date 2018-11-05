# anchor-aid [![Build Status](https://travis-ci.com/scottx611x/anchor-aid.svg?token=EkzyvwdZ2jcY78ErmS88&branch=master)](https://travis-ci.com/scottx611x/anchor-aid) [![codecov](https://codecov.io/gh/scottx611x/anchor-aid/branch/master/graph/badge.svg?token=yMq2cuLWGH)](https://codecov.io/gh/scottx611x/anchor-aid)

# What???
Anchor-aid renders any "iframe-able" webpage and proceeds to scroll into view and highlight some specific text that you want to share with someone. You are then provided with a persisting url that you can share with others, who can then be easily led to your text of interest.

# Why???
I thought it would be cool...? But mainly to be able to point to specific text in a webpage that doesn't have good/useful [bookmark links](https://www.w3schools.com/tags/att_a_name.asp)

# How???
The anchor aid interface is a serverless Flask app deployed with the help of [Zappa](). Incoming requests (url and text to search for) for new pages are POSTed and stored as JSON in an S3 bucket under a unique key. This key can then be used to construct a url like so: `https://www.anchor-aid.com/<key>` which will re-render the url/search term as it was done prior. 

[Current dev site](https://lc00m8pxxf.execute-api.us-east-1.amazonaws.com/dev/3898bdab-407d-468e-8f71-2510e41691e3)

![nov-03-2018 21-52-59](https://user-images.githubusercontent.com/5629547/47959126-dd040100-dfb2-11e8-9c4c-e2cc6da8b8dd.gif)


# TODOS:
- [x] terraform code to create s3 bucket~~~, and [custom IAM Roles for the lambda to be used by Zappa](https://github.com/Miserlou/Zappa#using-custom-aws-iam-roles-and-policies)~~~
- [x] Implement Zappa portion of code and utilize the role from previous step
- [x] Tests
- [ ] S3 bucket backups
- [ ] Google analytics
- [ ] Js minification
- [ ] REACT?
- [x] Implement form for users to submit site + search query
- [x] Redirect user after successful POST to renderd site w/ highlight
~~~- [ ] return the url of the site + hash key of s3 to user~~~
- [ ] setup travis to:
  - [x] run tests
  - [x] deploy on master builds
  - [ ] deploy on develop builds
- [ ] Donation buttons?
- [ ] App diagram?
- [ ] Make iframe links actually usable
- [ ] Make things pretty

# anchor-aid [![Build Status](https://travis-ci.com/scottx611x/anchor-aid.svg?token=EkzyvwdZ2jcY78ErmS88&branch=master)](https://travis-ci.com/scottx611x/anchor-aid) [![codecov](https://codecov.io/gh/scottx611x/anchor-aid/branch/master/graph/badge.svg?token=yMq2cuLWGH)](https://codecov.io/gh/scottx611x/anchor-aid)

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

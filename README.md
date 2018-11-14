# anchor-aid [![Build Status](https://travis-ci.com/scottx611x/anchor-aid.svg?token=EkzyvwdZ2jcY78ErmS88&branch=master)](https://travis-ci.com/scottx611x/anchor-aid) [![codecov](https://codecov.io/gh/scottx611x/anchor-aid/branch/master/graph/badge.svg?token=yMq2cuLWGH)](https://codecov.io/gh/scottx611x/anchor-aid)

### What?
Anchor-Aid renders any "iframe-able" webpage and proceeds to scroll into view and highlight some specific text that you want to share with someone. You are then provided with a persisting url that you can share with others, who can then be easily led to your text of interest.

### Why?
I thought it would be cool..., but mainly to be able to point to specific text in a webpage that doesn't have good/useful [bookmark links](https://www.w3schools.com/tags/att_a_name.asp). Sometimes its nice to be able to direct someone to a portion of some installation instructions or a point in the middle of an article .etc.

### How?
The anchor aid interface is a serverless Flask app deployed with the aid of [Zappa](https://github.com/Miserlou/Zappa) having the ability to support many concurrent users. Incoming requests (url and text to search for) are POSTed and stored as JSON in an S3 bucket under a unique key. This key can then be used to construct a url like so: `https://www.anchor-aid.com/<key>` which will re-render the url/search term as it was done prior.

### Why can't I just send someone a link and tell them to ctrl+f?
You still can, but this might be easier.
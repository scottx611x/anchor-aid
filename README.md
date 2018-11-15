# [anchor-aid](https://anchor-aid.scott-ouellette.com/) [![Build Status](https://travis-ci.com/scottx611x/anchor-aid.svg?token=EkzyvwdZ2jcY78ErmS88&branch=master)](https://travis-ci.com/scottx611x/anchor-aid) [![codecov](https://codecov.io/gh/scottx611x/anchor-aid/branch/master/graph/badge.svg?token=yMq2cuLWGH)](https://codecov.io/gh/scottx611x/anchor-aid)
---

## What?
Anchor-aid renders any "iframe-able" webpage and proceeds to scroll into view and highlight some specific text that you want to share with someone. You are then provided with a persisting url that you can share with others, who can then be easily led to your text of interest.

## Why?
I thought it would be cool..., but mainly to be able to point to specific text in a webpage that doesn't have good/useful [bookmark links](https://www.w3schools.com/tags/att_a_name.asp). Sometimes its nice to be able to direct someone to a portion of some installation instructions or a point in the middle of an article .etc.

## How?
The anchor aid interface is a serverless Flask app deployed with the aid of [Zappa](https://github.com/Miserlou/Zappa) having the ability to support many concurrent users. Incoming requests (url and text to search for) are POSTed and stored as JSON in an S3 bucket under a unique key. This key can then be used to construct a url like so: `https://anchor-aid.scott-ouellette.com/<key>` which will re-render the url/search term as it was done prior.

## Why can't I just send someone a link and tell them to ctrl+f?
You still can, but this might be easier.

---

## Sites that play nicely:
- [Wikipedia](https://anchor-aid.scott-ouellette.com/d8115acc-9928-46f5-8dbd-2f48333f3919)
- [Github](https://anchor-aid.scott-ouellette.com/908ceb2f-c7f2-4147-b17a-cc09c9703310)

## Known Limitations:
- The web page to be rendered must be "iframe-able". Sites like [stackoverflow](https://stackoverflow.com) block this functionality.
- The text to search for must be within the content of a Text Node in the DOM
- The web page to be rendered can't rely on any session/login information. Sites will behave the same within this applications as they do in a Private Browsing/Incognito window.
- The more specific the text to search for is, the better. searching for "the" probably will not get you too far.
- Resources requested within the iframe context requiring `Access-Control-Allow-Origin` headers can't currently be fetched.
---

<div align="center">
  <img src="https://user-images.githubusercontent.com/5629547/48486280-10cbfb80-e7e9-11e8-8e93-01d37d7577bc.gif" width="500"/>
</div>

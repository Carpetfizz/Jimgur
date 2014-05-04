Jimgur
======

Reddit bot that direct links to imgur images

##How it works

Jimgur works like this:

* Gets submissions using [PRAW](https://praw.readthedocs.org/en/latest/)

* Checks submission URLs for `http://imgur.com/` or `http://imgur.com/a`

* Authenticates and gets data from [imgur API](https://api.imgur.com/)

* Posts comment with direct link to image on reddit

##Deploy Jimgur

Having multiple Jimgur bots are useful because each one can be responsible for one or two subreddits.

1. Create a new reddit account for the bot, call it whatever you want.

2.  Edit this line with your information:

    r.login('username','password')

2. Register your application with [imgur API](https://api.imgur.com/)

3. Get your Client ID from imgur

4. Edit this line with your Client ID:

    request.add_header("Authorization","Client-ID "+"YOUR_CLIENT_ID")

5. Open your command line and run `python jimgur.py`

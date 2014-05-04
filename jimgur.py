import praw,urllib2,json,time

r = praw.Reddit("Jimgur image linker by /u/carpetfizz")
r.login('username','password')
already_done = []
while True:
	subreddit = r.get_subreddit('gaming+pics+aww+fitness+movies+hiphopimages')
	for submission in subreddit.get_hot(limit=100):
		url = submission.url
		if submission.id not in already_done:
			links_list = []
			request = None
			if url.startswith("http://imgur.com/"):
				image_id = url.rsplit('/',1)[1]
				request = urllib2.Request("https://api.imgur.com/3/image/%s"%image_id)
				request.isimage = True
			elif url.startswith("http://imgur.com/a/"):
				album_id = url.rsplit('/',1)[1]
				request = urllib2.Request("https://api.imgur.com/3/album/%s/images"%album_id)
				request.isimage = False
			already_done.append(submission.id)
			if request:
				#Register as an imgur app here: https://api.imgur.com/
				request.add_header("Authorization","Client-ID "+"YOUR_CLIENT_ID")
				try:
					response = json.loads(urllib2.urlopen(request).read())
					if request.isimage:
						links_list.append(response[u'data'][u'link'])
					else:
						for image in response[u'data'][u'images']:
							links_list.append(image[u'link'])
				except urllib2.HTTPError:
					continue
			if len(links_list) > 0:
				post_body=""
				for link in links_list:
					post_body+=link+"\n\n"
				try:
					submission.add_comment("#**Direct Link to Image(s)**\n\n%s\n\n*****\n\n[What's this?](http://www.reddit.com/r/jimgur/wiki/index)"%post_body)
					print("Commented: "+post_body)
				except praw.errors.RateLimitExceeded as error:
					print "Sleeping for "+str(error.sleep_time)+"s"
					time.sleep(error.sleep_time)
					continue


from twython import	Twython
twitter	=	Twython('f3eoMS4R7zRtR0IFcK8LXcIei',	'kJAAjsu3rrn5Qf4MXXpXDnpLvKzTcoaMhQZVokEnEvluVJvbRq')
for	status in twitter.search(q='"IIIT Hyderabad"')["statuses"]:
	user= status["user"]["screen_name"].encode('utf-8')
	if user != 'iiit_hyderabad':
		user = status["user"]["screen_name"].encode('utf-8')
		text = status["text"].encode('utf-8')
		print user,	":", text
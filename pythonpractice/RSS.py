import feedparser

d = feedparser.parse('http://www/reddit.com/r/python/.rss')
print (d['feed'],['title'])
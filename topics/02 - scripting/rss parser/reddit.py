import feedparser
import datetime
from time import mktime

def parse_feed(url):
    feed = feedparser.parse(url)
    an_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
    recent_posts = [entry for entry in feed.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > an_hour_ago]
    for post in recent_posts:
        print("(", post.updated, ") ", post.title, sep="")
        

    #show only items from last hour
    print("done")

if __name__ == '__main__':
    parse_feed('https://www.reddit.com/r/Python/.rss')
    
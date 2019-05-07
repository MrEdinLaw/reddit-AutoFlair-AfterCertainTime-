# Imports
import praw
from time import sleep
from datetime import datetime

# Config
reddit_client_id = "",
reddit_client_secret = "",
reddit_user_agent = "",
reddit_username = "",
reddit_password = "",

minutes_old = 90,  # In Minutes
sleep_time = 60,  # In Seconds
flair_text = "NewFlair"  # Flair text to be set
subredditName = ""  # SubredditName

# REST API connection
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent,
                     username=reddit_username,
                     password=reddit_password)

# Load More Data
while True:
    subreddit = reddit.subreddit(subredditName)
    for submission in subreddit.hot(limit=1000):
        minutes = (datetime.utcnow() - datetime.fromtimestamp(submission.created_utc)).total_seconds() / 60
        if minutes > minutes_old:
            submission.mod.flair(flair_text)
            print(submission.title)
    sleep(sleep_time)

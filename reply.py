""" reply.py
This file will reply to any post in the subreddit that contains the word "boom" in the title. """

import praw
import pdb
import re
import os
import details
import main


reddit = praw.Reddit('BoomBot v0.1')

if not os.path.isfile("replied_to.txt"):
    replied_to = []

else:
    with open("replied_to.txt", "r") as f:
        replied_to = f.read()
        replied_to = replied_to.split("\n")
        replied_to = list(filter(None, replied_to))

subreddit = reddit.subreddit('')
for submission in subreddit.new(limit=5):
    if submission.id not in replied_to and submission.created_utc > main.prevTime:
        if re.search("boom", submission.title, re.IGNORECASE):
            submission.reply("The boom counter has been reset! Days since last boom: ", main.daysSince)
            print("Bot replying to : ", submission.title)
            replied_to.append(submission.id)

with open("replied_to.txt", "w") as f:
    for post_id in replied_to:
        f.write(post_id + "\n")
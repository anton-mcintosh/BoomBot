import praw
import pdb
import re
import os
import details

reddit = praw.Reddit(client_id=details.mainUser["client_id"],
                     client_secret=details.mainUser["client_secret"],
                     username=details.mainUser["username"],
                     password=details.mainUser["password"],
                     user_agent=details.mainUser["user_agent"])

if not os.path.isfile("replied_to.txt"):
    replied_to = []

else:
    with open("replied_to.txt", "r") as f:
        replied_to = f.read()
        replied_to = replied_to.split("\n")
        replied_to = list(filter(None, replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Boom Bot says: Me too!!")
            print("Bot replying to : ", submission.title)
            replied_to.append(submission.id)

with open("replied_to.txt", "w") as f:
    for post_id in replied_to:
        f.write(post_id + "\n")
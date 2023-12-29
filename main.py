""" BoomBot v0.1 """
""" This bot will count the number of times the word "boom" is used in the Bellingham subreddit. 
It will also keep track of how many days it has been since the last boom. 
This file gathers data on past booms up until now."""

import praw
import details
from datetime import datetime


reddit = praw.Reddit('BoomBot v0.1')

subreddit = reddit.subreddit("Bellingham")
boomResults = subreddit.search("boom", time_filter="all")
boomDict = {}
firstFlag = True
firstBoom = 0
daysSince = 0
prevTime = 0
boomCount = 0

for submission in boomResults:
    boomDict[submission.title] = submission.created_utc

boomDict = sorted(boomDict.items(), key=lambda x: x[1])
firstBoom = datetime.utcfromtimestamp(boomDict[0][1]).strftime('%m-%d-%Y')
for i in boomDict:
    if "boom" in i[0].lower():
        boomCount += 1
        if firstFlag:
            prevTime = i[1]
            print("Title: ", i[0])
            firstFlag = False
        else:
            daysSince = round((i[1] - prevTime) / 86400, 2) 
            print("Title: ", i[0])
            print("Days since last boom: ", daysSince)
            print("Boom Date: ", datetime.utcfromtimestamp(i[1]).strftime('%m-%d-%Y'))
        prevTime = i[1]


print("Total booms since ", firstBoom, "is",boomCount)
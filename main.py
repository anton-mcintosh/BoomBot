import praw
import details
from datetime import datetime


reddit = praw.Reddit(client_id=details.mainUser["client_id"],
                     client_secret=details.mainUser["client_secret"],
                     username=details.mainUser["username"],
                     password=details.mainUser["password"],
                     user_agent=details.mainUser["user_agent"])

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
        prevTime = i[1]


print("Total booms since ", firstBoom, "is",boomCount)
import json
from pymongo import MongoClient
#connect to database
c = MongoClient('localhost',27017)
db = c.ddt

nodeInfo = db.tweets
table = db.table

# Parse JSON
with open('shineynewset/20170419205436_#hiring.json', 'rb') as f:
    for row in f:
        # insert into Mongo
        nodeInfo.insert_one(json.loads(row))


# JSON FILES
# 20170419205433_#hiring.json
# 20170419205436_#hiring.json
# 20170419205439_#hiring.json
# 20170419205441_#hiring.json
# 20170419205444_#hiring.json
# 20170419205446_#hiring.json

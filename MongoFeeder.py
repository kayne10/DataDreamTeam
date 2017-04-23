import os
import json
from pymongo import MongoClient
#connect to database
c = MongoClient('localhost',27017)
db = c.ddt

# change nodeInfo to db.tweets to insert Tweets
nodeInfo = db.tweets
# nodeInfo = db.coordinates
table = db.table

if os.path.exists('shineynewset'):
    # monitor this folder

# JSON FILES
datasets = [
    '20170419205433_#hiring.json',
    '20170419205436_#hiring.json',
    '20170419205439_#hiring.json',
    '20170419205441_#hiring.json',
    '20170419205444_#hiring.json',
    '20170419205446_#hiring.json',
]

# Parse JSON

for dataset in datasets:
    with open('shineynewset/' + dataset, 'rb') as f:
        for row in f:
            # insert into Mongo
            nodeInfo.insert_one(json.loads(row))

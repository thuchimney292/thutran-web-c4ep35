import pymongo
from bson.objectid import ObjectId
client= pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db= client['c4e']
db.posts.insert_one({"title":"HAHA",'author':'TT',"content":'TITLE HAHA'})


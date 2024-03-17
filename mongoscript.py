from pymongo import MongoClient
import datetime
client=MongoClient("mongodb+srv://ashishn:ash123@clust1.bqjebog.mongodb.net/")
db=client.scrapy
posts = db.test_collection
doc=post={"author":"Mike",
          "text":"my first blog post",
          "tags":["mongodb","python","pymongo"],
          "date":datetime.datetime.utcnow()}
post_id=posts.insert_one(post).inserted_id
print(post_id)
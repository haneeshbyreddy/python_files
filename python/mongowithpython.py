from pymongo import MongoClient
client=MongoClient("localhost",27017)
db=client.mydb
posts=db.posts
finding=posts.find_one({"likes":2})
print(finding)
print()
result = posts.find({"likes": {"$gt": 3}})

if result is not None:
    for person in result:
        print(person)
        print()
else:
    print("No document found with category 'title'")
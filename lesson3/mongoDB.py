import pymongo
client = pymongo.MongoClient("mongodb+srv://rabit_thu:12345678Abc@cluster0-m5xkr.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
 

# def insert(name,age):
#     db.user.insert_one({'name':name,"age":age})
# insert("a",31)
# db.user.insert_one({"name":'a','age':'18'})
# db.user.insert_one({"name":'b','age':'18'})
# db.user.insert_one({"name":'c','age':'18'})
# db.user.insert_one({'name':'a','age':'20'})
# print((db.user.find_one({'name':'a'})))
# result=db.user.update_many({"name":'a'},{"$set":{"age":30}})
# print('so phan tu da cap nhat: ',result.matched_count)
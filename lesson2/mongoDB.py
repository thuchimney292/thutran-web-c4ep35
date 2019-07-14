import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://rabit_thu:12345678Abc@cluster0-m5xkr.mongodb.net/test?retryWrites=true&w=majority")
db = client.restaurant
# db.foods.insert_one({'name':'com rang','price':'100'})
# db.foods.insert_one({'name':'ga','price':'150'})
def get_all_food():
    return list(db.foods.find())
def find_food_by_id(food_id):
    return db.foods.find_one({'_id':ObjectId(food_id)})
def insert_food(name,price):
    db.foods.insert_one({'name':name,"price":price})
def delete_food_by_id(food_id):
    db.foods.delete_one({'_id':ObjectId(food_id)})

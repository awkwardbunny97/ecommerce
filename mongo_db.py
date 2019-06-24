import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://c4e32:c4e32@cluster0-ayiyv.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.products

# db.dresswm.insert_one({'name':'product1','size':'S','color':'red','brand':'mango','price':45,'type':'dress'})
db.shirtsk.insert_one({'name':'product1','size':'S','color':'red','brand':'mango','price':45,'type':'shirt'})
db.shirtsm.insert_one({'name':'product1','size':'S','color':'red','brand':'mango','price':45,'type':'shirt'})

def get_all():
    return list(db.dresswm.find())
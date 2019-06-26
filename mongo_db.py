import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://c4e32:c4e32@cluster0-ayiyv.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.products
# db.products.insert_one({'name':'product1','size':'S','color':'red','brand':'mango','price':45,'type':'dress','product_url':'static/img/product-img/product-1.jpg'})


<<<<<<< HEAD
# Tạo database user:
us = client.users
list_account = us.users


=======
def get_all():
    return list(db.dresswm.find())

# tạo database user:
us = client.users
list_account = us.users

>>>>>>> 5bf850714ba059f0036189c36fe01e71edd3cd79
def insert_account(username: str, name: str, email: str, password: str):
    """[summary]

    Arguments:
        username {str} -- Tên tài khoản
        name {str} -- Họ và tên
        email {str} -- Địa chỉ mail
        password {str} -- Mật khẩu
    """
    list_account.insert_one({"Username": username,
                             "Name": name,
                             "Email": email,
                             "Password": password})


<<<<<<< HEAD
def get_product_by_Id(category): #products
    return list(db.shirtsk.find({'category': category}))

def get_all_account():
    return list(list_account.find())

# Tạo database category:

def get_category_by_Id(category_id):
    return db.products.find_one({"_id": ObjectId(category_id)})
=======
def get_all_account():
    return list(list_account.find())
>>>>>>> 5bf850714ba059f0036189c36fe01e71edd3cd79

#!/usr/bin/env python3

#########################################################
# This file contains basic operations for mongodb
#########################################################

# Import modules required for app
import os
import pymongo

#create a database,a collection
##########################
#In MongoDB, a database is not created until it gets content!
#MongoDB waits until you have created a collection (table)
#with at least one document (record) before it actually creates the database
#(and collection).
##########################
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb2"]
mycol = mydb["customers"]
#In MongoDB, a collection is not created until it gets content!

#Insert a document
mydoc = {"name":"John", "order":{"book":1, "pen": 2}}

x = mycol.insert_one(mydoc)
print (x)

#query object/documents in a collection
myquery = {"name":"John"}
result = mycol.find(myquery)
for y in result:
    print (y)



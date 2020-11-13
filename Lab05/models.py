#!/usr/bin/env python3

#########################################################
# This is the database processing file. (aka. Models)
# It contains the DB connections, queries and processes.
# Uses principles of Models, Views, Controllers (MVC).
#########################################################

# Import modules required for app
import os
from pymongo import MongoClient
from werkzeug.utils import secure_filename

# Set the database target to your local MongoDB instance
client = MongoClient('127.0.0.1:27017')
DB_NAME = "mongodb"  ##### Make sure this matches the name of your MongoDB database ######

# Get database connection with database name
db = client[DB_NAME]

# Retrieve all photos records from database
def get_photos():
    return db.photos.find({})

# Insert form fields into database
def insert_photo(request):
    title = request.form['title']
    comments = request.form['comments']
    filename = secure_filename(request.files['photo'].filename)
    thumbfile = filename.rsplit(".",1)[0] + "-thumb.jpg"

    db.photos.insert_one({'title':title, 'comments':comments, 'photo':filename, 'thumb':thumbfile})
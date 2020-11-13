######################################
# Title: my-api-step01.py
# Description: Guide to create own API
# Author: Jonas Werner
######################################


from flask import Flask, jsonify, request
import os
import json


app = Flask(__name__)


# Test the API by returning a text string
@app.route('/api/v1/test',methods=['GET'])
def apiTest():

    returnData  = "API return data"
    code        = 200

    return returnData, code


# Start the Flask webserver, specify it's port and IP as well as debug mode
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=int(os.getenv('PORT', '5100')))


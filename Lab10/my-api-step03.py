######################################
# Title: my-api-step03.py
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

# Read a vaule from the client API call, perform a calculation
# and return the result
@app.route('/api/v1/square',methods=['GET'])
def apiSquare():
    # We capture the arguments from the GET request
    req = request.args
    number = req['number']
    # The calculation is done
    number = int(number)**2

    returnData  = str(number)
    code        = 201

    return returnData, code


# Read a vaule from the client API call, perform multiple calculations,
# store the data in a dictionary and return the result
@app.route('/api/v1/calculations',methods=['GET'])
def apiCalculations():
    # We capture the arguments from the GET request
    req = request.args
    number = req['number']
    # The calculations are performed
    double  = int(number)*2
    square  = int(number)**2
    divided = int(number)/2

    # Create a dictionary to store the return values
    results = {}
    # Store the values
    results['double']  = double
    results['square']  = square
    results['divided'] = divided
    
    returnData  = results
    code        = 201

    return returnData, code

# Start the Flask webserver, specify it's port and IP as well as debug mode
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=int(os.getenv('PORT', '5100')))


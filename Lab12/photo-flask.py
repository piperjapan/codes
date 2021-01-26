#!/usr/bin/env python3

import ADC0832
import time
import os
from flask import Flask

app = Flask(__name__)

def init():
        ADC0832.setup()

def readval():
        res = ADC0832.getResult() - 80
        if res < 0:
                res = 0
        if res > 100:
                res = 100
        print ('res = %d' % res)
        return res

@app.route('/')
def mainmenu():
    PIval = readval()
    return """
    <html><body>
    <center><h1>BETA version of my home automation system<br/>
        <h2><u>The latest reading of the light sensor is: {0}<br>
    </center>
    </body></html>
    """.format(PIval)

if __name__ == "__main__":
        init()
        app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))

        try:
            while True:
                pass
        except KeyboardInterrupt:
            ADC0832.destroy()
            print ('Cleanup ADC and end!')
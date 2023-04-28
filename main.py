# we will use flask to create a web server
from flask import Flask, render_template, request
from parameters import *
app = Flask(__name__)

# define a landing page view


@app.route('/')
def position_mark():
    print(GPS)
    return render_template('index.html', interval=interval)

@app.route('/update')
def update():
    # update the GPS coordinates
    GPS['lat'] = request.args.get('lat')
    GPS['lon'] = request.args.get('lon')
    print(GPS)
    return 'OK'

@app.route('/gps')
def gps():
    return GPS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


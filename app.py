from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    return 'This is NOICE'

@application.route('/users')
def getUsers():
    return 'get the users'

@application.route('/poop')
def getPoop():
    return render_template('index.html')
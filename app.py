from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
application = Flask(__name__, '/static')

#################### Configure DB: ####################
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:1forall!@rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com/Bambook'
##need to initialize an engine 
##need connection
# db = SQLAlchemy(application)
engine = create_engine('mysql+pymysql://admin:1forall!@rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com/Bambook')
#################### DB Models ####################

# class People(db.Model):
#     id = db.column(db.Integer, primary_key=True)
#     name = db.column(db.String(200), nullable=False)
#     email = db.column(db.String(200), nullable=False, unique=True)

#     #create A string
#     def __repr__(self):
#         return '<Name %r>' % self.name

#################### Application Routes ####################
@application.route('/')
def index():
    #call the engine
    with engine.connect() as connection:
        res=connection.execute("SELECT email FROM users WHERE username='Eregnir'")
        emails=[]
        for row in res:
                emails.append(str(row))
        e1=str(emails[0])
    return render_template('index.html',ems=e1)


@application.route('/b')
def bitches():
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT email FROM users WHERE username='Eregnir'")
            usernames = []
            for row in result:
                usernames.append(str(row))
            return {"my data": usernames}

    except Exception as e:
        return {"error": str(e)}

@application.route('/home_2')
def home2():
    return render_template('pages/home_2.html')
    

@application.route('/books_list')
def books_list():
    return render_template('pages/books_list.html')

@application.route('/cart')
def cart():
    return render_template('pages/cart.html')

@application.route('/bookshelf')
def bookshelf():
    return render_template('pages/bookshelf.html')

@application.route('/pages')
def pages():
    return render_template('cart.html')

@application.route('/reading')
def reading():
    return render_template('reading.html')

@application.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    application.run()
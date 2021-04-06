from flask import Flask, render_template
application = Flask(__name__, '/static')

@application.route('/')
def index():
    return render_template('index.html')

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
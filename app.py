from flask import Flask, render_template
from mongo_db import get_all
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/regular-page')
def regular_page():
    return render_template('regular-page.html')

@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')

@app.route('/single-product-details')
def single_product():
    return render_template('single-product-details.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
# Products

# @app.route('/dresswm')
# def dresswm():
#     products = {
#         polo1:{
#             name: 
#         }
#     }
#     title = 'dresswm';
#     return render_template('test.html', title = title) 

@app.route('/dresswm')
def dressm():
    return render_template('test.html', data=get_all())
    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
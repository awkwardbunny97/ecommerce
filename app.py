from flask import Flask, render_template,url_for,redirect,session,request,jsonify
from mongo_db import insert_account,list_account,get_all_account,get_product_by_Id
app = Flask(__name__)
app.secret_key = "c4e"

@app.route('/')
def index():
  if 'Username' in session:
    return render_template('index.html',data=get_all_account(),username=session['Username'])
  return redirect(url_for('login'))

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

@app.route('/login', methods = ['POST'])
def get_login():
    check = False
    username = request.form.get('username')
    password = request.form.get('password')
    data = get_all_account()
    for k in data:
        if username == k['Username'] and password == k['Password']:
            check = True
            break
    if check:
        session['Username'] = username
        return redirect(url_for('index'))
    else:
        return render_template('login.html',login=check)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def get_info():
    username = request.form.get('username')
    data = get_all_account()
    users = []
    for i in data:
        users.append(i['Username'])
    if username in users:
        register = False
        return render_template('register.html',register=register)  
    else:
        password = request.form.get('password')
        name = request.form.get('name')
        email = request.form.get('email')
        insert_account(username,name,email,password)
        session['Username'] = username
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('Username')
    return redirect(url_for('index'))

# Products

# @app.route('/get_category_by_Id/{id}')
# def dressm():
#     return render_template('shop.html', data=get_all(), id = id)

# @app.route('/category/{category_id}')
# def products():
#   id = get_category_by_Id(category_id)
#   return render_template('test.html', data = id)

@app.route('/prod/<category>/<title>')
def prod(category, title):
    data = get_product_by_Id(category)
    return render_template('shop.html', product = data, title = title)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
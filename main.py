from flask import Flask, redirect, request, session
from replit import db
import os

marach = Flask(__name__, static_url_path='/static')
marach.secret_key = os.environ['secret']

@marach.route('/register', methods=['POST'])
def register1():
  if request.form['username'] not in db.keys():
    db[request.form['username']] = {'name': request.form['name'],'password': request.form['password']}
    session['username'] = request.form['username']
    return redirect ('/login')
  return 'User already Exists. Refresh to go back to home page'


@marach.route('/login', methods=['POST'])
def login1():
  if request.form['username'] in db.keys():
    if request.form['password'] == db[request.form['username']]['password']:
      return redirect ('/welcome')
    return redirect('/login')
  return redirect ('/login')


@marach.route('/logout', methods=['POST'])
def logout():
  session.clear()
  return redirect('/')


@marach.route('/')
def home():
  page = """<html>
<a href='/register'><h2>Register</h2></a>
<a href='/login'><h2>Login</h2></a>
  </html>
  """
  return page
  
@marach.route('/login')
def login():
  page = '''<form action="/login" method="post">
<p>Username <input type="text" name="username"></p>
<p>Password <input type="password" name="password"></p>
<button type="submit">Login</button>
  </form>
  '''
  return page

@marach.route('/register')
def register():
  page = '''<form action="/register" method="post">
<p>Name <input type="text" name="name"></p>
<p>Username <input type="text" name="username"></p>
<p>Password <input type="password" name="password"></p>
<button type="submit">Register</button>
  </form>
  '''
  return page

@marach.route('/welcome')
def welcome():
  page = f"""<h2>Hi {request.form['name']}. You are welcome.</h2>
  <button type='button' onClick='location.href="/logout"'>Logout</button>
  """
  return page


marach.run(host='0.0.0.0', port=81)
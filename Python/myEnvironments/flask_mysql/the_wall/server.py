from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='iVolunteerAsSecretKey'
mysql = MySQLConnector(app,'the_wall')



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	pw_hash = bcrypt.generate_password_hash(password)
	if len(first_name) < 2 or len(last_name) < 2 or len(email) < 2 or len(password) < 2:
		flash('Please enter more than one character!')
		return redirect('/')
	elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
		flash('Email address is invalid!')
		return redirect('/')
	else:
		query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) 
	 	VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
	 	# We'll then create a dictionary of data from the POST data received.
	 	data = {
	 			 'first_name': first_name, 
	 			 'last_name':  last_name,
	 			 'email': email,
	 			 'pw_hash': pw_hash
	 		   }
	 	# Run query, with dictionary values injected into the query.
	 	mysql.query_db(query, data)
	 	session['first_name'] = first_name
	 	session['email'] = email
		return redirect('/wall')

@app.route('/login', methods=['post'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	user = mysql.query_db(user_query, query_data)[0] # user will be returned in a list
	if bcrypt.check_password_hash(user['password'], password):
		session['first_name'] = user['first_name']
		session['last_name'] = user['last_name']
		session['email'] = user['email']
		session['user_id'] = user['id']
		print session
		return redirect('/wall')
	else: 
		flash('Password is incorrect!')
		return redirect('/')

@app.route('/wall', methods=['get'])
def wall():
	# messages = mysql.query_db("SELECT * FROM messages")
	return render_template('wall.html', first_name=session['first_name'])


@app.route('/message', methods=['post'])
def postMessage():
	message = request.form['message']
	userID = session['user_id']
	query = """INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"""
	 	# We'll then create a dictionary of data from the POST data received.
	data = {
 			 'message': message,
 			 'user_id': userID
 		   }
 	# Run query, with dictionary values injected into the query.
 	mysql.query_db(query, data)
	return redirect('/wall')


app.run(debug=True)


 # select users.first_name, users.last_name, users.email, users.id from users left join messages on users.id = messages.user_id order by messages.created_at DESC;

# @app.route('/friends', methods=['POST'])
# def create():
# 	# Write query as a string. Notice how we have multiple values
# 	# we want to insert into our query.
# 	query = """INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) 
# 	VALUES (:first_name, :last_name, :email_address, NOW(), NOW())"""
# 	# We'll then create a dictionary of data from the POST data received.
# 	data = {
# 			 'first_name': request.form['first_name'], 
# 			 'last_name':  request.form['last_name'],
# 			 'email_address': request.form['email_address']
# 		   }
# 	# Run query, with dictionary values injected into the query.
# 	mysql.query_db(query, data)
# 	return redirect('/')

# @app.route('/friends/<friend_id>/edit')
# def updateFriends(friend_id):
# 	query = "SELECT * FROM friends WHERE id = :specific_id"
# 	data = {'specific_id': friend_id}
# 	friends = mysql.query_db(query, data)
# 	return render_template('edit.html', one_friend=friends[0])


# @app.route('/friends/<friend_id>', methods=['post'])
# def edit(friend_id):
# 	query = """UPDATE friends 
# 			 SET first_name = :first_name, last_name = :last_name, email_address = :email_address 
# 			 WHERE id = :id"""
# 	data = {
# 			 'first_name': request.form['first_name'], 
# 			 'last_name':  request.form['last_name'],
# 			 'email_address': request.form['email_address'],
# 			 'id': friend_id
# 		   }
# 	mysql.query_db(query, data)
# 	return redirect('/friends/%s/edit' % (friend_id))


# @app.route('/friends/<friend_id>/delete', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')


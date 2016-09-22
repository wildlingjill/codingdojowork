from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key='iVolunteerAsSecretKey'
mysql = MySQLConnector(app,'the_wall')

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


app.jinja_env.globals.update(custom_strftime=custom_strftime)


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
	elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
		flash('Email address is invalid!')
		return redirect('/')
	else:
		query = """INSERT INTO users (first_name, last_name, email, password, users_created_at, updated_at) 
	 	VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
	 	# We'll then create a dictionary of data from the POST data received.
	 	data = {
	 			 'first_name': first_name, 
	 			 'last_name':  last_name,
	 			 'email': email,
	 			 'pw_hash': pw_hash
	 		   }
	 	# Run query, with dictionary values injected into the query.
	 	user = mysql.query_db(query, data)
	 	session['first_name'] = user['first_name']
		session['last_name'] = user['last_name']
		session['email'] = user['email']
		session['id'] = user['id']
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
		session['id'] = user['id']
		print session.items()
		return redirect('/wall')
	else: 
		flash('Password is incorrect!')
		return redirect('/')


@app.route('/wall', methods=['get'])
def wall():
	query = """SELECT users.first_name, users.last_name, messages.id, messages.message, messages.messages_created_at from messages 
	left join users on messages.user_id=users.id 
	order by messages.messages_created_at desc"""
 	messages = mysql.query_db(query)
 	query2 = """SELECT users.first_name, users.last_name, comments.comment, comments.comments_created_at, comments.message_id from comments 
 	left join users on comments.user_id = users.id 
 	left join messages on comments.message_id=messages.id 
 	order by comments.comments_created_at ASC"""
 	comments = mysql.query_db(query2)
 	print comments
	return render_template('wall.html', messages=messages, comments=comments)


@app.route('/message', methods=['post'])
def postMessage():
	print session.items()
	message_content = request.form['message']
	userID = session['id']
	query = """INSERT INTO messages (message, user_id, messages_created_at, messages_updated_at) VALUES (:message, :user_id, NOW(), NOW())"""
	 	# We'll then create a dictionary of data from the POST data received.
	data = {
 			 'message': message_content,
 			 'user_id': userID
 		   }
 	# Run query, with dictionary values injected into the query.
 	posted_messages = mysql.query_db(query, data)
	return redirect('/wall')


@app.route('/comment/<message_id>', methods=['post'])
def postComment(message_id):
	print session.items()
	comment = request.form['comment']
	userID = session['id']
	query = """INSERT INTO comments (comment, user_id, message_id, comments_created_at, comments_updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())"""
	 	# We'll then create a dictionary of data from the POST data received.
	data = {
 			 'comment': comment,
 			 'user_id': userID,
 			 'message_id': message_id
 		   }
 	# Run query, with dictionary values injected into the query.
 	mysql.query_db(query, data)
	return redirect('/wall')


app.run(debug=True)



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


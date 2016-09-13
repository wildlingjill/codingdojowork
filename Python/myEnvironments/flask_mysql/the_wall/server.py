from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key='keepItSecret_KeepItSafe'
mysql = MySQLConnector(app,'the_wall')



@app.route('/')
def index():
	return render_template('index.html')


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



app.run(debug=True)
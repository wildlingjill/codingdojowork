from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key='mySecretkey'
mysql = MySQLConnector(app,'email_validation')



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
	if not re.match(r"[^@]+@[^@]+\.[^@]+", request.form['email_address']):
		flash('Email address is invalid!')
		return redirect('/') 
	else:
		query = """INSERT INTO emails (email_address, created_at, updated_at) 
		VALUES (:email_address, NOW(), NOW())"""
		data = {
			 'email_address': request.form['email_address']
		   }
		mysql.query_db(query, data)
		return redirect('/success')	


@app.route('/success')
def success():
	emails = mysql.query_db("SELECT * FROM emails")
	print emails
	return render_template('success.html', all_emails=emails)



	# Write query as a string. Notice how we have multiple values
	# we want to insert into our query.
	# query = """INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) 
	# VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"""
	# # We'll then create a dictionary of data from the POST data received.
	# data = {
	# 		 'first_name': request.form['first_name'], 
	# 		 'last_name':  request.form['last_name'],
	# 		 'occupation': request.form['occupation']
	# 	   }
	# # Run query, with dictionary values injected into the query.
	# mysql.query_db(query, data)
	# return redirect('/')



# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')


app.run(debug=True)
from flask import Flask, render_template, request, redirect, session			
app = Flask(__name__)  
app.secret_key='secretKeyNumber'

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
def randomNum():
	session['random_number'] = random.randrange(0, 101)   # random number between 0-100
	return session['random_number'] 

@app.route('/') 
def index():
	randomNum()
  	return render_template('index.html') 

@app.route('/guess', methods=['POST'])
def numberMatch():
	print session['random_number']
	user_guess = int(request.form['user_guess'])
	if user_guess == session['random_number']:
		return render_template('correct.html')
	elif user_guess < session['random_number']:
		return render_template('low.html')
	else:
		return render_template('high.html')


# @app.route('/guess/high', methods=['POST'])
# def tooHigh():
	


# @app.route('/guess/low', methods=['POST'])
# def tooLow():
	


@app.route('/reset', methods=['POST'])
def resetCounter():
	return redirect('/')

app.run(debug=True) 
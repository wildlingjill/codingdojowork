from flask import Flask, render_template, request, redirect, session			
app = Flask(__name__)  
app.secret_key='fluffyunicornsparkles'
import datetime
import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
 

activities = []

def sumGold():
	session['gold'] += 0
	return session['gold']

# date.isoformat()
# classmethod datetime.now([tz])


@app.route('/') 
def index():
	sumGold()
	return render_template('index.html', activities=activities) 

@app.route('/process_money', methods=['POST'])
def processMoney():
	if request.form["building"] == "farm":
		random_number = random.randrange(10, 21)
		session['gold'] += random_number
		activities.append('Earned %d gold from the farm!' % (random_number))
		print activities[-1]
		return redirect('/')
	elif request.form["building"] == "cave":
		random_number = random.randrange(5, 11)
		session['gold'] += random_number
		activities.append('Earned %d gold from the cave!' % (random_number))
		print activities[-1]
		return redirect('/')
	elif request.form["building"] == "house":
		random_number = random.randrange(2, 6)
		session['gold'] += random_number
		activities.append('Earned %d gold from the house!' % (random_number))
		print activities[-1]
		return redirect('/')
	else:
		random_number = random.randrange(-50, 51)
		session['gold'] += random_number
		if (random_number > 0):
			activities.append('Earned %d gold from the casino!' % (random_number))
		else:
			activities.append('Entered a casino and lost %d gold...Ouch.' % (random_number * -1))
		print activities[-1]
		return redirect('/')

@app.route('/reset', methods=['POST'])
def resetGold():
	session['gold'] = 0
	activities[:] = []
	return redirect('/')

app.run(debug=True) 
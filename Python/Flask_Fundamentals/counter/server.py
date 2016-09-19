from flask import Flask, render_template, request, redirect, session			
app = Flask(__name__)  
app.secret_key='fluffyunicornsparkles'

 
def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


@app.route('/') 
def index():
	sumSessionCounter()
  	return render_template('index.html') 

@app.route('/updatebytwo', methods=['POST'])
def updateByTwo():
	sumSessionCounter()
	return redirect('/')

@app.route('/reset', methods=['POST'])
def resetCounter():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True) 
from flask import Flask, render_template, request, redirect, session, flash		
app = Flask(__name__)    
app.secret_key='mischief_managed'


@app.route('/', methods = ['GET'])          					
def index():
  	return render_template('index.html') 	

# name and comment not blank, comment no more than 120 char


@app.route('/result', methods = ['POST'])

def ninjas():
	flash_messages = False
	if len(request.form['name']) < 1:
		flash('Name cannot be empty!')
		flash_messages = True	
	if len(request.form['comment']) < 1:
		flash('Comment cannot be empty!')
		flash_messages = True 	
	if len(request.form['comment']) > 120:
		flash('Comment is too long! Must be less than 120 characters.')
		flash_messages = True	
	if flash_messages:
		return render_template('index.html') 
	else:
		name = request.form['name']
		dojo_location = request.form['dojo_location']
		favourite_language = request.form['favourite_language']
		comment = request.form['comment']
		return render_template('result.html', name=name, dojo_location=dojo_location, favourite_language=favourite_language, comment=comment) 
                 							
app.run(debug=True)    



# Import Flask to allow us to create our app.
# Global variable __name__ tells Flask whether or not we are running the file
# directly, or importing it as a module.
# The "@" symbol designates a "decorator" which attaches the following
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
# Return 'Hello World!' to the response.
# Run the app in debug mode.


from flask import Flask, render_template, request, redirect			
app = Flask(__name__)    					
@app.route('/', methods = ['GET','POST'])          					
def index():
  	if request.method == 'POST':
		return redirect('/result') 

  	return render_template('index.html') 

@app.route('/result', methods = ['POST'])

def ninjas():
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


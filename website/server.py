from flask import Flask, render_template
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://cspickmymeals-default-rtdb.firebaseio.com/', None)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def index():
	return render_template('index.html')

@app.route("/results")  # this sets the route to this page
def results():
    result = firebase.get('/restaurants', None)
    return str(result)


if __name__ == "__main__":
    app.run()
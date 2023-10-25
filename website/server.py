from flask import Flask, render_template
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication()

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def index():
	return render_template('index.html')

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run()
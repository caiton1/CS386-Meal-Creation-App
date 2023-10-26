from flask import Flask, render_template, request, redirect, url_for, session
from firebase import firebase
from flask_session import Session


firebaseConfig={
     "apiKey": "AIzaSyA73NPIvm3n5aDntTnMe97SLsZOaJ9tUbU",
     "databaseURL": "https://cspickmymeals-default-rtdb.firebaseio.com",
     "authDomain": "cspickmymeals.firebaseapp.com",
     "projectId": "cspickmymeals",
     "storageBucket": "cspickmymeals.appspot.com",
     "messagingSenderId": "906324121880",
     "appId": "1:906324121880:web:982c7aebf232653692266d",
     "measurementId": "G-P805WYYVH1"
}

# TODO: impliment cryptography if adding passwords ALSO look into flask_login

app = Flask(__name__)

SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

database = firebase.FirebaseApplication(firebaseConfig['databaseURL'], None)


# TODO: testing session IGNORE
@app.route("/set/<value>")
def set_session(value):
     session["key"] = value
     return "<h1>Ok</h1>"


@app.route("/get/")
def get_session():
     stored_session = session.get("key", "No session was set")
     return f"<h3>{stored_session}</h3>"
# end testing session


# Defining the home page of our site
@app.route("/")  # this sets the route to this page d
def index():
	return render_template('index.html')


# need to add and/or read users from database and store session accross pages
# impliment passwords and cryptogrophy later
# TODO: create a signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
     return "<h1>signup page is a work in progress</h1>"

# TODO: create a login page 
@app.route("/login", methods=["GET","POST"])
def login():
     return "<h1>login page is a work in progress</h1>"

# TODO: create logout page, look into ending session
@app.route("/logout")
def logout():
     return "<h1>logout page is a work in progress</h1>"

# TODO: create dashboard page 
@app.route("/dashboard")
def route():
     return "<h1>dashboard page is a work in progress</h1>"

# view list of recpies
@app.route("/recipe", methods=["GET"])
def recipe():
    # TODO: to reduce database reads and "cost", 
    # impliment sessions and store the database data
    result = database.get('/Recipes', None) 
    recipeList = {}

    for key, value in result.items():
        recipeList.update({key:{
            "href":key.replace(" ", "+"),
            "caption":key
    }})
          
    return render_template('recipe.html', recipes=recipeList)


# search page, need to fix and impliment error handling.
# (will fall on its face if it is not exact match)
# TODO: may need to rethink implimentation, this is not a good approach
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        searchRecipe = request.form["nm"]
        searchRecipe = searchRecipe.replace(" ", "+")
        return redirect(f"/recipe/{searchRecipe}")
    else:      
        return render_template("search.html")
    

# view recipe
@app.route("/recipe/<selection>")
def viewRecipe(selection):
     selection = selection.replace("+", " ")
     result = database.get('/Recipes', None)
     data = result[selection]
     return render_template("selection.html", 
                            dataInput=data, recipeName=selection)

if __name__ == "__main__":
    app.run()
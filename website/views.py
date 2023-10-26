from flask import Flask, render_template, request, redirect, url_for, session
import requests
import pyrebase
from flask_session import Session

# TODO: move to config file
config = {
     "apiKey": "AIzaSyA73NPIvm3n5aDntTnMe97SLsZOaJ9tUbU",
     "authDomain": "cspickmymeals.firebaseapp.com",
     "databaseURL": "https://cspickmymeals-default-rtdb.firebaseio.com",
     "projectId": "cspickmymeals",
     "storageBucket": "cspickmymeals.appspot.com",
     "messagingSenderId": "906324121880",
     "appId": "1:906324121880:web:9ff3c7693d9b124192266d",
     "measurementId": "G-DVZP5XDVHR"
}


# TODO: impliment cryptography if adding passwords ALSO look into flask_login

app = Flask(__name__)

SESSION_TYPE = "filesystem" # TODO: put in config file
app.config.from_object(__name__)
Session(app) # user sessions stored server side for now

# connect app to firebase
firebase = pyrebase.initialize_app(config)

# auth reference
auth = firebase.auth()
# database refernce
db = firebase.database()

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


# need to add and/or read users from db and store session accross pages
# impliment passwords and cryptogrophy later
# TODO: create a signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
     if request.method == "POST":
          email = request.form["email"]
          password = request.form["pass"]
          try:
               user_token=auth.create_user_with_email_and_password(email, password)
               data = {user_token["localId"]:{
                    "favorites":"",
                    "meal_plan":""
               }}
               db.child("user").push(data)
               return redirect(url_for("login"))
          except:
               error = "Invalid email or email already exists! Please also make sure password is atleast 6 characters long."
               return render_template('signup.html', msg=error)
     else:
          return render_template('signup.html', msg="")
     


# TODO: create a login page 
@app.route("/login", methods=["GET","POST"])
def login():
     if request.method == "POST":
          email = request.form["email"]
          password = request.form["pass"]
          try:
               user_token=auth.sign_in_with_email_and_password(email, password)
               session["token"] = user_token["localId"]
               return redirect(url_for("dashboard"))
          except:
               error = "invalid email or password"
               return render_template('login.html', msg=error)
     else:
          return render_template('login.html', msg="")

# TODO: create logout page, look into ending session
@app.route("/logout")
def logout():
     session.remove()
     return "<h1>logout page is a work in progress</h1>"

# TODO: create dashboard page 
@app.route("/dashboard")
def dashboard():
     token = session.get("token", "session error")
     print(token)
     return "<h1>dashboard page is a work in progress</h1>"

# view list of recpies
@app.route("/recipe", methods=["GET"])
def recipe():
    # TODO: to reduce db reads and "cost", 
    # impliment sessions and store the db data
    recipe_list = db.child("Recipes").get()
    title_list = {}

    for recipe in recipe_list:
        title_list.update({recipe.key():{
             "href":recipe.key().replace(" ", "+"),
             "caption":recipe.key()
        }})
          
    return render_template('recipe.html', recipes=title_list)


# search page, need to fix and impliment error handling.
# (will fall on its face if it is not exact match)
# TODO: may need to rethink implimentation, this is not a good approach
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        search_recipe = request.form["nm"]
        search_recipe = search_recipe.replace(" ", "+")
        return redirect(f"/recipe/{search_recipe}")
    else:      
        return render_template("search.html")
    

# view recipe
@app.route("/recipe/<selection>")
def viewRecipe(selection):
     selection = selection.replace("+", " ")
     data = db.child("Recipes").child(selection).get()
     return render_template("selection.html", 
                            dataInput=data.val(), recipeName=selection)

if __name__ == "__main__":
    app.run()
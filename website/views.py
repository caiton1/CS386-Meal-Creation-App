from flask import Flask, render_template, request, redirect, url_for, session
from firebase import firebase
from flask_session import Session
# TODO: impliment cryptography if adding passwords

app = Flask(__name__)

SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

firebase = firebase.FirebaseApplication\
    ('https://cspickmymeals-default-rtdb.firebaseio.com/', None)

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


# need to add and/or read users from database and session store
# impliment passwords and cryptogrophy later
# TODO: create a signup page

# TODO: create a login page 

# TODO: create logout page

# TODO: create dashboard page

# view list of recpies
@app.route("/recipe", methods=["GET"])
def recipe():
    # TODO: to reduce database reads and "cost", 
    # impliment sessions and store the database data
    result = firebase.get('/Recipes', None) 
    recipeList = {}

    for key, value in result.items():
        recipeList.update({key:{
            "href":key.replace(" ", "+"),
            "caption":key
    }})
          
    return render_template('recipe.html', recipes=recipeList)


# search page, need to fix and impliment error handling.
# (will fall on its face if it is not exact match)
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
     result = firebase.get('/Recipes', None)
     data = result[selection]
     return render_template("selection.html", 
                            dataInput=data, recipeName=selection)

if __name__ == "__main__":
    app.run()
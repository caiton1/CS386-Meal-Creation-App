from flask import Flask, render_template, request, redirect, flash, url_for, session
import pyrebase
from flask_session import Session
import functions.config as config
import functions.user as user
from functions.favorite import add_favorite, remove_favorite, is_favorited
from functions.meal_plan import is_planned, add_planned, remove_planned
from functions.preferenceFilter import filter_recipes
from functions.calorieFilter import get_caloric_data, sort_calories
import functions.calc_total_cost as calc_cost
from functions.sort_by_cost import low_to_high
import functions.allergy as allergy
import os
from functions.swipe import random_recipe

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)  # user sessions stored server side for now

# connect app to firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# auth reference
auth = firebase.auth()
# database reference
db = firebase.database()
# initialize user class
user = user.UserData()


@app.route('/') 
def index():
    """Main page, should have a check that

    Dynamic content variables:
    tokenTest -- the session ID (also stored on the database), used in JS for alerting user if necessary
    """
    if session.get('token') is None:
        session['token'] = ''
    return render_template('index.html', tokenTest='')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup process that will check if the user is already logged in and ensure proper input to database

    Dynamic content variables:
    msg -- feedback to the user that will be shown below the signup dialog "box"
    tokenTest -- user session ID that gets checked and alerts the user they are already signed in
    """
    if session['token'] == '':
        if request.method == 'POST':
            user.login_info(request.form)
            try:
                user.create_user(auth, db)
                return redirect(url_for('login'))
            except:
                error = '*Invalid email or email already exists! ' \
                        'Please also make sure password is at least 6 characters long.'

                return render_template('signup.html', msg=error)
        else:
            return render_template('signup.html', msg='')
    else:
        return render_template('index.html', tokentTest=session['token'])
          

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login process that also checks if the user is already logged in

    Dynamic content variables:
    msg -- feedback to the user that will be shown below the signup dialog "box"
    tokenTest -- user session ID that gets checked and alerts the user they are already signed in
    """
    if session['token'] == '':
        if request.method == 'POST':
            user.login_info(request.form)
            try:
                user.login(auth)
                session['token'] = user.user_token['localId']
                return redirect(url_for('dashboard'))
            except:
                error = '*invalid email or password'
                return render_template('login.html', msg=error)
        else:
            return render_template('login.html', msg='')
    else:
        return render_template('index.html', tokenTest=session['token'])


@app.route('/logout')
def logout():
    """Logout process, empty and reset session and user class variables"""
    session['token'] = ''
    session['alert'] = ''
    user.logoff()
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    """Dashboard page, contains favorite meals and planned meals for registered users

    Dynamic content variables:
    fav_data -- a dictionary containing the link and name to be displayed
    plan_data -- a dictionary containing the link and name to be displayed
    """
    token = session.get('token', 'session error')
    if token == '':
        return redirect(url_for('login'))
    else:
        fav_links = user.user_recipies_to_links(db, token, 'favorites')
        plan_links = user.user_recipies_to_links(db, token, 'meal_plan')

        return render_template('dashboard.html', fav_data=fav_links, plan_data=plan_links)



@app.route('/recipe', methods=['POST', 'GET'])
def recipe():
    """The recipe page will be the core component of the website.
    list recipes and give the user the ability to search and filter

    Dynamic content variables:
    recipes -- dictionary (of dictionaries) of recipies to be displayed
    """
    if request.method == 'POST':
        recipes = user.get_recipes(db)
        filtered_list = []
        preference = request.form.get('preference')
        selection = request.form.get('selection')
        allergies = str(request.form.get('allergies'))
        print(allergies)
        
        if preference != '':
            filter_recipes(recipes, preference, filtered_list)
            
        if selection is not None: 
            if selection == 'calories':
                calorie_list = get_caloric_data(db)
                calorie_list = sort_calories(calorie_list)
                filtered_list = [name.get('Name') for name in calorie_list]
            elif selection == 'cost':
                cost = calc_cost.get_recipe_data(db, recipes.val())
                cost = low_to_high(cost)
                filtered_list = [name.get('Name') for name in cost]
        
        if allergies:
            print("list not empty")
            allergies = allergies.split(', ')
            allergy_list = allergy.get_recipe_data(recipes)
            allergy_list = allergy.filter_by_allergies(allergy_list, allergies)
            filtered_list = [name.get('Name') for name in allergy_list]
                
        filtered_list = user.list_to_links(filtered_list)
        return render_template('recipe.html', recipes=filtered_list)
    else:
        # If it's a GET request, render the recipe.html template without filtering
        recipe_links = user.recipe_to_links(db)
        return render_template('recipe.html', recipes=recipe_links)


# view recipe
@app.route('/recipe/<selection>', methods=['POST', 'GET'])
def view_recipe(selection):
    """The actual recipe page

    Keyword arguments:
    selection -- the link to the recipe that will get transformed into what it is put under in the database
    Dynamic content variables:
    dataInput -- the recipe data to be parsed and displayed on the page
    recipeName -- the recipe name
    favorited -- a string value used to load the favorite box as checked or not ('', 'checked')
    planned -- a string value used to load the planned box as checked or not ('', 'checked')
    """
    selection = selection.replace('+', ' ')
    check_box_fav = ''
    check_box_planned = ''
    # get recipies
    recipe_data = user.get_recipe_data(db, selection)

    # get user data if exists
    if session['token'] != '':
        token = session.get('token', 'session error')
        user_data = user.get_user_data(db)
        # check favorite or not
        check_box_fav, favorites = is_favorited(user_data, token, selection)
        check_box_planned, planned = is_planned(user_data, token, selection)
     
    # user clicks submit button
    if request.method == 'POST':
        if session['token'] != '':
            # check if favorite
            if request.form.get('favorite'):
                add_favorite(db, token, favorites, selection)
            else:
                remove_favorite(db, token, favorites, selection)

            #  check if planned
            if request.form.get('plan'):
                add_planned(db, token, planned, selection)
            else:
                remove_planned(db, token, planned, selection)
                    
            return redirect(url_for('view_recipe', selection=selection))
        else:
            return redirect(url_for('login'))
          
    else:
        return render_template('selection.html', dataInput=recipe_data.val(), recipeName=selection,
                               favorited=check_box_fav, planned=check_box_planned)



@app.route('/report', methods =["GET", "POST"])
def report():
    if request.method == "POST":
       subject = request.form.get("subject")
       body = request.form.get("body") 

       file = open("issue.txt","w+")
       file.write(subject + "\n" + body)
       file.close()

       os.system('gcc -Wall emailSend.c -o emailOut')
       os.system('emailOut.exe')
    return render_template('report.html')

  
@app.route('/swipe',  methods=['POST', 'GET'])
def swipe():
    """ The swipe feature page, here a user will like or dislike a recipe based on quick info and adds it to planned

    Keyword arguments:
    data -- the recipe data (dict) returned from the random_recipe function
    """
    token = session.get('token', 'session error')
    if token == '':
        return redirect(url_for('login'))
    else:
        recipe_data = user.get_recipes(db).val()
        if request.method == 'POST':
            user_data = user.get_user_data(db)
            recipe_name = request.form.get('recipe_name')
            print(recipe_name)  # debug
            # check planned or not
            check_box_planned, planned = is_planned(user_data, token, recipe_name)
            if request.form.get('submit_button'):
                # if not already planned, add to plan
                add_planned(db, token, planned, recipe_name)
            else:
                # if already planned, remove
                remove_planned(db, token, planned, recipe_name) # causes issue, deletes key all together in DB
            # generate new recipe through GET
            return redirect(url_for('swipe'))

        else:
            random_data = random_recipe(recipe_data)
            return render_template('swipe.html', data=random_data)


def start_app():
    app.run()


if __name__ == '__main__':
    start_app()

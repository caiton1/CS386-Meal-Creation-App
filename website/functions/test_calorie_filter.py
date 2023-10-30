import os
import pyrebase
import calorieFilter

# Retrieve Firebase configuration from environment variable
firebase_api_key = os.environ.get('FIREBASEKEY')

# Firebase configuration
firebase_config = {
    "apiKey": firebase_api_key,
    "authDomain": "cspickmymeals.firebaseapp.com",
    "databaseURL": "https://cspickmymeals-default-rtdb.firebaseio.com",
    "projectId": "cspickmymeals",
    "storageBucket": "cspickmymeals.appspot.com",
    "messagingSenderId": "906324121880",
    "appId": "1:906324121880:web:9ff3c7693d9b124192266d",
    "measurementId": "G-DVZP5XDVHR"
}

firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()


def test_get_recipe_data():
    recipes_data = db.child("Recipes").get().val()
    recipes = []
    for recipe_name, recipe_details in recipes_data.items():
        # Extracting "Calories per serving" from "Serving Size"
        calories_per_serving = recipe_details.get('Serving Size', {}).get('Calories per serving', 0)
        # Appending the complete recipe details to the list
        recipes.append({
            'Name': recipe_name,
            'Calories per serving': calories_per_serving
        })
    
    assert recipes == calorieFilter.get_caloric_data()


def test_sort_calories():
    calorie_data = calorieFilter.get_caloric_data()
    sorted_recipes = calorieFilter.sort_calories(calorie_data)

    calories_list = []

    for recipe in sorted_recipes:
        calories_list.append(recipe['Calories per serving'])

    assert calories_list == [689, 537, 440, 365, 350, 350, 284, 201, 196, 156]
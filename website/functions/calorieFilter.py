import os
import pyrebase

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

# Function to get recipe data from Firebase
def get_recipe_data():
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
    return recipes

# Get recipe data from Firebase
recipes = get_recipe_data()

# Sort recipes by "Calories per serving" from highest to lowest
sorted_recipes = sorted(recipes, key=lambda x: x['Calories per serving'], reverse=True)

# Print recipe names and "Calories per serving" in descending order
for recipe in sorted_recipes:
    recipe_name = recipe['Name']
    calories_per_serving = recipe['Calories per serving']
    print(f"Recipe Name: {recipe_name}")
    print(f"Calories per serving: {calories_per_serving}")
    print("===")  # Separator between recipes

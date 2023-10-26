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
        # Extracting ingredients as a dictionary
        ingredients = recipe_details.get('Ingredients', {})
        # Appending the complete recipe details to the list
        recipes.append({
            'Name': recipe_name,
            'Description': recipe_details.get('Description', []),
            'Directions': recipe_details.get('Directions', []),
            'Ingredients': ingredients,
            'Rating': recipe_details.get('Rating', 0),
            'Serving Size': recipe_details.get('Serving Size', {})
        })
    return recipes

# Function to calculate total cost from ingredients
def calculate_total_cost(ingredients):
    total_cost = 0
    for cost in ingredients.values():
        try:
            total_cost += float(cost.split('$')[1])
        except (ValueError, IndexError):
            print(f"Error: Invalid cost format '{cost}'")
    return total_cost

# Get recipe data from Firebase
recipes = get_recipe_data()

# Sort recipes by total cost from lowest to highest
sorted_recipes = sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']))

# Print recipe names and total costs
for recipe in sorted_recipes:
    recipe_name = recipe['Name']
    total_cost = calculate_total_cost(recipe['Ingredients'])
    print(f"Recipe Name: {recipe_name}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("===")  # Separator between recipes

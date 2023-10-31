import sys
sys.path.append('../functions')
import pyrebase
import calorieFilter
import config

firebase = pyrebase.initialize_app(config.firebaseConf)
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
    
    assert recipes == calorieFilter.get_caloric_data(db)


def test_sort_calories():
    calorie_data = calorieFilter.get_caloric_data(db)
    sorted_recipes = calorieFilter.sort_calories(calorie_data)

    calories_list = []

    for recipe in sorted_recipes:
        calories_list.append(recipe['Calories per serving'])

    assert calories_list == [689, 537, 440, 365, 350, 350, 284, 201, 196, 156]
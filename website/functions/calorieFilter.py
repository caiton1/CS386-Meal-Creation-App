# Function to get recipe data from Firebase
def get_caloric_data(db):
    recipes_data = db.child('Recipes').get().val()
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


def sort_calories(recipes):
    # Sort recipes by "Calories per serving" from highest to lowest
    return sorted(recipes, key=lambda x: x['Calories per serving'], reverse=True)


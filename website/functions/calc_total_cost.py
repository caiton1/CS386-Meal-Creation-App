'''@author: JKBrotamonte'''
# Function to get recipe data from Firebase
def get_recipe_data(db, recipe_data):
    recipes_data = dict(recipe_data)
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
        # Split the cost into quantity and price parts
        parts = cost.split(', $')
        if len(parts) == 2 and parts[1].replace('.', '', 1).isdigit():
            try:
                # Add the price to the total cost
                total_cost += float(parts[1])
            except ValueError:
                print(f"Error: Invalid cost format '{cost}'")
        else:
            print(f"Error: Invalid cost format '{cost}'")
    return total_cost
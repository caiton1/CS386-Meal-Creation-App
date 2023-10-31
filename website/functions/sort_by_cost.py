'''@author: JKBrotamonte'''
from calc_total_cost import get_recipe_data, calculate_total_cost

# Function to sort recipes by total cost from low to high
def low_to_high(recipes):
    sorted_recipes = sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']))
    return sorted_recipes

# Function to sort recipes by total cost from high to low
def high_to_low(recipes):
    sorted_recipes = sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']), reverse=True)
    return sorted_recipes

# Function to print sorted recipes
def print_sorted_recipes(recipes, order):
    print(f'{order}:')
    for recipe in recipes:
        recipe_name = recipe['Name']
        total_cost = calculate_total_cost(recipe['Ingredients'])
        print(f'Recipe Name: {recipe_name}')
        print(f'Total Cost: ${total_cost:.2f}')
        print('===')  # Separator between recipes
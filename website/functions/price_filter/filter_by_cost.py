'''@author: JKBrotamonte'''
from calc_total_cost import get_recipe_data, calculate_total_cost

# Function to filter recipes by total cost range
def filter_by_cost_range(recipes, min_cost, max_cost):
    filtered_recipes = []
    for recipe in recipes:
        total_cost = calculate_total_cost(recipe['Ingredients'])
        if min_cost <= total_cost <= max_cost:
            filtered_recipes.append(recipe)
    return filtered_recipes
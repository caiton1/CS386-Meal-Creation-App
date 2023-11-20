'''@author: JKBrotamonte'''
import sys
sys.path.append('../functions')

from calc_total_cost import get_recipe_data, calculate_total_cost
from sort_by_cost import low_to_high, high_to_low, print_sorted_recipes
from filter_by_cost import filter_by_cost_range

import config as config
import user
import pyrebase


user_data = user.UserData()
firebase = pyrebase.initialize_app(config.firebaseConf)
db = firebase.database()

recipes_data = user_data.get_recipes(db)
# Get recipe data from Firebase
recipes = get_recipe_data(db, recipes_data)

# Test calculate_total_cost function
def test_calculate_total_cost():
    sample_ingredients = {
        "Ingredient1": "1 cup, $2",
        "Ingredient2": "0.5 lb, $3.50",
        # Add more sample ingredients here
    }
    total_cost = calculate_total_cost(sample_ingredients)
    assert total_cost == 5.50, f"Expected total cost: 5.50, Actual total cost: {total_cost:.2f}"


# Test low_to_high function
def test_low_to_high():
    sorted_low_to_high = low_to_high(recipes)
    assert sorted_low_to_high == sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']))


# Test high_to_low function
def test_high_to_low():
    sorted_high_to_low = high_to_low(recipes)
    assert sorted_high_to_low == sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']), reverse=True)


# Test filter_by_cost_range function
def test_filter_by_cost_range():
    min_cost = 10
    max_cost = 17
    filtered_recipes = filter_by_cost_range(recipes, min_cost, max_cost)
    for recipe in filtered_recipes:
        total_cost = calculate_total_cost(recipe['Ingredients'])
        assert min_cost <= total_cost <= max_cost, f"Recipe '{recipe['Name']}' total cost out of range"

'''@author: JKBrotamonte'''

import os
import pyrebase
from calc_total_cost import get_recipe_data, calculate_total_cost
from sort_by_cost import low_to_high, high_to_low, print_sorted_recipes
from filter_by_cost import filter_by_cost_range

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

# Get recipe data from Firebase
recipes = get_recipe_data()

# Test calculate_total_cost function
def test_calculate_total_cost():
    sample_ingredients = {
        "Ingredient1": "1 cup, $2",
        "Ingredient2": "0.5 lb, $3.50",
        # Add more sample ingredients here
    }
    total_cost = calculate_total_cost(sample_ingredients)
    assert total_cost == 5.50, f"Expected total cost: 5.50, Actual total cost: {total_cost:.2f}"
    print("calculate_total_cost function passed successfully.")

# Test low_to_high function
def test_low_to_high():
    recipes = get_recipe_data()
    sorted_low_to_high = low_to_high(recipes)
    assert sorted_low_to_high == sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']))
    print("low_to_high function passed successfully.")

# Test high_to_low function
def test_high_to_low():
    recipes = get_recipe_data()
    sorted_high_to_low = high_to_low(recipes)
    assert sorted_high_to_low == sorted(recipes, key=lambda x: calculate_total_cost(x['Ingredients']), reverse=True)
    print("high_to_low function passed successfully.")

# Test filter_by_cost_range function
def test_filter_by_cost_range():
    recipes = get_recipe_data()
    min_cost = 10
    max_cost = 17
    filtered_recipes = filter_by_cost_range(recipes, min_cost, max_cost)
    for recipe in filtered_recipes:
        total_cost = calculate_total_cost(recipe['Ingredients'])
        assert min_cost <= total_cost <= max_cost, f"Recipe '{recipe['Name']}' total cost out of range"
    print("filter_by_cost_range function passed successfully.")

# Run the tests
def test_all_functions():
    test_calculate_total_cost()
    test_low_to_high()
    test_high_to_low()
    test_filter_by_cost_range()

test_all_functions()

# get recipe data for following
recipes = get_recipe_data()

# show print result of low to high
sorted_low_to_high = low_to_high(recipes)
print_sorted_recipes(sorted_low_to_high, "Low to High")

# show print result of high to low
sorted_high_to_low = high_to_low(recipes)
print_sorted_recipes(sorted_high_to_low, "High to Low")

# show print result of low to high with a range from 10-17
min_cost = 10
max_cost = 17
filtered_recipes = filter_by_cost_range(recipes, min_cost, max_cost)
sorted_low_to_high = low_to_high(filtered_recipes)
print_sorted_recipes(sorted_low_to_high, "Low to High within $10 - $17")
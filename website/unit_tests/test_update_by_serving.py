import sys
sys.path.append('../functions')
from update_by_serving import adjust_recipe, adjust_quantity
import pyrebase
import config as config
import user


user = user.UserData()
firebase = pyrebase.initialize_app(config.firebaseConf)
db = firebase.database()

recipe_data = user.get_recipes(db).val()

def test_adjust_quantity():
    assert adjust_quantity('0.5 cup', 2) == '1 cup'
    assert adjust_quantity('1 teaspoon', 0.5) == '1/2 teaspoon'
    assert adjust_quantity('2', 1.5) == '3'

def test_adjust_recipe():
    desired_serving_size = 6
    adjusted_recipe = adjust_recipe(recipe_data["2 Meat Meatloaf"], desired_serving_size)

    # Write assertions based on the expected output
    assert adjusted_recipe['Serving Size']['People served'] == desired_serving_size

    # Example assertions for the Ingredients
    assert adjusted_recipe['Ingredients']['Bread crumbs'] == '3/4 cup, $1.50'
    assert adjusted_recipe['Ingredients']['Carrot'] == '1 1/2 shredded, $1.35'
    assert adjusted_recipe['Ingredients']['Dijon mustard'] == "1 1/2 teaspoon, $1.95"
    assert adjusted_recipe['Ingredients']['Dried Thyme'] == "3/4 teaspoon, $2.55"
    assert adjusted_recipe['Ingredients']['Eggs'] == "3, $2.55"
    assert adjusted_recipe['Ingredients']['Garlic cloves'] == "3 minced, $1.20"
    assert adjusted_recipe['Ingredients']['Ground beef'] == "2 1/4 pound, $10.50"
    assert adjusted_recipe['Ingredients']['Ground pork'] == "3/4 pound, $2.25"
    assert adjusted_recipe['Ingredients']['Onion'] == "1 1/2 chopped finely, $1.05"
    assert adjusted_recipe['Ingredients']['Pepper'] == "3/4 teaspoon, $6.00"
    assert adjusted_recipe['Ingredients']['Salt'] == "1 1/2 teaspoon, $3.00"

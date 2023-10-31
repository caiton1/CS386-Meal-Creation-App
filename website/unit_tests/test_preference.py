import pyrebase
import sys
sys.path.append('../functions')
from preferenceFilter import filter_recipes
import config as config
import user


firebase = pyrebase.initialize_app(config.firebaseConf)
db = firebase.database()
user_data = user.UserData()
recipe_data = user_data.get_recipes(db)

def test_vegetarian_recipes():
    preference = 'vegetarian'
    filtered_list = []
    filter_recipes(recipe_data, preference, filtered_list)

    expected_data = [
        "Angel Hair with Lemon & Garlic",
        "Chocolate Chip Cookies",
        "Egg & Veggie Breakfast Burrito",
        "Potato Salad",
        "Veggie Quesadilla"]
    assert filtered_list == expected_data


def test_vegan_recipes():
    preference = "vegan"
    filtered_list = []
    filter_recipes(recipe_data, preference, filtered_list)
    if not filtered_list:
        expected_data = []
    assert filtered_list == expected_data

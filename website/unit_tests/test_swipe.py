import sys
sys.path.append('../functions')
import website.functions.swipe as swipe
import config as config
import user
import pyrebase


user = user.UserData()
firebase = pyrebase.initialize_app(config.firebaseConf)
db = firebase.database()


# test return of recipe generation for integration
def test_swipe():
    recipe_data = user.get_recipes(db).val()
    recipe_dict = dict(swipe.random_recipe(recipe_data))

    assert 'name' in recipe_dict and 'description' in recipe_dict and \
           'rating' in recipe_dict and 'serving_cost' in recipe_dict

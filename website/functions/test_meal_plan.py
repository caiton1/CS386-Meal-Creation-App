'''@author: aidenseay'''

# This tests all of the functions for meal_plan.py

# initialize the server for local tests  ---------------------------

import meal_plan
import config
import pyrebase
import user

# connect app to firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# auth reference
auth = firebase.auth()
# database refernce
db = firebase.database()
# initialize user class
user = user.UserData()

user.email = 'test@test.com'
user.password = 'asdfasdf'
user.login(auth)
token = user.user_token['localId']

# -----------------------------------------------------------------

# test add planned
def test_add_planned():
    # add a plan entry
    meal_plan.add_planned(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get planned list
    planned_list = user_data.val()[token]['meal_plan']
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    # assert
    assert planned_list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf']


# add plan when it already exists
def test_add_nothing():
    # add a plan entry
    meal_plan.add_planned(db, token, ['Chinese Beef and Broccoli', '2 Meat Meatloaf'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get plan list
    planned_list = user_data.val()[token]['meal_plan']
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    # assert
    assert planned_list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf']
    

# test remove planned
def test_remove_planned():
    # add a plan  entry
    meal_plan.remove_planned(db, token, ['Chinese Beef and Broccoli', '2 Meat Meatloaf'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get plan list
    plan_list = user_data.val()[token]['meal_plan']
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    # assert
    assert plan_list == ['Chinese Beef and Broccoli']

# test remove plan when not there
def test_remove_nothing():
    # add a plan entry
    meal_plan.remove_planned(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get plan list
    plan_list = user_data.val()[token]['meal_plan']
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    # assert
    assert plan_list == ['Chinese Beef and Broccoli']

    
# test a few random recipe names on is_planned
def test_is_planned():
    # add a plan entry
    meal_plan.add_planned(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # plan to test
    button, list = meal_plan.is_planned(user_data, token, '2 Meat Meatloaf')
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    assert (button == 'checked') and (list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf'])

# test a few random recipe names on is_not_planned
def test_not_planned():
    # add a planned entry
    meal_plan.add_planned(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # add a plan to test
    button, list = meal_plan.is_planned(user_data, token, 'Easy Bake Chicken Breast')
    # clean up
    db.child('user').child(token).child('meal_plan').remove()
    assert (button == '') and (list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf'])

'''@author: caiton1'''
import sys
sys.path.append('../functions')
import favorite
import config
import pyrebase
import user

# connect app to firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# auth reference
auth = firebase.auth()
# database reference
db = firebase.database()
# initialize user class
user = user.UserData()

user.email = 'test@test.com'
user.password = 'asdfasdf'
user.login(auth)
token = user.user_token['localId']

# functions will also ensure compatibility with database and proper read/writes

# test add favorite
def test_add_favorite():
    # add a favorite entry
    favorite.add_favorite(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get favorite list
    favorite_list = user_data.val()[token]['favorites']
    # clean up
    db.child('user').child(token).child('favorites').remove()
    # assert
    assert favorite_list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf']


# add favorite when it already exists
def test_add_nothing():
    # add a favorite entry
    favorite.add_favorite(db, token, ['Chinese Beef and Broccoli', '2 Meat Meatloaf'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get favorite list
    favorite_list = user_data.val()[token]['favorites']
    # clean up
    db.child('user').child(token).child('favorites').remove()
    # assert
    assert favorite_list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf']
    

# test remove favorite
def test_remove_favorite():
    # add a favorite entry
    favorite.remove_favorite(db, token, ['Chinese Beef and Broccoli', '2 Meat Meatloaf'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get favorite list
    favorite_list = user_data.val()[token]['favorites']
    # clean up
    db.child('user').child(token).child('favorites').remove()
    # assert
    assert favorite_list == ['Chinese Beef and Broccoli']


# test remove favorite when not there
def test_remove_nothing():
    # add a favorite entry
    favorite.remove_favorite(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # get favorite list
    favorite_list = user_data.val()[token]['favorites']
    # clean up
    db.child('user').child(token).child('favorites').remove()
    # assert
    assert favorite_list == ['Chinese Beef and Broccoli']


# test a few random recipe names on is_favorited
def test_is_favorited():
    # add a favorite entry
    favorite.add_favorite(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # favorite to test
    button, list = favorite.is_favorited(user_data, token, '2 Meat Meatloaf')
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert (button == 'checked') and (list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf'])


# test a few random recipe names on is_not_favorited
def test_not_favorited():
    # add a favorite entry
    favorite.add_favorite(db, token, ['Chinese Beef and Broccoli'], '2 Meat Meatloaf')
    # get user data from database
    user_data = db.child('user').get()
    # add a favorite to test
    button, list = favorite.is_favorited(user_data, token, 'Easy Bake Chicken Breast')
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert (button == '') and (list == ['Chinese Beef and Broccoli', '2 Meat Meatloaf'])



'''@author: caiton1'''
import favorite
import config
import pyrebase
import user
import random

# connect app to firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# auth reference
auth = firebase.auth()
# database refernce
db = firebase.database()
# initialize user class
user = user.UserData()

user.email = f'test@test.com'
user.password = 'asdfasdf'
user.login(auth)
token = user.user_token['localId']


# test favorite update functionality, ensure database match
def test_update_favorite():
    favorite.update_favorites(db, 'checked', token, ['test1'], 'test2')
    result = db.child('user').child(token).child('favorites').get().val()
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert result == ['test1', 'test2']
# test unfavorite update functionality, ensure database match
def test_update_unfavorite():
    favorite.update_favorites(db, '', token, ['test1'], 'test2')
    result = db.child('user').child(token).child('favorites').get().val()
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert result == ['test1']


# test a few random recipe names against functionn
def test_is_favorited():
    # add a favorite entry
    favorite.update_favorites(db, '', token, ['2 Meat Meatloaf','Chinese Beef and Broccoli'], 'test1')
    # get user data from database
    user_data = db.child('user').get()
    # add a favorite to test
    button, list = favorite.is_favorited(user_data, token, '2 Meat Meatloaf')
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert (button == '') and (list == ['Chinese Beef and Broccoli'])

def test_not_favorited():
    # add a favorite entry
    favorite.update_favorites(db, '', token, ['2 Meat Meatloaf','Chinese Beef and Broccoli'], 'test1')
    # get user data from database
    user_data = db.child('user').get()
    # add a favorite to test
    button, list = favorite.is_favorited(user_data, token, 'Easy Bake Chicken Breast')
    # clean up
    db.child('user').child(token).child('favorites').remove()
    assert (button == 'checked') and (list == ['2 Meat Meatloaf','Chinese Beef and Broccoli'])
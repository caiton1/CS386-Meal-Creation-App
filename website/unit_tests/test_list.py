import sys
sys.path.append('../functions')
import list
import config
import pyrebase
import user

# Connect app to Firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# Auth reference
auth = firebase.auth()
# Database reference
db = firebase.database()
# Initialize user class
user = user.UserData()

user.email = 'test@test.com'
user.password = 'asdfasdf'
user.login(auth)
token = user.user_token['localId']

# Test add to shopping list
def test_add_to_shopping_list():
    recipe_data = {
        'Ingredients': {
            'Onion': '1, unit, $1.5',
            'Tomato': '2, unit, $0.75'
        }
    }
    list.add_to_shopping_list(db, recipe_data, token)
    # Get user data from database
    user_data = db.child('user').get()
    # Get shopping list
    shopping_list_data = user_data.val()[token]['shopping_list']
    # Clean up
    db.child('user').child(token).child('shopping_list').remove()
    # Assert
    assert shopping_list_data == '[{"ingredient":"Onion","amount":1,"cost":1.5},{"ingredient":"Tomato","amount":2,"cost":1.5}]'


# Test remove from shopping list
def test_remove_from_shopping_list():
    # Add items to the shopping list
    shopping_list_data = [
        {'ingredient': 'Onion', 'amount': 1, 'cost': 1.5},
        {'ingredient': 'Tomato', 'amount': 2, 'cost': 1.5}
    ]
    db.child('user').child(token).child('shopping_list').set(shopping_list_data)
    # Remove an item from the shopping list
    list.remove_from_shopping_list(db, token, 'Onion')
    # Get user data from database
    user_data = db.child('user').get()
    # Get updated shopping list
    updated_shopping_list_data = user_data.val()[token]['shopping_list']
    # Clean up
    db.child('user').child(token).child('shopping_list').remove()
    # Assert
    assert updated_shopping_list_data == '[{"ingredient":"Tomato","amount":2,"cost":1.5}]'

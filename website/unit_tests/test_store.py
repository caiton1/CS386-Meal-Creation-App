# choose_store test file

import sys
sys.path.append('../functions')
import choose_store
import pyrebase
import config
import user

# connect app to firebase
firebase = pyrebase.initialize_app(config.firebaseConf)
# auth reference
auth = firebase.auth()
# database refernce
db = firebase.database()
# initialize user class
user = user.UserData()

def test_get_store_data():
    
    # access the database
    stores_data = user.get_stores(db)

    # get into the store name values
    stores_holder = stores_data.val()

    # retrieve the store names as a list
    stores_list = list(stores_holder['Store Names'])

    assert choose_store.get_store_data(stores_data) == stores_list


def test_get_store_name():
    test_input = 'Albertsons'

    assert choose_store.get_store_name(test_input) == 'albertsons'

def test_scan_for_store(): 

    test_store = ['Sprouts']
    
    # access the database
    stores_data = user.get_stores(db)

    # get into the store name values
    stores_holder = stores_data.val()

    # retrieve the store names as a list
    stores_list = list(stores_holder['Store Names'])

    # iterate through the list looking checking for the name
    for store in stores_list:

        if store.lower() == test_store:

            test_flag = True


    assert test_flag == choose_store.scna_for_store(stores_data, test_store)
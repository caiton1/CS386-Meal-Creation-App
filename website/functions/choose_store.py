# choose_store.py file

# get the store data from the database and turn it into a list
def get_store_data( store_data ):

    # get the store data from the database 
    stores_data = dict( store_data.val())

    # create the store name list
    stores = []

    # iterate through the store data
    for store_name, store_details in store_data.items():

        # take the store name and add it to the list
        stores.append({
            'Store name' : store_name
        })

    # return the list of the store names
    return stores

# function for getting the store name from the user
def get_store_name( user_input ):

    # change the inputed name to lowercase
    user_store = user_input.lower()

    # return the adjusted store name
    return user_store


# function to scan the database for the store name 
def scan_for_store( stores, user_store ):

    # iterate through the store section of the database
    for store in stores:

        # grab the current store in the database
        if store.lower() == user_store:

            # confirm the store is in the database by returning the original inputted store
            return user_store

    # return "Not in database"
    return "Store not in database"
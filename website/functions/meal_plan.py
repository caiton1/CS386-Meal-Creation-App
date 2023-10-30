'''@author: aidenseay'''
# The purpose of this program is to keep track of all the planned 
# recipies for issue #30

# checks to see if the meal is planned
def is_planned( user_data, token, selection ):

    box_display = ''
    plan_list = []

    # iterate through the planned list from the db
    for planned in user_data.val()[token]['meal_plan']:

        # append to list to be returned
        plan_list.append(planned)

        # check to see if it is selected
        if planned == selection:
            box_display = 'checked'
        
    # return the box display and planned list
    return [ box_display, plan_list ]


# updates the planned db when something is added
def add_planned( db, token, planned, selection ):

    # check to see if not in the planned list
    if selection not in planned:

        # append to the list
        planned.append(selection)
    db.child('user').child(token).update({"meal_plan":planned})


# updates the planned db when something is removed
def remove_planned( db, token, planned, selection ):

        # check to see if it is in the planned list
    if selection in planned:

        # remove from the list
        planned.remove(selection)
    db.child('user').child(token).update({"meal_plan":planned})
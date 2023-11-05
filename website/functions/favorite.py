'''@author: caiton1'''
# check if current recipe is favorited


def is_favorited(user_data, token, selection):
    box_display = ''
    favorite_list = []
    # check if selection is in user favorite
    for favorite in user_data.val()[token]['favorites']:
        favorite_list.append(favorite)
        if favorite == selection: 
            box_display = 'checked'  # display checked
    return [box_display, favorite_list]

    
# update database by adding favorite 
def add_favorite(db, token, favorites, selection):
    # not in favorite list AND checked
    if selection not in favorites:
        # add to list
        favorites.append(selection)
    db.child('user').child(token).update({'favorites': favorites})


# update database by removing favorite
def remove_favorite(db, token, favorites, selection):
    # in favorite list AND  not checked
    if selection in favorites:
        # remove from list
        favorites.remove(selection)
    db.child('user').child(token).update({'favorites':favorites})
        



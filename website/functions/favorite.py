'''@author: caiton1'''
# check if current recipe is favorited
def is_favorited(user_data, token, selection):
    box_display = ''
    favorite_list = []
    # check if selection is in user favorite
    for favorite in user_data.val()[token]['favorites']:
        favorite_list.append(favorite)
        if favorite == selection: 
            box_display = 'checked' # display checked
    return [box_display, favorite_list]
    
# update database when favorite button is clicked
def update_favorites(db, box_display, token, favorites,selection):
    # in favorite list AND  not checked
    if selection in favorites and box_display != 'checked':
        # remove from list
        favorites.remove(selection)
        db.child('user').child(token).update({'favorites':favorites})
    # not in favorite list AND checked
    if selection not in favorites and box_display == 'checked':
        # add to list
        favorites.append(selection)
        db.child('user').child(token).update({'favorites':favorites})
        



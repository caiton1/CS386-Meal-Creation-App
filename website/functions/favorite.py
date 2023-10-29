'''@author: caiton1'''
# check if current recipe is favorited
def is_favorited(user_data, token, selection):
    box_display = ''
    favorite_list = []
    # check if selection is in user favorite
    for favorite in user_data.val()[token]['favorites']:
        if favorite == selection: 
            box_display = 'checked' # display checked
        else: 
            # only append everything accept the match 
            # because if we click button, we dont want in favorites
            favorite_list.append(favorite)
    return [box_display, favorite_list]
    
# update database when favorite button is clicked
def update_favorites(db, box_display, token, favorites,selection):
    if box_display == 'checked':
        favorites.append(selection)
    db.child('user').child(token).update({'favorites':favorites})

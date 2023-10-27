'''@author: caiton1'''
# check if current recipe is favorited
def is_favorited(user_data, token, selection):
    button_display = 'favorite'
    favorite_list = []
    for favorite in user_data.val()[token]['favorites']:
        if favorite == selection: 
            button_display = 'unfavorite'
        else: 
            # only append everything accept the match 
            # because if we click button, we dont want in favorites
            favorite_list.append(favorite)
    return [button_display, favorite_list]
    
# update database when favorite button is clicked
def update_favorites(db, button_display, token, favorites,selection):
    if button_display == 'favorite':
        favorites.append(selection)
    db.child('user').child(token).update({'favorites':favorites})

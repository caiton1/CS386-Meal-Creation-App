################################################################################
# Rating.py
# Implemented by aidenseay
# Holds all necessary functions to rate each meal
# These functions assume
# - token (aka user id) is a string
# - ratings is a list of dictionaries
#   - ex. ratings = [{token:True}] (has one rating)
#   - True for thumbs up
#   - False for thumbs down
################################################################################

# Calculate rating from thumbs
def calculate_rating( token, ratings ):

    total_rates = len( ratings )
    good_rates = count_thumb_up( ratings )
    rating_precent = good_rates / total_rates * 100

    return rating_precent



# count thumbs up for calculation
def count_thumb_up( ratings ):

    count = 0
    rating = [list(user.values())[0] for user in ratings]

    for user in rating:
        if user == True:
            count += 1

    return count


# Get thumbs up from user
def toggle_thumb_up( token, ratings ):

    tokens = [list(user.keys())[0] for user in ratings]

    if check_thumb( token, ratings ):
        tokenIndex = tokens.index(token)
        ratings.pop(tokenIndex)
        
    else:

        if not check_thumb( token, ratings ) and token in tokens:
            tokenIndex = tokens.index(token)
            ratings.pop(tokenIndex)

        ratings.append({token:True})



# Get thumbs down from user
def toggle_thumb_down( token, ratings ):

    tokens = [list(user.keys())[0] for user in ratings]

    if not check_thumb( token, ratings ) and token in tokens:

        tokenIndex = tokens.index(token)
        ratings.pop(tokenIndex)

    else:

        if check_thumb( token, ratings ):

            tokenIndex = tokens.index(token)
            ratings.pop(tokenIndex)
            
        ratings.append({token:False})



# check thumb up position
def check_thumb( token, ratings ):

    rating = [list(user.values())[0] for user in ratings]
    tokens = [list(user.keys())[0] for user in ratings]

    for index in range(len(tokens)):

        if rating[index] and token == tokens[index]:

            # Thumbs up
            return True
    
    # Not thumbs up
    return False
# Function to get recipe data from Firebase
def get_recipe_data(recipe_data):
    recipes_data = dict(recipe_data.val())
    recipes = []

    for recipe_name, recipe_details in recipes_data.items():
        # Extracting ingredients as a list
        ingredients = list(recipe_details.get('Ingredients', {}).keys())
        #Extract the description as a list
        descriptions = recipe_details.get('Description', [])

        # Appending the needed recipe details to the list
        recipes.append({
            'Name': recipe_name,
            'Description': descriptions,
            'Ingredients': ingredients,
        })
    return recipes

# Function for getting the allergies
def input_to_allergies(user_input):
    
    # prompt the user for their allergies
    user_input = user_input.lower()

    # if there are no allergies, return the 0 value
    if user_input == '0':
        return user_input

    # turn the inputted data into a allergies list
    allergies = [allergy.strip() for allergy in user_input.split(',')]

    # return the allergies list
    return allergies

#TODO : fix
# Filtering  Allergy Function
def filter_by_allergies( recipes, allergies ):
    # if there are no allergies, return all the recipes
    if allergies == '0' or None:
        return recipes

    # create an empty list for the recipes without the allegies
    filtered_recipes = []

    # iterate through the recipes
    for recipe in recipes:
        # allergy flag for the current recipe
        has_allergy = False
        # iterate through the allergies list 
        for allergy in allergies:
            description = [desc.lower() for desc in recipe.get('Description')]
            #check if the current allergy is the the description or ingredients
            if allergy.lower() in description:
                # set the allergy flag to True
                has_allergy = True
                break
                

            ingredients = [ingredient.lower() for ingredient in recipe.get('Ingredients')]
            if allergy.lower() in ingredients:
                has_allergy = True
                break
        
        # If the current recipe doesn't have any allergies
        if not has_allergy:
            # Add recipe to the filtered list
            filtered_recipes.append(recipe)

        # return all the recipes without the allergies
    return filtered_recipes
def filter_recipes(db, preference, filtered_list):
    # Get recipes from the database
    recipes = db.child("Recipes").get()
    if recipes is not None:
        for recipe in recipes.each():
            recipe_data = recipe.val()
            description = recipe_data.get("Description")

            # Check if the preference is in the description
            if any(preference.lower() in keyword.lower() for keyword in description):
                # append to list
                filtered_list.append(recipe.key())

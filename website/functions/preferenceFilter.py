def filter_recipes(recipe_data, preference, filtered_list):
    if recipe_data is not None:
        for recipe in recipe_data.each():
            recipe_data = recipe.val()
            description = recipe_data.get('Description')

            # Check if the preference is in the description
            if any(preference.lower() in keyword.lower() for keyword in description):
                # append to list
                filtered_list.append(recipe.key())
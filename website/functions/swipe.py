import random
from .calc_total_cost import calculate_total_cost


def random_recipe(recipe_data):
    """ generates a random recipe and returns a dict of relevant item"""
    # random recipe as tuple, index 0 is the name and index 1 is the information
    recipe = random.choice(list(recipe_data.items()))

    # extract data from recipe to be used in website
    name = recipe[0]
    print(name)
    # description/tags
    description = recipe[1]['Description']
    rating = recipe[1]['Rating']
    cost = calculate_total_cost(recipe[1]['Ingredients'])
    # servings, will only be used for calculating per serving cost
    servings = recipe[1]['Serving Size'].get('People served')
    serving_cost = ''
    if servings is not None:
        serving_cost = cost/servings
        serving_cost = "{:.2f}".format(serving_cost)  # cost only relevant up to hundredth

    recipe_data = {
        'name': name,
        'description': description,
        'rating': rating,
        'serving_cost': serving_cost
    }

    return recipe_data




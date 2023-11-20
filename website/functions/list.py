from fractions import Fraction
import json
from calc_total_cost import calculate_total_cost
from update_by_serving import adjust_recipe

class FractionEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Fraction):
            return {
                "__fraction__": True,
                "numerator": o.numerator,
                "denominator": o.denominator
            }
        return super().default(o)

def create_shopping_list(recipe_data, desired_serving_size):
    shopping_list = []
    total_cost = 0

    if recipe_data:
        ingredients = recipe_data.get('Ingredients', {})
        adjusted_recipe = adjust_recipe(recipe_data, desired_serving_size)
        cost_total = adjusted_recipe.get('Total Cost', 0)

        for ingredient, ingredient_details in adjusted_recipe['Ingredients'].items():
            converted_amount = ingredient_conversion(ingredient_details)

            if converted_amount is not None:
                cost = float(ingredient_details.split(", ")[-1].split("$")[-1])
                total_cost = cost * converted_amount
                
                found = False
                for item in shopping_list:
                    if item['ingredient'] == ingredient:
                        item['amount'] += converted_amount
                        item['cost'] += total_cost
                        found = True
                        break

                if not found:
                    shopping_list.append({
                        'ingredient': ingredient,
                        'amount': converted_amount,
                        'cost': total_cost
                    })

    serialized_list = serialize_shopping_list(shopping_list)
    return serialized_list, total_cost



def serialize_shopping_list(shopping_list):
    return json.dumps(shopping_list, cls=FractionEncoder)


def add_to_shopping_list(db, recipe_data, token):
    shopping_list_ref = db.child('user').child(token).child('shopping_list')
    total_cost_ref = db.child('user').child(token).child('total_cost')

    serialized_list, total_cost = create_shopping_list(recipe_data)

    shopping_list_ref.set(serialized_list)
    total_cost_ref.set(total_cost)


def remove_from_shopping_list(db, token, selection):
    shopping_list_ref = db.child('user').child(token).child('shopping_list')

    shopping_list = shopping_list_ref.get()
    if shopping_list:
        shopping_list = shopping_list.val()

        updated_list = [item for item in shopping_list if item.get('recipe') != selection]

        shopping_list_ref.set(json.dumps(updated_list))


def ingredient_conversion(details):
    conversion = {
        'teaspoon': Fraction(1, 3),
        'clove': Fraction(1, 3),
        'tablespoon': 1,
        'ounce': 2,
        'cup': 16,
        'packet': Fraction(26, 10),
        'pound': 30
    }

    split_details = details.split(', ')
    amount_unit = split_details[0]

    # Check if there's a space - mixed fractions
    if ' ' in amount_unit:
        parts = amount_unit.split(' ')
        if len(parts) == 1:  # whole num
            amount = parts[0]
            unit = split_details[1]
        else:
            amount = ' '.join(parts[:-1])
            unit = parts[-1]

        if unit.lower() in conversion:
            if '/' in amount:
                whole, frac = amount.split(' ')
                frac_num, frac_den = frac.split('/')
                parsed_amount = int(whole) * conversion[unit.lower()] + Fraction(int(frac_num), int(frac_den)) * conversion[unit.lower()]
            else:
                parsed_amount = int(amount) * conversion[unit.lower()]
        else:
            parsed_amount = amount
    else:
        amount = amount_unit
        unit = split_details[1]
        if unit.lower() in conversion:
            parsed_amount = int(amount) * conversion[unit.lower()]
        else:
            parsed_amount = int(amount)

    return parsed_amount

    




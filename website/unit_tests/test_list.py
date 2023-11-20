from fractions import Fraction
from list import add_to_shopping_list, remove_from_shopping_list

def test_add_to_shopping_list():
    # Prepare initial shopping list data and recipe data
    shopping_list = []
    recipe_data = {
        'Ingredients': {
            'Onion': '1, unit, $1.5',
            'Tomato': '2, unit, $0.75'
        }
    }
    print("Original Shopping List:", shopping_list)

    # Call the function under test
    add_to_shopping_list(shopping_list, recipe_data)

    # Assert the updated shopping list
    expected_list = [
        {'ingredient': 'Onion', 'amount': 1, 'cost': 1.5},
        {'ingredient': 'Tomato', 'amount': 2, 'cost': 1.5}
    ]
    print("Updated Shopping List:", expected_list)

    assert shopping_list == expected_list


def test_remove_from_shopping_list():
    # Prepare initial shopping list data and recipe data
    shopping_list = [
        {'ingredient': 'Onion', 'amount': 1, 'cost': 1.5},
        {'ingredient': 'Tomato', 'amount': 2, 'cost': 1.5}
    ]
    recipe_data = {
        'Ingredients': {
            'Tomato': '2, unit, $0.75'
        }
    }
    print("Original Shopping List:", shopping_list)

    # Call the function under test
    remove_from_shopping_list(shopping_list, recipe_data)

    # Assert the updated shopping list after removal
    expected_list = [{'ingredient': 'Onion', 'amount': 1, 'cost': 1.5}]
    print("Updated Shopping List:", expected_list)
    assert shopping_list == expected_list

from preferenceFilter import filter_recipes


def test_vegetarian_recipes():
    preference = 'vegetarian'
    filtered_list = []
    filter_recipes(preference, filtered_list)

    expected_data = [
        "Angel Hair with Lemon & Garlic",
        "Chocolate Chip Cookies",
        "Egg & Veggie Breakfast Burrito",
        "Potato Salad",
        "Veggie Quesadilla"]
    assert filtered_list == expected_data


def test_vegan_recipes():
    preference = "vegan"
    filtered_list = []
    filter_recipes(preference, filtered_list)
    if not filtered_list:
        expected_data = []
    assert filtered_list == expected_data


if __name__ == "__main__":
    test_vegetarian_recipes()
    test_vegan_recipes()

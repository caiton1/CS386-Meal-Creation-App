def adjust_whole_number(amount, ratio):
    amount_parts = amount.split()

    # Check if the amount is a valid numeric value
    try:
        numeric_value = eval(amount_parts[0])
    except (SyntaxError, NameError):
        return amount  # Return the original amount if it's not a valid numeric value

    return f"{numeric_value * ratio} {amount_parts[-1]}"


def adjust_fraction(amount, ratio):
    amount_parts = amount.split()
    new_amount = eval(amount_parts[0]) + eval(amount_parts[1]) / eval(amount_parts[2])
    new_amount *= ratio
    return f"{new_amount} {amount_parts[-1]}"

def adjust_mixed_number_fraction(amount, ratio):
    amount_parts = amount.split()

    # Parse the whole number (including fractions)
    whole_number_parts = amount_parts[0].split('/')
    whole_number = int(whole_number_parts[0]) / int(whole_number_parts[1]) if len(whole_number_parts) == 2 else int(amount_parts[0])

    # Parse the fraction part
    if len(amount_parts) > 1:
        fraction_parts = amount_parts[1].split('/')
        fraction = int(fraction_parts[0]) / int(fraction_parts[1]) if len(fraction_parts) == 2 else 0
    else:
        fraction = 0

    # Calculate the mixed number
    mixed_number = whole_number + fraction

    # Handle additional fractions if available
    if len(amount_parts) > 4:
        mixed_number += eval(amount_parts[3]) / eval(amount_parts[4])

    mixed_number *= ratio

    return f"{mixed_number} {amount_parts[-1]}"

def adjust_recipe(recipe, desired_serving_size):
    adjusted_recipe = recipe.copy()
    current_serving_size = recipe["Serving Size"]
    serving_size_ratio = desired_serving_size / current_serving_size

    for ingredient, details in adjusted_recipe["Ingredients"].items():
        print(details)
        if details[0].isdigit and '/' not in details:
            adjusted_amount = adjust_whole_number(details, serving_size_ratio)
        elif '/' in details[0]:
            adjusted_amount = adjust_fraction(details, serving_size_ratio)
        else:
            adjusted_amount = adjust_mixed_number_fraction(details, serving_size_ratio)

        adjusted_recipe["Ingredients"][ingredient] = f"{adjusted_amount}, ${float(details.split(', $')[1]) * serving_size_ratio:.2f}"

    adjusted_recipe["Serving Size"] = desired_serving_size

    return adjusted_recipe

# Sample recipe data
sample_recipe = {
    "2 Meat Meatloaf": {
        "Description": [
            "Dinner",
            "American",
            "High-Protien",
            "Easy",
            "Beef",
            "Comfort"
        ],
        "Directions": [
            "Preheat oven to 350F.",
            "Soften the bread crumbs in the milk for a few minutes, then pour off the excess milk.",
            "Combine the 2 meats and mix well. Add all other ingredients and mix until thoroughly combined.",
            "Place in large loaf pan, 2 smaller loaf pans or shape into loaf shape and bake on flat baking pan.",
            "Bake for 1 hour at 350 or until browned and fully cooked inside."
        ],
        "Ingredients": {
            "Bread crumbs": "1/2 cup, $1",
            "Carrot": "1 shredded, $0.90",
            "Dijon mustard": "1 teaspoon, $1.30",
            "Dried Thyme": "1/2 teaspoon, $1.70",
            "Eggs": "2, $1.70",
            "Garlic cloves": "2 minced, $0.80",
            "Ground beef": "1 1/2 pound, $7",
            "Ground pork": "1/2 pound, $1.50",
            "Onion": "1 chopped finely, $0.70",
            "Pepper": "1/2 teaspoon, $4",
            "Salt": "1 teaspoon, $2"
        },
        "Rating": 3,
        "Serving Size": 4
    }
}

# Example usage:
desired_serving_size = 6
adjusted_recipe = adjust_recipe(sample_recipe["2 Meat Meatloaf"], desired_serving_size)
print(adjusted_recipe)
from fractions import Fraction
import copy
import logging

# Constants
CURRENCY_SYMBOL = '$'
COST_FORMAT = '{:.2f}'

# Configure logging
logging.basicConfig(level=logging.WARNING)

def float_to_mixed_number(number):
    if isinstance(number, (int, float)):
        # Split the number into the whole part and the fractional part
        whole_part = int(number)
        fractional_part = Fraction(number - whole_part).limit_denominator()

        # Check if there is a fractional part
        if fractional_part != 0:
            # Format the mixed number as a string
            if whole_part != 0:
                mixed_number = f'{whole_part} {fractional_part.numerator}/{fractional_part.denominator}'
            else:
                mixed_number = f'{fractional_part.numerator}/{fractional_part.denominator}'
            return mixed_number
        else:
            # If there is no fractional part, return only the whole part
            return str(whole_part)
    else:
        raise ValueError("Input must be a float or integer")

def adjust_whole_number(quantity, ratio):
    adjusted_value = int(float(quantity) * ratio)
    return float_to_mixed_number(adjusted_value)

def adjust_fraction(quantity, ratio):
    adjusted_value = Fraction(quantity) * ratio
    return float_to_mixed_number(adjusted_value)

def adjust_mixed_number_with_unit(quantity, ratio, unit):
    whole_part, fraction_part = quantity.split()
    whole_number = int(whole_part)
    fraction = Fraction(fraction_part)
    adjusted_value = (whole_number + fraction) * ratio
    return f"{float_to_mixed_number(adjusted_value)} {unit}"

def adjust_quantity(original_quantity, ratio):
    try:
        # Separate quantity and unit
        parts = original_quantity.split()

        if len(parts) >= 2 and '/' in parts[1]:
            # Handle mixed number case, e.g., '1 1/2 pound'
            quantity = ' '.join(parts[0:2])  # Join the first two parts (whole and fraction)
            unit = ' '.join(parts[2:]) if len(parts) > 2 else ''
            return adjust_mixed_number_with_unit(quantity, ratio, unit)
        else:
            # Handle other cases
            quantity, unit = parts[0], ' '.join(parts[1:]) if len(parts) > 1 else ''

        # Check for common quantity formats
        if '/' in quantity:
            adjusted_fraction = adjust_fraction(quantity, ratio)
            return f"{adjusted_fraction} {unit}" if unit else adjusted_fraction

        # Try to parse the quantity as a fraction
        try:
            fraction_quantity = Fraction(quantity)
            adjusted_value = fraction_quantity * ratio
            return f"{float_to_mixed_number(adjusted_value)} {unit}" if unit else float_to_mixed_number(adjusted_value)
        except ValueError:
            # If parsing as a fraction fails, use float_to_mixed_number for float cases
            adjusted_value = float(quantity) * ratio
            return f"{float_to_mixed_number(adjusted_value)} {unit}" if unit else float_to_mixed_number(adjusted_value)

    except (ValueError, IndexError) as e:
        logging.error(f"Error converting quantity: {original_quantity}. Error: {e}")
        return original_quantity

def adjust_recipe(recipe, desired_servings):
    adjusted_recipe = copy.deepcopy(recipe)

    try:
        if 'Serving Size' in adjusted_recipe:
            adjusted_recipe['Serving Size']['People served'] = desired_servings
        else:
            logging.warning("Warning: 'Serving Size' not found in recipe structure. Serving size not updated.")

        if 'Ingredients' in adjusted_recipe:
            ratio = desired_servings / recipe['Serving Size']['People served']
            for ingredient, details in adjusted_recipe['Ingredients'].items():
                quantity, cost = details.split(', ')
                adjusted_quantity = adjust_quantity(quantity, ratio)
                adjusted_cost = round(float(cost[1:]) * ratio, 2)
                adjusted_recipe['Ingredients'][ingredient] = f"{adjusted_quantity}, {CURRENCY_SYMBOL}{adjusted_cost:.2f}"

            adjusted_recipe['Total Cost'] = sum(float(details.split(', ')[1][1:]) for details in adjusted_recipe['Ingredients'].values())
        else:
            logging.warning("Warning: 'Ingredients' not found in recipe structure. Ingredient quantities and costs not updated.")

        return adjusted_recipe

    except Exception as e:
        logging.error(f"Error adjusting recipe: {e}")
        return recipe

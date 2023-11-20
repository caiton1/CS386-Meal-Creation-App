from fractions import Fraction
from list import ingredient_conversion

def test_ingredient_conversion():
    details = "1 tablespoon, $2.50"
    result = ingredient_conversion(details)
    print("\nResult for 1 tablespoon:", result)
    assert result == 1, "Incorrect conversion for tablespoon"
    
    details = "2 teaspoon, $1.20"
    result = ingredient_conversion(details)
    print("Result for 2 teaspoon:", result)
    assert result == Fraction(2, 3), "Incorrect conversion for teaspoon"
    
    details = "1 1/2 cup, $3.00"
    result = ingredient_conversion(details)
    print("Result for 1 1/2 cup:", result)
    assert result == Fraction(24, 1), "Incorrect conversion for cup"
    
    details = "3 eggs, $2.00"
    result = ingredient_conversion(details)
    print("Result for 3 eggs:", result)
    assert str(result) == '3', "Incorrect conversion for eggs"
    
    details = "1 clove, $0.50"
    result = ingredient_conversion(details)
    print("Result for 1 clove:", result)
    assert result == Fraction(1, 3), "Incorrect conversion for clove"

    # Test case for unexpected amount_unit format
    details = "1, $2.00"
    result = ingredient_conversion(details)
    print("Result for unexpected format:", result)
    assert result == 1

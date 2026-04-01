
from isort.literal import register_type
from typing import Callable, Any

# Assuming ISortPrettyPrinter is defined elsewhere or can be mocked
# from your application's context, if necessary.
# ISortPrettyPrinter = ...

def test_invalid_input():
    # Test that the function raises a TypeError when name is not a string
    try:
        register_type(123, int)  # Invalid input for name (not a string)
    except TypeError as e:
        assert str(e) == "name must be a string"
    
    # Test that the function raises a TypeError when kind is not a type
    try:
        register_type("example", "int")  # Invalid input for kind (not a type)
    except TypeError as e:
        assert str(e) == "kind must be a type"

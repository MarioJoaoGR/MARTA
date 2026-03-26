
# Module: isort.literal
from typing import Any, Callable

import pytest


class ISortPrettyPrinter:
    pass

type_mapping = {}  # Initialize type_mapping as a dictionary

def wrap(function: Callable[[Any, ISortPrettyPrinter], str]) -> Callable[[Any, ISortPrettyPrinter], str]:
    """
    Decorates a given function to be registered in a type mapping.
    
    The `wrap` function takes a single argument, `function`, which is expected to be a callable that accepts two parameters: an instance of `Any` and an instance of `ISortPrettyPrinter`. This function does not return any value directly but instead registers the provided function in a global type mapping using its name as the key.
    
    Parameters:
        function (Callable[[Any, ISortPrettyPrinter], str]): The function to be registered. It should accept two parameters: an instance of `Any` and an instance of `ISortPrettyPrinter`, and return a string representation of some kind.
    
    Returns:
        Callable[[Any, ISortPrettyPrinter], str]: The same function that was passed in, wrapped with the registration logic.
    """
    name = function.__name__  # Correctly capture the function's name
    kind = type(function)  # Determine the type of the function
    type_mapping[name] = (kind, function)  # Register the function in the global type mapping
    return function

# Test cases for wrap function
def test_wrap():
    # Define a mock function to be registered
    def my_function(obj: Any, printer: ISortPrettyPrinter) -> str:
        return "mocked result"
    
    # Call the wrap function with the mock function
    wrapped_function = wrap(my_function)
    
    # Check that the returned function is the same as the input function
    assert wrapped_function == my_function
    
    # Define some test objects and printer instances
    obj = "test object"
    printer = ISortPrettyPrinter()
    
    # Call the wrapped function with the test objects
    result = wrapped_function(obj, printer)
    
    # Check that the result of calling the wrapped function is as expected
    assert result == "mocked result"

# Run the test case
if __name__ == "__main__":
    pytest.main()

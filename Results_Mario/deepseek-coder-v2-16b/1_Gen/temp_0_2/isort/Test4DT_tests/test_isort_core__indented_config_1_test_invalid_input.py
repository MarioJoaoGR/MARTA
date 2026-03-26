
from isort.core import Config, _indented_config

def test_invalid_input():
    # Create an instance of Config (assuming it's defined in isort.core)
    initial_config = Config()
    
    # Test case for invalid input where indent is not a string
    try:
        result = _indented_config(initial_config, 123)  # Passing an integer instead of a string
        assert False, "Expected TypeError but passed."
    except TypeError as e:
        assert str(e) == "object of type 'int' has no len()", f"Unexpected error message: {str(e)}"

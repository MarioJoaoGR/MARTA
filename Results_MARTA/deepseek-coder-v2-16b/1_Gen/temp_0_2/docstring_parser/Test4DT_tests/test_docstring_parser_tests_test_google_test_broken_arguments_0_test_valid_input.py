
import pytest
from docstring_parser.tests.test_google import parse  # Assuming this is the correct module and function to use for parsing

def test_valid_input():
    """Test with valid input that should not raise ParseError."""
    docstring = """
    ```python
    def valid_function():
        '''This is a valid docstring.'''
    ```
    """
    # The parse function should be able to handle this well-formed docstring without raising a ParseError
    parsed_docstring = parse(docstring)

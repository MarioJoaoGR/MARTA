
import pytest
from docstring_parser.tests.test_google import parse

def test_error_handling():
    with pytest.raises(Exception):
        # This should raise an Exception because the docstring does not contain a proper exception description
        parse("Short description\n\nExample:\n\nRaises:")

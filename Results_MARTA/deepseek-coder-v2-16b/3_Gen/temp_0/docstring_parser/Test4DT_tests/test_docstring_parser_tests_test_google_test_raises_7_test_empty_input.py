
import pytest
from docstring_parser.tests.test_google import parse

def test_raises() -> None:
    """Test parsing raises in a Google-style docstring.

This function tests the ability to parse `raises` sections from a Google-style docstring using the `parse` function. It checks if the parsed docstring correctly identifies and stores any raised exceptions specified in the docstring.

Parameters:
    None

Returns:
    None

Examples:
    ```python
    def test_raises():
        # This will raise an AssertionError if the parsing of raises does not work as expected.
        test_raises()
    ```
"""
    docstring = parse(
        """
        Short description
        Raises:
            ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

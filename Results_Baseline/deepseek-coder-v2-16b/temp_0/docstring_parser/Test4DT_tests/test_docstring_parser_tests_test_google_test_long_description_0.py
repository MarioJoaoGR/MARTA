
import pytest
from docstring_parser import parse

# Test cases for parsing long descriptions in Google-style docstrings
@pytest.mark.parametrize(
    "source, expected_short_desc, expected_long_desc, expected_blank",
    [
        (
            """This is a summary.
            
            Args:
                param1 (int): Description of parameter 1.
                param2 (str): Description of parameter 2.
                
            Returns:
                int: The result of the operation, which could be an integer.
            """,
            "This is a summary.",
            """Args:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.""",
            True
        ),
        # Add more test cases as needed
    ]
)
def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
    """Test parsing long description."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
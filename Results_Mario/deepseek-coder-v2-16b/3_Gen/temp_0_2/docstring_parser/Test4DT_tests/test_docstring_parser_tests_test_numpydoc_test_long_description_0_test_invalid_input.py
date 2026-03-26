
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    (None, None, None, False),  # Test with invalid input type (None)
])
def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank):
    """Test parsing long description."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

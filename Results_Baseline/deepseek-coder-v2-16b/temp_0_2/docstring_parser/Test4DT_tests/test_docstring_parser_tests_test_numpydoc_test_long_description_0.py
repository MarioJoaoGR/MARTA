
import pytest
from docstring_parser import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    ("Short description\n\nLong description", "Short description", "Long description", True),
    ("""
        Short description
    
        Long description
    """, "Short description", "Long description", True),
    ("""
        Short description
    
        Long description
        Second line
    """, "Short description", "Long description\nSecond line", True),
    ("Short description\nLong description", "Short description", "Long description", False),
    ("""
        Short description
        Long description
    """, "Short description", "Long description", False),
    ("\nShort description\nLong description\n", "Short description", "Long description", False),
    ("""
        Short description
        Long description
        Second line
    """, "Short description", "Long description\nSecond line", False)
])
def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
    """Test parsing long description."""
    docstring = parse(source)
    
    if expected_blank:
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
        assert docstring.blank_after_short_description is True
    else:
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
        assert docstring.blank_after_short_description is False
    
    assert not docstring.meta

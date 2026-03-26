
import pytest
from docstring_parser.tests.test_google import GoogleParser

def test_google_parser_unknown_section() -> None:
    """Test parsing an unknown section with default GoogleParser configuration.
    """
    parser = GoogleParser()
    docstring = parser.parse(
        """
        Unknown:
            spam: a
        """
    )
    assert docstring.short_description == "Unknown:"
    assert docstring.long_description == "spam: a"
    assert len(docstring.meta) == 0

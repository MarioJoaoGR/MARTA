
import pytest
from docstring_parser.tests.test_google import GoogleParser

def test_google_parser_unknown_section() -> None:
    """Test parsing an unknown section with default GoogleParser configuration.
    
    This function initializes a `GoogleParser` object and attempts to parse a 
    docstring containing an unknown section title 'Unknown'. The parsed result is 
    then checked for correctness, ensuring that the short description matches 
    "Unknown:", the long description matches "spam: a", and there are no meta entries.
    
    Parameters:
        None.
        
    Returns:
        None.
        
    Examples:
        ```python
        test_google_parser_unknown_section()
        ```
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

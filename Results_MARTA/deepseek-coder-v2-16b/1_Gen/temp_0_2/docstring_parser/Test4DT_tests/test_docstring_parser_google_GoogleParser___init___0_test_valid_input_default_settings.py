
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_valid_input_default_settings():
    # Arrange
    parser = GoogleParser()
    
    # Act
    # No action needed as the constructor sets up default settings
    
    # Assert
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    assert parser.title_colon is True

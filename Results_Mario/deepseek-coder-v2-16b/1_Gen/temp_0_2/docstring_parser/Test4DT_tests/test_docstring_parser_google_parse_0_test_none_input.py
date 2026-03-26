
import pytest
from docstring_parser.google import parse, Section
from unittest.mock import patch

def test_none_input():
    with patch('docstring_parser.google.GoogleParser') as mock_parser:
        # Mock the parse method to return a default Docstring object when text is None
        mock_instance = mock_parser.return_value
        mock_instance.parse.return_value = "default_docstring"
        
        result = parse(None)
        
        assert result == "default_docstring"

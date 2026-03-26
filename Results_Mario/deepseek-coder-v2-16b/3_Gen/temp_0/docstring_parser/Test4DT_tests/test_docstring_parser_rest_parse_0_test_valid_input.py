
import pytest
from unittest.mock import patch, MagicMock
from docstring_parser.rest import parse, Docstring, DocstringStyle, ParseError

def test_valid_input():
    rest_docstring = "This is a brief description.\n\nAnd this is more detailed documentation."
    
    with patch('inspect.cleandoc', return_value=rest_docstring):
        parsed_docstring = parse(rest_docstring)
        
        assert parsed_docstring.short_description == "This is a brief description."
        assert parsed_docstring.long_description == "And this is more detailed documentation."
        assert isinstance(parsed_docstring, Docstring)
        assert parsed_docstring.style == DocstringStyle.REST
        
        # Add more assertions for meta information if necessary

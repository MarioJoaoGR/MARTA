
import pytest
from docstring_parser.common import DocstringExample

def test_edge_cases():
    # Create an instance of DocstringExample with edge case values
    example = DocstringExample(args=['arg1', 'arg2'], snippet='print("Hello, World!")', description='A simple example')
    
    # Assert that the properties are set correctly
    assert example.snippet == 'print("Hello, World!")'
    assert example.description == 'A simple example'


import pytest
from docstring_parser.common import DocstringExample

def test_edge_cases():
    # Test edge cases where args, snippet, and description are provided
    example = DocstringExample(args=['arg1', 'arg2'], snippet='print("Hello, World!")', description='A simple example')
    
    assert example.snippet == 'print("Hello, World!")'
    assert example.description == 'A simple example'

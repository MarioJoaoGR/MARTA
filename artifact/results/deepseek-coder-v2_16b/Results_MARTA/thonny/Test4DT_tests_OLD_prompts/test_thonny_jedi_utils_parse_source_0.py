
import pytest
from unittest.mock import patch
import parso

def parse_source(source):
    return parso.parse(source)

@patch('parso.parse')
def test_parse_simple_function(mock_parso):
    source = "def example(): return 42"
    mock_parso.return_value = "parsed_ast"
    
    ast = parse_source(source)
    
    assert ast == "parsed_ast"

@patch('parso.parse')
def test_parse_complex_code(mock_parso):
    source = """
    def main():
        x = 10
        y = 20
        return x + y
    """
    mock_parso.return_value = "parsed_ast"
    
    ast = parse_source(source)
    
    assert ast == "parsed_ast"

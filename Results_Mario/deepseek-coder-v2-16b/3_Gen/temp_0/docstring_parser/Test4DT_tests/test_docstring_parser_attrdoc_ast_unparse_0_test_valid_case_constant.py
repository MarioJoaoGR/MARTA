
import ast
from unittest.mock import patch
import pytest
from docstring_parser.attrdoc import ast_unparse  # Assuming this is the correct module path

def test_valid_case_constant():
    example_node = ast.parse("1 + 2").body[0].value  # Assuming this represents a constant expression
    
    with patch('ast.unparse', return_value='1 + 2'):
        result = ast_unparse(example_node)
        assert result == '1 + 2'

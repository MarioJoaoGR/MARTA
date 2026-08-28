
import ast
from unittest.mock import patch
from py_backwards.utils.snippet import VariablesReplacer

def test_valid_input():
    class Variable:
        def __init__(self, value):
            self.value = value
    
    variables_dict = {'x': Variable(10), 'y': Variable(20)}
    replacer = VariablesReplacer(variables_dict)

    with patch('py_backwards.utils.snippet.ast') as mock_ast:
        mock_ast.parse.return_value = ast.Module(body=[ast.ImportFrom(module='math', names=[ast.alias(name='sqrt', asname=None)])])
        node = mock_ast.parse.return_value.body[0]
        replaced_node = replacer.visit_ImportFrom(node)
        assert isinstance(replaced_node, ast.ImportFrom), "Expected an ImportFrom node"
        assert replaced_node.module == 'math', f"Expected module to be math, got {replaced_node.module}"

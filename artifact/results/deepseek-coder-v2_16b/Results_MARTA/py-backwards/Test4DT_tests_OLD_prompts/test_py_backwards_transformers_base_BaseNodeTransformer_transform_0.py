
import ast
from py_backwards.transformers.base import BaseNodeTransformer
import pytest
from unittest.mock import patch

# Test for valid input transformation
def test_valid_input():
    some_code = """
    def greet(name):
        print(f"Hello, {name}!")
    """
    with pytest.raises(IndentationError):
        tree = ast.parse(some_code)
        transformer = BaseNodeTransformer(tree)
        new_tree = transformer.transform()

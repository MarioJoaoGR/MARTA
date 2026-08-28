
import ast
import pytest
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

# Test for valid list transformation

# Test for invalid input
def test_invalid_input():
    original_list = 'invalid'
    with pytest.raises(TypeError):
        tree = ast.parse(f"[{', '.join([str(e) for e in original_list])}]")
        transformer = StarredUnpackingTransformer()
        transformed_tree = transformer.visit_Call(tree.body[0].value)
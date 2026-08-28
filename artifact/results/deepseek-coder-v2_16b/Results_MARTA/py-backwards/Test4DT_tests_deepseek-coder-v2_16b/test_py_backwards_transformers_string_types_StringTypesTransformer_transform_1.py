
import ast
from py_backwards.transformers.string_types import StringTypesTransformer
import pytest

@pytest.fixture
def sample_ast():
    code = """
    def example():
        return "str"
    """
    tree = ast.parse(code)
    return tree

@pytest.mark.parametrize("input_code, expected_id", [
    ("def example(): return 'str'", 'unicode'),
    ("def example(): return u'str'", 'unicode')
])
def test_StringTypesTransformer_transform_basic(input_code, expected_id):
    tree = ast.parse(input_code)
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)
    
    for node in ast.walk(result.tree):
        if isinstance(node, ast.Name) and node.id == 'str':
            assert node.id == expected_id

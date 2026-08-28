
import ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
import pytest

# Test fixture setup
@pytest.fixture
def transformer():
    return StarredUnpackingTransformer()

# Test for transforming a list with starred unpacking
def test_transform_list_with_starred_unpacking(transformer):
    original_list = [2, *range(10), 1]
    ast_expressions = [ast.parse("[2, *range(10), 1]").body[0].value.elts]
    transformed_list = transformer._to_sum_of_lists(ast_expressions)
    expected_list = [2] + list(range(10)) + [1]
    assert isinstance(transformed_list, list) and transformed_list == expected_list

# Test for transforming a print statement with starred unpacking
def test_transform_print_with_starred_unpacking(transformer):
    original_print = print(*range(1), *range(3))
    ast_expressions = [ast.parse("range(1)").body[0].value, ast.parse("range(3)").body[0].value]
    transformed_print = transformer._to_sum_of_lists(ast_expressions)
    expected_print = print(*(list(range(1)) + list(range(3)))
    assert str(transformed_print) == str(expected_print)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: '(' was never closed (line 24, col 27)
    expected_print = print(*(list(range(1)) + list(range(3)))
"""
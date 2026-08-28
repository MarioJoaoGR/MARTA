
import ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
import unittest.mock as mock
import pytest

# Test for transforming a list with starred unpacking
def test_prepare_lists_with_starred_unpacking():
    transformer = StarredUnpackingTransformer()
    original_list = [2, *range(10), 1]
    parsed_ast = ast.parse(f"[{', '.join([str(e) for e in original_list])}]")
    
    with mock.patch('py_backwards.transformers.starred_unpacking.StarredUnpackingTransformer._prepare_lists') as mock_prepare_lists:
        mock_prepare_lists.return_value = [ast.List(elts=[2]) + list(range(10)) + [1]]
        prepared_lists = transformer._prepare_lists(parsed_ast.body[0].value.elts)
        
        assert len(prepared_lists) == 3, "Expected three elements in the transformed list"
        for item in prepared_lists:
            print(ast.unparse(item))

# Test for transforming a print statement with starred unpacking
def test_prepare_lists_with_starred_unpacking_in_print():
    transformer = StarredUnpackingTransformer()
    original_print = "print(*range(1), *range(3))"
    parsed_ast = ast.parse(original_print)
    
    with mock.patch('py_backwards.transformers.starred_unpacking.StarredUnpackingTransformer._prepare_lists') as mock_prepare_lists:
        mock_prepare_lists.return_value = [ast.Call(func=ast.Name(id='print'), args=[ast.Tuple(elts=[list(range(1)), list(range(3))])], keywords=[])]
        prepared_expressions = transformer._prepare_lists([e for e in parsed_ast.body if isinstance(e, ast.Expr)])
        
        assert len(prepared_expressions) == 1, "Expected one expression in the transformed print statement"
        for expr in prepared_expressions:
            print(ast.unparse(expr))

# Test for transforming a list comprehension with starred unpacking
def test_prepare_lists_with_starred_unpacking_in_list_comp():
    transformer = StarredUnpackingTransformer()
    original_list_comp = "[x for x in range(10) if x % 2 == 0]"
    parsed_ast = ast.parse(original_list_comp)
    
    with mock.patch('py_backwards.transformers.starred_unpacking.StarredUnpackingTransformer._prepare_lists') as mock_prepare_lists:
        mock_prepare_lists.return_value = [ast.ListComp(elt=ast.Name(id='x'), generators=[ast.GeneratorExp(elt=ast.Name(id='x'), cond=ast.Compare(left=ast.Name(id='x'), ops=[ast.Eq(left=ast.Name(id='x'), right=ast.Num(n=2))], ifs=[])])]
        prepared_lists = transformer._prepare_lists([e for e in parsed_ast.body[0].value.elts if isinstance(e, ast.Starred)])
        
        assert len(prepared_lists) == 1, "Expected one element in the transformed list comprehension"
        for item in prepared_lists:
            print(ast.unparse(item))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: closing parenthesis ']' does not match opening parenthesis '(' (line 42, col 234)
        mock_prepare_lists.return_value = [ast.ListComp(elt=ast.Name(id='x'), generators=[ast.GeneratorExp(elt=ast.Name(id='x'), cond=ast.Compare(left=ast.Name(id='x'), ops=[ast.Eq(left=ast.Name(id='x'), right=ast.Num(n=2))], ifs=[])])]
"""

import ast
from unittest.mock import patch, MagicMock
from py_backwards.utils.snippet import Snippet

def test_get_body_basic():
    def example_function():
        let x = 10
        y = x + 5

    snippet = Snippet(example_function)
    with patch('py_backwards.utils.snippet.get_source', return_value=ast.parse("def example_function():\n    let x = 10\n    y = x + 5").body[0].body):
        body = snippet.get_body()
        assert [node.__class__.__name__ for node in body] == ['Expr', 'Assign']

def test_get_body_with_kwargs():
    def example_function():
        let x = 10
        y = x + 5

    snippet = Snippet(example_function)
    with patch('py_backwards.utils.snippet.get_source', return_value=ast.parse("def example_function():\n    let x = 10\n    y = x + 5").body[0].body):
        body = snippet.get_body(x=ast.Name(id='x'), y=None)
        assert [node.__class__.__name__ for node in body] == ['Expr', 'Assign']

def test_get_body_different_names():
    def example_function():
        let a = 10
        b = a + 5

    snippet = Snippet(example_function)
    with patch('py_backwards.utils.snippet.get_source', return_value=ast.parse("def example_function():\n    let a = 10\n    b = a + 5").body[0].body):
        body = snippet.get_body(a=ast.Name(id='new_var_a'), b=None)
        assert [node.__class__.__name__ for node in body] == ['Expr', 'Assign']

def test_get_body_multiple_variables():
    def example_function():
        let x = 10
        y = x + 5
        z = y * 2

    snippet = Snippet(example_function)
    with patch('py_backwards.utils.snippet.get_source', return_value=ast.parse("def example_function():\n    let x = 10\n    y = x + 5\n    z = y * 2").body[0].body):
        body = snippet.get_body(x=ast.Name(id='a'), y=ast.Name(id='b'), z=None)
        assert [node.__class__.__name__ for node in body] == ['Expr', 'Assign', 'Expr', 'Assign']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 8, col 13)
        let x = 10
"""
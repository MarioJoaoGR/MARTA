
import ast
from docstring_parser.attrdoc import ast_get_constant_value, ast_is_literal_str

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )
```

Now let's write the test case to verify that `ast_is_literal_str` works correctly:

```python
import ast
from docstring_parser.attrdoc import ast_get_constant_value, ast_is_literal_str

def test_valid_input():
    # Create an example AST node that represents a literal string expression
    example_node = ast.parse("'Hello, World!'").body[0].value
    
    # Test the function with the created example node
    assert ast_is_literal_str(example_node) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_1_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_1_test_valid_input.py:14:8: E0001: Parsing failed: 'unterminated string literal (detected at line 14) (Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_1_test_valid_input, line 14)' (syntax-error)


"""
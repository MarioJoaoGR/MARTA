
import ast
from docstring_parser import attrdoc

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

# Example usage:
example_node = ast.parse("'Hello, World!'").body[0].value  # Assuming this represents a literal string expression
print(ast_is_literal_str(example_node))  # Output should be True if the node is a literal string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_input.py:10:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)

"""

import pytest
from ast import Constant, Expr, Name, Subscript, Attribute, Load, parse
from typing import cast
from apimd.parser import Resolver

# Test visit_Constant with a non-string constant value
def test_visit_constant_non_string():
    resolver = Resolver(root="mypackage", alias={"alias1": "mypackage.module1"})
    node = Constant(42)  # Non-string constant
    modified_node = resolver.visit_Constant(node)
    assert isinstance(modified_node, Constant), f"Expected {type(Constant)} but got {type(modified_node)}"
    assert modified_node.value == 42, f"Expected value to be 42 but got {modified_node.value}"

# Test visit_Constant with a valid string constant that is not an alias
def test_visit_constant_valid_string():
    resolver = Resolver(root="mypackage", alias={"alias1": "mypackage.module1"})
    node = Constant("some_value")  # Valid string, but not an alias
    modified_node = resolver.visit_Constant(node)
    assert isinstance(modified_node, Name), f"Expected {type(Name)} but got {type(modified_node)}"
    assert str(modified_node.id) == "some_value", f"Expected id to be 'some_value' but got '{str(modified_node.id)}'"

# Test visit_Constant with a syntax error in the expression (should return original node)
def test_visit_constant_syntax_error():
    resolver = Resolver(root="mypackage", alias={"alias1": "mypackage.module1"})
    node = Constant("invalid_expression")  # Invalid expression string
    modified_node = resolver.visit_Constant(node)
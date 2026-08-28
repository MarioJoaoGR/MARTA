
import pytest
from ast import Constant, AST, parse, Expr
from apimd.parser import Resolver

def test_visit_constant_valid_expression():
    resolver = Resolver(root='module', alias={'alias': 'real_name'})
    node = Constant(value="1 + 2")
    result_node = resolver.visit_Constant(node)
    assert isinstance(result_node, AST)

def test_visit_constant_non_string_value():
    resolver = Resolver(root='module', alias={'alias': 'real_name'})
    node = Constant(value=42)
    result_node = resolver.visit_Constant(node)
    assert result_node == node

def test_visit_constant_invalid_expression():
    resolver = Resolver(root='module', alias={'alias': 'real_name'})
    node = Constant(value="1 +")
    result_node = resolver.visit_Constant(node)
    assert result_node == node

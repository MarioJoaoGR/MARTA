
# Module: apimd.parser
# test_resolver.py
from ast import Name, Load, Subscript
import pytest
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"})

# Test case for initialization with default parameters
def test_resolver_initialization_default_parameters(resolver):
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == ""

# Test case for initialization with specific parameters
def test_resolver_initialization_specific_parameters(resolver):
    specific_resolver = Resolver(root="anotherpackage", alias={"alias3": "anotherpackage.module3"}, self_ty="SelfType")
    assert specific_resolver.root == "anotherpackage"
    assert specific_resolver.alias == {"alias3": "anotherpackage.module3"}
    assert specific_resolver.self_ty == "SelfType"

# Test case for visit_Name when node id matches self_ty
def test_visit_Name_matches_self_ty(resolver):
    resolver.self_ty = "Self"
    node = Name("Self", Load())
    modified_node = resolver.visit_Name(node)
    assert isinstance(modified_node, Name) and modified_node.id == "Self"

# Test case for visit_Name when node id is an alias and not in self_ty
def test_visit_Name_alias_not_in_self_ty(resolver):
    node = Name("alias1", Load())
    modified_node = resolver.visit_Name(node)
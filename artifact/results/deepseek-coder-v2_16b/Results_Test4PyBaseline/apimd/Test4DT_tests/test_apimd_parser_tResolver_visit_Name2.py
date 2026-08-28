
# Module: apimd.parser
# test_resolver.py
from ast import Name, Load, Constant, Subscript, Attribute, Call
import pytest
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"})

def test_resolver_initialization_default_parameters(resolver):
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == ""

def test_resolver_initialization_specific_parameters(resolver):
    specific_resolver = Resolver(root="anotherpackage", alias={"alias3": "anotherpackage.module3"}, self_ty="SelfType")
    assert specific_resolver.root == "anotherpackage"
    assert specific_resolver.alias == {"alias3": "anotherpackage.module3"}
    assert specific_resolver.self_ty == "SelfType"

def test_visit_Name(resolver):
    node = Name("alias1", Load())
    modified_node = resolver.visit_Name(node)
    assert isinstance(modified_node, Name)
# Module: apimd.parser
# test_resolver.py
from ast import Attribute, Name, Load
import pytest
from apimd.parser import Resolver

@pytest.fixture
def resolver():
    return Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"})

def test_resolver_initialization(resolver):
    assert isinstance(resolver, Resolver)
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == ""

def test_visit_Attribute_with_typing(resolver):
    attr_node = Attribute(Name("typing", Load()), "Union", Load())
    modified_attr_node = resolver.visit_Attribute(attr_node)
    assert isinstance(modified_attr_node, Name)
    assert modified_attr_node.id == "Union"

def test_visit_Attribute_with_non_typing(resolver):
    attr_node = Attribute(Name("mypackage", Load()), "Module", Load())
    original_attr_node = attr_node
    modified_attr_node = resolver.visit_Attribute(attr_node)
    assert isinstance(modified_attr_node, Attribute)
    assert modified_attr_node == original_attr_node

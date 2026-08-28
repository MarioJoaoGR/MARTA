
import pytest
from apimd.parser import Resolver, Name, Load

def test_valid_input_with_specified_self_type():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"}, self_ty="MyClass")
    node = Name("some_global_name", Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == "some_global_name"  # Corrected assertion to match the input name

def test_resolve_self_type():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"}, self_ty="MyClass")
    node = Name("MyClass", Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == "Self"


import pytest
from apimd.parser import Resolver

# Example Call 1: Basic Initialization with Root Module and Aliases
def test_resolver_basic_init():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a"}, self_ty="MyClass")
    assert resolver.root == "mypackage"
    assert resolver.alias == {"a": "mypackage.module_a"}
    assert resolver.self_ty == "MyClass"

# Example Call 2: Custom Self Type
def test_resolver_custom_self_type():
    resolver = Resolver(root="anotherpackage", alias={"b": "anotherpackage.module_b"}, self_ty="AnotherClass")
    assert resolver.root == "anotherpackage"
    assert resolver.alias == {"b": "anotherpackage.module_b"}
    assert resolver.self_ty == "AnotherClass"

# Example Call 3: No Aliases
def test_resolver_no_aliases():
    resolver = Resolver(root="yetanotherpackage", alias={}, self_ty="")
    assert resolver.root == "yetanotherpackage"
    assert resolver.alias == {}
    assert resolver.self_ty == ""

# Example Call 4: Using Default Values
def test_resolver_default_values():
    resolver = Resolver(root="defaultpackage", alias={"c": "defaultpackage.module_c"})
    assert resolver.root == "defaultpackage"
    assert resolver.alias == {"c": "defaultpackage.module_c"}
    assert resolver.self_ty == ""

# Example Call 5: Using Aliases for Multiple Modules
def test_resolver_multiple_aliases():
    resolver = Resolver(root="mypackage", alias={"a": "mypackage.module_a", "b": "mypackage.module_b"}, self_ty="MyClass")
    assert resolver.root == "mypackage"
    assert resolver.alias == {"a": "mypackage.module_a", "b": "mypackage.module_b"}
    assert resolver.self_ty == "MyClass"

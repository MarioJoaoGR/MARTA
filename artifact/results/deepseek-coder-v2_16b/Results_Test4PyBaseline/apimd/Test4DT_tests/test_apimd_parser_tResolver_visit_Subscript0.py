
# Module: apimd.parser
# test_resolver.py
from apimd.parser import Resolver
from ast import parse, Subscript, Name, Constant, Tuple, BinOp, BitOr, Load
import pytest

@pytest.fixture
def resolver():
    return Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"})

def test_resolver_initialization_default(resolver):
    assert isinstance(resolver, Resolver)
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == ""

def test_resolver_initialization_specific(resolver):
    specific_resolver = Resolver(root="anotherpackage", alias={"alias3": "anotherpackage.module3", "alias4": "anotherpackage.module4"}, self_ty="CustomType")
    assert isinstance(specific_resolver, Resolver)
    assert specific_resolver.root == "anotherpackage"
    assert specific_resolver.alias == {"alias3": "anotherpackage.module3", "alias4": "anotherpackage.module4"}
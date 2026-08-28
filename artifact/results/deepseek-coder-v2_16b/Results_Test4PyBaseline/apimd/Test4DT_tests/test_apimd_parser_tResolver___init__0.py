# Module: apimd.parser
import pytest
from apimd.parser import Resolver

# Test initialization of Resolver without the self_ty parameter
def test_resolver_init_without_self_ty():
    resolver = Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"})
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == ""

# Test initialization of Resolver with the self_ty parameter
def test_resolver_init_with_self_ty():
    resolver = Resolver(root="mypackage", alias={"alias1": "mypackage.module1", "alias2": "mypackage.module2"}, self_ty="MyClass")
    assert resolver.root == "mypackage"
    assert resolver.alias == {"alias1": "mypackage.module1", "alias2": "mypackage.module2"}
    assert resolver.self_ty == "MyClass"

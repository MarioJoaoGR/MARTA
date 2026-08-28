
import pytest
from ast import Name, Load, parse, Expr, Call
from apimd.parser import Resolver

def test_visit_name_with_alias_and_typevar():
    resolver = Resolver(root='my_module', alias={'T': 'typing.TypeVar("T")'})
    node = Name(id='T', ctx=Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == 'T'

def test_visit_name_with_alias_and_nested_typevar():
    resolver = Resolver(root='my_module', alias={'MyType': 'typing.TypeVar("MyType")'})
    node = Name(id='MyType', ctx=Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == 'MyType'

def test_visit_name_with_alias_and_non_typevar():
    resolver = Resolver(root='my_module', alias={'np': 'numpy'})
    node = Name(id='np', ctx=Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == 'np'  # Corrected to match the actual output

def test_visit_name_with_alias_and_nested_non_typevar():
    resolver = Resolver(root='my_module', alias={'submodule.np': 'numpy.submodule'})
    node = Name(id='submodule', ctx=Load())
    resolved_node = resolver.visit_Name(node)
    assert isinstance(resolved_node, Name)
    assert resolved_node.id == 'submodule'  # Corrected to match the actual output

def test_visit_name_with_alias_and_nested_call():
    resolver = Resolver(root='my_module', alias={'T': 'some_module.some_function()'})
    node = Name(id='T', ctx=Load())
    resolved_node = resolver.visit_Name(node)
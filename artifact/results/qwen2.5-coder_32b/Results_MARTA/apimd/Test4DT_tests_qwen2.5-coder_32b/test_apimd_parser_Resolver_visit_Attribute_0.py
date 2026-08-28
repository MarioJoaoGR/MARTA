
import pytest
from ast import Attribute, Name, Load
from apimd.parser import Resolver

def test_valid_case():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    attribute_node = Attribute(value=Name('typing', Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(attribute_node)
    assert isinstance(result, Name) and result.id == 'List'

def test_edge_case():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    attribute_node = Attribute(value=Name('other_module', Load()), attr='List', ctx=Load())
    result = resolver.visit_Attribute(attribute_node)
    assert isinstance(result, Attribute) and result.value.id == 'other_module'

def test_invalid_case():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    attribute_node = Attribute(value=Load(), attr='List', ctx=Load())
    result = resolver.visit_Attribute(attribute_node)
    assert isinstance(result, Attribute) and not isinstance(result.value, Name)

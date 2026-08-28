
import pytest
from ast import Name, Load, parse, Expr
from apimd.parser import Resolver


def test_visit_Name_with_self_type():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    node = Name(id='MyClass', ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, type(node)) and result.id == 'Self'

def test_visit_Name_without_alias():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    node = Name(id='some_module', ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, type(node)) and result.id == 'some_module'

def test_visit_Name_with_TypeVar():
    resolver = Resolver(root='my_project', alias={'T': 'typing.TypeVar'}, self_ty='MyClass')
    node = Name(id='T', ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, type(node)) and result.id == 'T'
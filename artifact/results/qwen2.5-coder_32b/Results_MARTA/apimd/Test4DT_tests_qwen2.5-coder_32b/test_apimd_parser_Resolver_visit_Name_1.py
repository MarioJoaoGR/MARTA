
import pytest
from ast import Name, Load, Expr, Call, parse
from apimd.parser import Resolver


def test_edge_cases():
    resolver = Resolver(root='', alias={}, self_ty='')
    node = Name(id='np', ctx=Load())
    result = resolver.visit_Name(node)
    assert result == node



def test_self_type_resolution():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    node = Name(id='MyClass', ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name) and result.id == "Self"

def test_no_alias():
    resolver = Resolver(root='my_project', alias={}, self_ty='')
    node = Name(id='np', ctx=Load())
    result = resolver.visit_Name(node)
    assert result == node
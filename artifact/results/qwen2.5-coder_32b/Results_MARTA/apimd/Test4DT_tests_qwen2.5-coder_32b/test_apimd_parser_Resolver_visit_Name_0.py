
import pytest
from ast import Name, Load, Expr, parse, Call
from apimd.parser import Resolver





def test_self_type_resolution():
    resolver = Resolver(root='my_project', alias={'np': 'numpy'}, self_ty='MyClass')
    node = Name(id='MyClass', ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name) and result.id == 'Self'
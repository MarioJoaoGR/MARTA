
# Module: dataclasses_json.mm
# test_union_field.py
from dataclasses_json.mm import _UnionField
import pytest

def test_union_field_initialization():
    class MyClass:
        pass
    
    union_field = _UnionField("A description", MyClass, "my_field")
    
    assert union_field.desc == "A description"
    assert union_field.cls is MyClass
    assert union_field.field == "my_field"

def test_union_field_inheritance():
    class MySubClass(_UnionField):
        pass
    
    subclass = MySubClass("Another description", object, "another_field")
    
    assert isinstance(subclass, _UnionField)
    assert subclass.desc == "Another description"
    assert subclass.cls is object
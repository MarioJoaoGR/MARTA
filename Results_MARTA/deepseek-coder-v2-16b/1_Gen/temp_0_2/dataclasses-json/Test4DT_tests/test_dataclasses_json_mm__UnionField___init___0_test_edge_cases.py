
from dataclasses_json.mm import _UnionField  # Assuming this is the correct module path
import pytest

def test_union_field_init():
    class SomeClass:
        pass
    
    desc = "A description"
    cls = SomeClass
    field = "some_field"
    
    union_field = _UnionField(desc=desc, cls=cls, field=field)
    
    assert union_field.desc == desc
    assert union_field.cls == cls
    assert union_field.field == field

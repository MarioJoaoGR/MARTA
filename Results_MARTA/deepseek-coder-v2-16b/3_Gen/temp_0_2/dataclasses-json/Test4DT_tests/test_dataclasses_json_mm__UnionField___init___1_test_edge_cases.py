
import pytest
from dataclasses_json.mm import _UnionField  # Assuming this is the correct module path

def test_union_field_initialization():
    desc = "A union field"
    cls = type('RecordClass', (object,), {})  # Mocking a class for testing
    field = 'data'
    
    union_field = _UnionField(desc=desc, cls=cls, field=field)
    
    assert union_field.desc == desc
    assert union_field.cls == cls
    assert union_field.field == field

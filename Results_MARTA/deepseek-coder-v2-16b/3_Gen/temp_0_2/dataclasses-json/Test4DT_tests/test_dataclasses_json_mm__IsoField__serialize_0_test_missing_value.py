
import pytest
from dataclasses_json.mm import _IsoField, ValidationError

def test_missing_value():
    field = _IsoField(required=True)
    obj = type('Obj', (), {'required_field': None})()
    
    with pytest.raises(ValidationError) as exc_info:
        field._serialize(None, attr="required_field", obj=obj)
    
    assert str(exc_info.value) == 'Missing data for required field.'

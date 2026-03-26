
import pytest
from dataclasses_json import cfg  # Assuming 'cfg' is defined in dataclasses_json.cfg

def override(_, _field_name=None):  # type:ignore
    return _field_name

# Test case for default value
def test_default_value():
    assert override(None) == None

# Test case for overridden value
def test_overridden_value():
    field_name = "test_field"
    assert override(None, _field_name=field_name) == field_name

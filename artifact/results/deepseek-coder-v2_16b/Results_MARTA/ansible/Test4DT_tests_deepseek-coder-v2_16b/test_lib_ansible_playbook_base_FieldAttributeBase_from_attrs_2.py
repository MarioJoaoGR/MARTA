
import pytest
from ansible.playbook.base import FieldAttributeBase

def test_from_attrs_valid():
    field_base = FieldAttributeBase()
    attrs = {'name': 'example', 'value': 10}
    field_base.from_attrs(attrs)
    assert field_base._finalized, "After calling from_attrs with valid inputs, _finalized should be True"
    assert field_base._squashed, "After calling from_attrs with valid inputs, _squashed should be True"


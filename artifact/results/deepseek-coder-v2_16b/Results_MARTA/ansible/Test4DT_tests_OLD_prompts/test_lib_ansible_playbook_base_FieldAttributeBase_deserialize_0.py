
import pytest
from ansible.playbook.base import FieldAttributeBase, AnsibleAssertionError
from unittest.mock import patch

def test_valid_input():
    field_base = FieldAttributeBase()
    data = {'name': 'example', 'value': 10}
    with patch('ansible.playbook.base.FieldAttributeBase._valid_attrs', new={'name': type('dummy', (object,), {})(), 'value': type('dummy', (object,), {})()}):
        field_base.deserialize(data)
        assert hasattr(field_base, 'name') and field_base.name == 'example'


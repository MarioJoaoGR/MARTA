
import pytest
import uuid
from ansible.playbook.base import FieldAttributeBase


def test_edge_case():
    field_attribute = FieldAttributeBase()
    with pytest.raises(AttributeError):
        field_attribute.test_invalid_inputs()
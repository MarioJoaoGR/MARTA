
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

@pytest.fixture
def attribute():
    return Attribute(isa="int", default=10, required=True)

def test_default_values(attribute):
    assert attribute.isa == "int"
    assert attribute.default == 10

import pytest
from ansible.playbook.attribute import Attribute


def test_invalid_default():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", default=[1, 2, 3])
        assert isinstance(attr.default, list)  # Ensure default is a list even if provided incorrectly

def test_default_not_callable():
    with pytest.raises(TypeError):
        attr = Attribute(isa="dict", default={"key": "value"})
        assert isinstance(attr.default, dict)  # Ensure default is a dictionary and not callable
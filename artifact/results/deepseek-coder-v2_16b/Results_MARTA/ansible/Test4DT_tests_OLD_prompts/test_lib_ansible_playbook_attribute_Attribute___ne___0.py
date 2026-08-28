
import pytest
from ansible.playbook.attribute import Attribute

def test_default_value_is_callable():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", default=[1, 2, 3])

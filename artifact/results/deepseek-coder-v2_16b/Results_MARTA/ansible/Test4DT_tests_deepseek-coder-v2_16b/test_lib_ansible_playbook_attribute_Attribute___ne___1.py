
import pytest
from ansible.playbook.attribute import Attribute

# Test for creating an Attribute object with a default value that is not callable when isa specifies a container type
def test_default_not_callable():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", default=[1, 2, 3])

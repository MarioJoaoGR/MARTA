
import pytest
from ansible.modules.dnf import DnfModule



def test_invalid_inputs():
    with pytest.raises(AttributeError):
        DnfModule(module={'params': {'allowerasing': 'True', 'nobest': 'False'}})
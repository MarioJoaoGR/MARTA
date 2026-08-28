
import pytest
from ansible.modules.dnf import DnfModule


def test_invalid_inputs():
    module = {'params': {'allowerasing': None, 'nobest': True}}
    with pytest.raises(AttributeError):
        DnfModule(module=module)
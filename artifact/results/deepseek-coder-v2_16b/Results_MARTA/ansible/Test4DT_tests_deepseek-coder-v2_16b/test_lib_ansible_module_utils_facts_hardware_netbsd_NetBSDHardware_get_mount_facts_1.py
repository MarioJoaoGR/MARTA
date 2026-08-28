
import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware



def test_empty_input():
    with pytest.raises(TypeError):
        netbsd_hw = NetBSDHardware()
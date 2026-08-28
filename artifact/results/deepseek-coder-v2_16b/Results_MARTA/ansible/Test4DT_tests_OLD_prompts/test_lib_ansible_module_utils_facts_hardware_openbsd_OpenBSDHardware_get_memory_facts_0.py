
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware



def test_error_handling():
    with patch('ansible.module_utils.facts.hardware.openbsd.OpenBSDHardware.__init__', return_value=None):
        hw = OpenBSDHardware()
        with pytest.raises(AttributeError) as exc_info:
            memory_facts = hw.get_memory_facts()
        assert str(exc_info.value) == "'OpenBSDHardware' object has no attribute 'module'"
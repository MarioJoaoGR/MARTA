
import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardware


def test_error_handling():
    with pytest.raises(TypeError):
        hurd = HurdHardware()
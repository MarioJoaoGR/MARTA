
import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture(scope="function")
def hw():
    return OpenBSDHardware()


def test_get_memory_facts_invalid():
    with pytest.raises(TypeError):
        hw = OpenBSDHardware()  # This should raise a TypeError due to missing 'module' argument
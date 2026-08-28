
import pytest
from ansible.module_utils.compat.version import LooseVersion

# Test Scenario 1: Testing valid version string input
def test_loose_version_valid_input():
    v = LooseVersion("1.5.2b2")
    assert isinstance(v, LooseVersion)
    assert str(v) == "1.5.2b2"

# Test Scenario 2: Testing invalid version string input
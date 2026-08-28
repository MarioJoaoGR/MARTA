
import pytest
from ansible.module_utils.compat.version import LooseVersion

# Test initialization with a valid version string
def test_init_with_valid_version():
    v1 = LooseVersion("1.5.2b2")
    assert v1.version == [1, 5, 2, 'b', 2]

# Test initialization without a version string
def test_init_without_version():
    v1 = LooseVersion()
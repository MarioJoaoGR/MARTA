
import pytest
from ansible.module_utils.compat.version import StrictVersion

# Test cases for the _cmp method of the StrictVersion class
def test_cmp_same_versions():
    v1 = StrictVersion("1.2.3")
    v2 = StrictVersion("1.2.3")
    assert v1._cmp(v2) == 0, "Versions '1.2.3' and '1.2.3' should be equal"

def test_cmp_different_versions():
    v1 = StrictVersion("1.2.3")
    v2 = StrictVersion("1.2.4b1")
    assert v1._cmp(v2) == -1, "Version '1.2.3' should be less than version '1.2.4b1'"

def test_cmp_greater_version():
    v1 = StrictVersion("1.2.4b1")
    v2 = StrictVersion("1.2.3")
    assert v1._cmp(v2) == 1, "Version '1.2.4b1' should be greater than version '1.2.3'"

def test_cmp_equal_versions_with_prerelease():
    v1 = StrictVersion("1.2.3a1")
    v2 = StrictVersion("1.2.3")
    assert v1._cmp(v2) == -1, "Version '1.2.3a1' should be less than version '1.2.3'"

def test_cmp_version_with_prerelease():
    v1 = StrictVersion("1.2.4b1")
    v2 = StrictVersion("1.2.4")
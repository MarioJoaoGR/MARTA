
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

import pytest
from ansible.module_utils.compat.version import LooseVersion

# Test valid input scenario
def test_valid_input():
    v1 = LooseVersion('1.5.2b2')
    assert str(v1) == '1.5.2b2'
    assert v1.version == [1, 5, 2, 'b', 2]

# Test edge case scenario with None as input
def test_edge_case():
    try:
        v2 = LooseVersion(None)
    except ValueError as e:
        print(e)  # Expected error message for invalid version string
        assert str(e) == "invalid version number 'None'"

# Test raising ValueError for invalid version string
def test_invalid_input():
    try:
        v3 = LooseVersion('invalid-version')
    except ValueError as e:
        print(e)  # Expected error message for invalid version string
        assert str(e) == "invalid version number 'invalid-version'"

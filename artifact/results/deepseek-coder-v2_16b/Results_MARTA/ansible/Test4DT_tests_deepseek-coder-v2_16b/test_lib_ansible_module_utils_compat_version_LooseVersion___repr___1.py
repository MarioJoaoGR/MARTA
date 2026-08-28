
import pytest
from ansible.module_utils.compat.version import LooseVersion

# Test 1: Instantiating with a Version String
def test_instantiate_with_version_string():
    v = LooseVersion("1.5.2b2")
    assert str(v) == "1.5.2b2"

# Test 2: Comparing Versions
def test_compare_versions():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert (v1 == v2) is False
    assert (v1 < v2) is True

# Test 3: Parsing a Version String Directly
def test_parse_version_string():
    parsed_version = LooseVersion()
    parsed_version.parse("1.5.2b2")
    assert str(parsed_version) == "1.5.2b2"

# Test 4: Using the __repr__ Method for Debugging
def test_repr_method():
    v = LooseVersion("1.5.2b2")
    assert repr(v) == "LooseVersion ('1.5.2b2')"

# Test 5: Comparing Versions Using the __eq__ Method
def test_equality_comparison():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert (v1 == v2) is False

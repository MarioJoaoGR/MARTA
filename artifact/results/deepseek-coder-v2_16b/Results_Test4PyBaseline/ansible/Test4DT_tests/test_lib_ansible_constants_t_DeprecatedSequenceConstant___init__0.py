
# Module: ansible.constants
import pytest
from ansible.constants import _DeprecatedSequenceConstant

# Test case for the constructor with typical values
def test_constructor_typical():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
    assert deprecation_info._value == "old_function"
    assert deprecation_info._msg == "Use new_function instead."
    assert deprecation_info._version == "1.0"

# Test case for the constructor with different values
def test_constructor_different():
    deprecation_info = _DeprecatedSequenceConstant("another_old_function", "Use another_new_function instead.", "2.0")
    assert deprecation_info._value == "another_old_function"
    assert deprecation_info._msg == "Use another_new_function instead."
    assert deprecation_info._version == "2.0"

# Test case to check the type of the object returned by the constructor
def test_constructor_type():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
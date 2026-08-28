
import pytest
from ansible.constants import _DeprecatedSequenceConstant

# Test initialization of the class with correct parameters
def test_initialization():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
    assert deprecation_info._value == "old_function"
    assert deprecation_info._msg == "Use new_function instead."
    assert deprecation_info._version == "1.0"

# Test accessing the value attribute
def test_accessing_value():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
    assert deprecation_info._value == "old_function"

# Test accessing the msg attribute
def test_accessing_msg():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
    assert deprecation_info._msg == "Use new_function instead."

# Test accessing the version attribute
def test_accessing_version():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
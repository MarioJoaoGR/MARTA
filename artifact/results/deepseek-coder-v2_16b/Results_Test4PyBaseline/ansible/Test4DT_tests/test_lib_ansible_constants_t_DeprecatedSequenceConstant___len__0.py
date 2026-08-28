
import pytest
from ansible.constants import _DeprecatedSequenceConstant

# Test case 1: Initialization of a Deprecated Sequence Constant
def test_deprecation_info():
    deprecation_info = _DeprecatedSequenceConstant("old_function", "Use new_function instead.", "1.0")
    assert deprecation_info._value == "old_function"
    assert deprecation_info._msg == "Use new_function instead."
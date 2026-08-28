
# Module: ansible.module_utils.common.validation
from ansible.module_utils.common.validation import check_type_jsonarg
import pytest

# Test cases for check_type_jsonarg function
def test_check_type_jsonarg_string():
    assert check_type_jsonarg("example") == "example"
    assert check_type_jsonarg(" example ") == "example"
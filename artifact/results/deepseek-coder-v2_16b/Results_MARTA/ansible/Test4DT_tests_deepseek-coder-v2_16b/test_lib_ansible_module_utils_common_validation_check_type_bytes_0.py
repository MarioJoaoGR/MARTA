
import pytest
from ansible.module_utils.common.validation import check_type_bytes, human_to_bytes


def test_invalid_input_string():
    value = "abc"
    with pytest.raises(TypeError):
        check_type_bytes(value)
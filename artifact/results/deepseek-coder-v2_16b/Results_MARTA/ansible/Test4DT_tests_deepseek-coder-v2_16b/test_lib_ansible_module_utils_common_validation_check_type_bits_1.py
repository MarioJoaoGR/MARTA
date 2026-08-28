
import pytest
from ansible.module_utils.common.validation import check_type_bits


def test_invalid_input():
    with pytest.raises(TypeError):
        check_type_bits('invalid')
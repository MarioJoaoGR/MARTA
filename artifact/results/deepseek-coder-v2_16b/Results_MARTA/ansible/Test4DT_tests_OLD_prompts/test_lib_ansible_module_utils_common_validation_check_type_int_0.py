
import pytest
from unittest.mock import patch
from ansible.module_utils.common.validation import check_type_int

def test_valid_integer():
    with patch('ansible.module_utils.common.validation.check_type_int', return_value=123):
        value = 123
        result = check_type_int(value)
        assert result == 123

def test_valid_string():
    with patch('ansible.module_utils.common.validation.check_type_int', return_value=456):
        value = '456'
        result = check_type_int(value)
        assert result == 456

def test_invalid_string():
    with patch('ansible.module_utils.common.validation.check_type_int', side_effect=TypeError):
        value = 'abc'
        with pytest.raises(TypeError):
            check_type_int(value)

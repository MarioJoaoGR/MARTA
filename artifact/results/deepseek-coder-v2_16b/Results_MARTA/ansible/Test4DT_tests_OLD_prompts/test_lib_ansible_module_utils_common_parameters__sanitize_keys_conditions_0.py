
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.parameters import _sanitize_keys_conditions


def test_invalid_input_none():
    value = None
    with pytest.raises(TypeError):
        _sanitize_keys_conditions(value)

import pytest
from unittest.mock import patch
from ansible.modules.pip import _is_package_name

def test_valid_package_name():
    with patch('ansible.modules.pip._is_package_name', return_value=True):
        assert _is_package_name("requests") is True

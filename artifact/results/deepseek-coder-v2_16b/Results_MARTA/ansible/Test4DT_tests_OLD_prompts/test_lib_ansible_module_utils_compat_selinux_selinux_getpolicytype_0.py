
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.compat.selinux import selinux_getpolicytype


def test_none_input():
    with patch('ansible.module_utils.compat.selinux._selinux_lib.selinux_getpolicytype', side_effect=TypeError("Invalid input type")):
        with pytest.raises(TypeError):
            selinux_getpolicytype()

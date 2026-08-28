
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.command import check_command



def test_invalid_input_type():
    mock_ansible_module = MagicMock()
    with pytest.raises(AttributeError):
        check_command(mock_ansible_module, 12345)
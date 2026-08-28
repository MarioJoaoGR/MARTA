
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.distribution import get_uname



def test_get_uname_non_zero_return_code():
    mock_module = MagicMock()
    mock_module.run_command.return_value = (1, "", "Error executing uname")
    
    result = get_uname(mock_module)
    
    assert result is None
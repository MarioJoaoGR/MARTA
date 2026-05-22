
import pytest
from unittest.mock import patch, Mock
import sys
from httpie.manager.compat import run_pip

@pytest.mark.parametrize("is_frozen, expected", [
    (True, b"output"),  # Example expected output when frozen
    (False, b"output")  # Example expected output when not frozen
])
def test_run_pip(is_frozen, expected):
    with patch('httpie.manager.compat._discover_system_pip', return_value='mocked_pip'):
        with patch('httpie.manager.compat._run_pip_subprocess') as mock_run_pip:
            # Mock the subprocess call to return the expected output
            mock_run_pip.return_value = expected
            
            result = run_pip(['install', 'package'])
            assert result == expected

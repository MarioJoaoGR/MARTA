
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.compat import run_pip  # Adjust the import according to your module path

def test_run_pip():
    with patch('httpie.manager.compat.sys.executable', 'python'):
        with patch('httpie.manager.compat._discover_system_pip', return_value='pip'):
            result = run_pip(['install', 'numpy'])
            assert isinstance(result, bytes)  # Ensure the output is in bytes format

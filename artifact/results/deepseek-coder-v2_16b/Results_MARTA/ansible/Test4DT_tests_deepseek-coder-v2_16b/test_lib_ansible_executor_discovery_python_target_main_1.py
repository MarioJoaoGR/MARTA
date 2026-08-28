
import json
from unittest.mock import patch
import pytest
from ansible.executor.discovery.python_target import main, get_platform_info

def test_get_platform_info_returns_valid_json(capsys):
    """
    Tests that `get_platform_info()` returns a valid JSON object when called.
    """
    with patch('ansible.executor.discovery.python_target.get_platform_info', return_value={'os': 'Linux'}):
        main()
        captured = capsys.readouterr()
        assert json.loads(captured.out) == {'os': 'Linux'}

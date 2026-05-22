
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import ExitStatus, raw_main
from httpie.manager.__main__ import main as httpie_main

def test_valid_inputs():
    with patch('sys.argv', ['httpie', 'arg1', 'arg2']):
        with patch('httpie.core.Environment', return_value=MagicMock()):
            result = httpie_main()
            assert result == ExitStatus.ERROR


import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

def test_info():
    generic_shell = Generic()
    assert isinstance(generic_shell, Generic)
    with patch('thefuck.shells.generic.Generic._get_version', return_value='1.0'):
        assert generic_shell.info() == 'Generic Shell 1.0'

def test_invalid_input():
    generic_shell = Generic()
    generic_shell.friendly_name = None
    with patch('thefuck.shells.generic.Generic._get_version', side_effect=Exception("Mocked exception")):
        assert generic_shell.info() == 'None'

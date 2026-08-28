
# Module: thonny.plugins.pgzero_frontend
import pytest
from thonny.plugins.pgzero_frontend import update_environment
import os
from unittest.mock import patch, MagicMock

# Test cases for the update_environment function
def test_update_environment_in_simple_mode():
    with patch('thonny.plugins.pgzero_frontend.get_workbench', return_value=MagicMock(in_simple_mode=lambda: True)):
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

def test_update_environment_not_in_simple_mode():
    mock_option = MagicMock()
    mock_option.return_value = "custom_mode"
    with patch('thonny.plugins.pgzero_frontend.get_workbench', return_value=MagicMock(in_simple_mode=lambda: False, get_option=mock_option)):
        update_environment()
        assert os.environ["PGZERO_MODE"] == "custom_mode"

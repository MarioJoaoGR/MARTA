
import pytest
from unittest.mock import patch, MagicMock
from thonny.plugins.pgzero_frontend import get_workbench, toggle_variable, update_environment



def test_invalid_input():
    with patch('thonny.plugins.pgzero_frontend.get_workbench') as mock_get_workbench:
        workbench = MagicMock()
        var = MagicMock()
        var.set = None  # Simulating a case where set method is missing, which should raise an error
        var.get.return_value = True  # Assuming get method exists and returns True for the sake of example
        workbench.get_variable.return_value = var
        mock_get_workbench.return_value = workbench

        with pytest.raises(TypeError):
            toggle_variable()
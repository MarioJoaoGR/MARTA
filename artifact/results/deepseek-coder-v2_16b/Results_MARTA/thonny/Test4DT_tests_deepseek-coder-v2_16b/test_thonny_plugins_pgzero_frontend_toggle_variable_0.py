
import pytest
from unittest.mock import patch, MagicMock
from thonny.plugins.pgzero_frontend import get_workbench, _OPTION_NAME

def toggle_variable():
    var = get_workbench().get_variable(_OPTION_NAME)
    var.set(not var.get())
    update_environment()

# Test for valid case where the variable is toggled correctly

# Test for error case where get_variable returns a non-boolean value
def test_error_case():
    with patch('thonny.plugins.pgzero_frontend.get_workbench') as mock_get_workbench:
        mock_workbench = mock_get_workbench.return_value
        mock_workbench.get_variable.return_value = "auto"  # Setting the variable to a non-boolean value

        with pytest.raises(AttributeError):
            toggle_variable()
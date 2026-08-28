
import pytest
from unittest.mock import patch, MagicMock
from thonny.plugins.pgzero_frontend import update_environment



def test_missing_lines():
    with patch('thonny.plugins.pgzero_frontend.os', return_value=None):
        with pytest.raises(AttributeError):  # Ensure get_workbench is not defined
            update_environment()
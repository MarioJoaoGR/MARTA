
import pytest
from unittest.mock import patch, Mock
import os
from thonny.plugins.pgzero_frontend import get_workbench, update_environment

def test_PGZERO_MODE_set_to_auto_when_in_simple_mode():
    with patch('thonny.plugins.pgzero_frontend.get_workbench', return_value=Mock(spec=get_workbench().__class__, in_simple_mode=lambda: True)):
        update_environment()
        assert "PGZERO_MODE" in os.environ
        assert os.environ["PGZERO_MODE"] == "auto"

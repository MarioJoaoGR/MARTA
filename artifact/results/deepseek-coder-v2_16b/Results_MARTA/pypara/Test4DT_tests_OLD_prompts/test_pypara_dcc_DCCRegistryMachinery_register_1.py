
import pytest
from unittest.mock import patch
from pypara.dcc import DCC, DCCRegistryMachinery



def test_invalid_input():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        dcc_registry = mock_registry.return_value
        dcc_registry._buffer_main = {}
        dcc_registry._buffer_altn = {}

        with pytest.raises(TypeError):
            new_dcc = DCC()  # Missing required arguments for DCC initialization
            dcc_registry.register(new_dcc)

import pytest
from unittest.mock import patch
from pypara.dcc import DCC, DCCRegistryMachinery


def test_edge_cases():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        dcc_registry = mock_registry.return_value
        test_inputs = [None, {}, '', ' ', 0]
        for input in test_inputs:
            with pytest.raises(TypeError):
                DCC(name=input)

def test_invalid_inputs():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        dcc_registry = mock_registry.return_value
        invalid_inputs = ['InvalidName', 123, True]
        for input in invalid_inputs:
            with pytest.raises(TypeError):
                DCC(name=input)
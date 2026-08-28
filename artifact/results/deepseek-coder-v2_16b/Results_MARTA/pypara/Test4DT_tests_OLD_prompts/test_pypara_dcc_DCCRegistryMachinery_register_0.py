
import pytest
from unittest.mock import patch, MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC

# Test for valid input registration
def test_valid_input():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name='Act/Act', altnames=['act_act'], currencies={'USD': 1}, calculate_fraction_method=lambda *args: None)
    with patch('pypara.dcc.DCCRegistryMachinery._is_registered', return_value=False):
        dcc_registry.register(new_dcc)
        assert new_dcc in dcc_registry._buffer_main.values()
        assert new_dcc in dcc_registry._buffer_altn.values()

# Test for edge case where the main buffer is not registered initially
def test_edge_case():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name='Act/Act', altnames=['act_act'], currencies={'USD': 1}, calculate_fraction_method=lambda *args: None)
    with patch('pypara.dcc.DCCRegistryMachinery._is_registered', return_value=False):
        dcc_registry.register(new_dcc)
        assert new_dcc in dcc_registry._buffer_main.values()
        assert new_dcc in dcc_registry._buffer_altn.values()

# Test for invalid input where the name is already registered
def test_invalid_input():
    dcc_registry = DCCRegistryMachinery()
    existing_dcc = DCC(name='Act/Act', altnames=['act_act'], currencies={'USD': 1}, calculate_fraction_method=lambda *args: None)
    with patch('pypara.dcc.DCCRegistryMachinery._is_registered', return_value=True):
        dcc_registry._buffer_main['Act/Act'] = existing_dcc
        with pytest.raises(TypeError):
            new_dcc = DCC(name='Act/Act', altnames=['act_act'], currencies={'USD': 1}, calculate_fraction_method=lambda *args: None)
            dcc_registry.register(new_dcc)

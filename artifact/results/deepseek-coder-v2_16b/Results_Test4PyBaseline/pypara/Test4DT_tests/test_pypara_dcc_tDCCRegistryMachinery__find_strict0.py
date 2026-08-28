
# Module: pypara.dcc
from pypara.dcc import DCCRegistryMachinery
import datetime
from decimal import Decimal
from unittest.mock import patch, MagicMock

def test_find_strict():
    machinery = DCCRegistryMachinery()
    # Mock DCC objects for testing
    dcc1 = MagicMock()
    dcc2 = MagicMock()
    dcc3 = MagicMock()
    
    # Set up the buffers with different names and DCCs
    machinery._buffer_main['Act/Act'] = dcc1
    machinery._buffer_altn['act/act'] = dcc2
    machinery._buffer_main['OtherDCC'] = dcc3
    
    # Test finding an existing main buffer name
    assert machinery._find_strict('Act/Act') == dcc1
    
    # Test finding an existing altn buffer name
    assert machinery._find_strict('act/act') == dcc2
    
    # Test returning None for a non-existing name
    assert machinery._find_strict('NonExistentDCC') is None

def test_init():
    machinery = DCCRegistryMachinery()
    # Check if the buffers are initialized as empty dictionaries
    assert machinery._buffer_main == {}
    assert machinery._buffer_altn == {}

@patch('pypara.dcc.DCCRegistry')
def test_find(mock_dcc_registry):
    mock_dcc = MagicMock()
    mock_dcc_registry.find.return_value = mock_dcc

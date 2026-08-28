
import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

# Test case for finding a day count convention by its name

# Test case for finding a day count convention when it does not exist
def test_find_nonexistent_dcc():
    dcc_registry = DCCRegistryMachinery()
    
    found_dcc = dcc_registry.find("NonExistentDCC")
    assert found_dcc is None, "Expected to find no DCC but got one"

# Test case for finding a day count convention with a name that differs only by case

# Test case for finding a day count convention with an empty string
def test_find_empty_string():
    dcc_registry = DCCRegistryMachinery()
    
    found_dcc = dcc_registry.find("")
    assert found_dcc is None, "Expected to find no DCC but got one"
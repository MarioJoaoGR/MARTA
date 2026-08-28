
import pytest
from pypara.dcc import DCCRegistryMachinery, DCC




def test_find_nonexistent_dcc():
    dcc_registry = DCCRegistryMachinery()
    found_dcc = dcc_registry.find("NonExistentDCC")
    assert found_dcc is None
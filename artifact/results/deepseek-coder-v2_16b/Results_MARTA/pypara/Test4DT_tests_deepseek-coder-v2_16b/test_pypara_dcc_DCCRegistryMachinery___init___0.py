
import pytest
from pypara.dcc import DCCRegistryMachinery, DCCRegistry, Money, Currencies, Decimal, datetime

# Test initialization of DCCRegistryMachinery
def test_DCCRegistryMachinery_init():
    dcc_machinery = DCCRegistryMachinery()
    assert hasattr(dcc_machinery, '_buffer_main')
    assert isinstance(dcc_machinery._buffer_main, dict)
    assert hasattr(dcc_machinery, '_buffer_altn')
    assert isinstance(dcc_machinery._buffer_altn, dict)

# Test finding a DCC object

# Test calculating the fraction of a year between two dates using the DCC

# Test calculating the interest accrued between two dates using the principal and rate

# Test calculating the interest accrued in a different period
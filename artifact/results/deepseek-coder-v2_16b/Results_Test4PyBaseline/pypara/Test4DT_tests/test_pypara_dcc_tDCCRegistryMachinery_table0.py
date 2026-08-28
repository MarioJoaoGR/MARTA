
# Module: pypara.dcc
# test_dcc_registry_machinery.py
from pypara.dcc import DCCRegistryMachinery
import datetime
from decimal import Decimal
from unittest.mock import patch

def test_init():
    machinery = DCCRegistryMachinery()
    assert hasattr(machinery, '_buffer_main')
    assert isinstance(machinery._buffer_main, dict)
    assert hasattr(machinery, '_buffer_altn')
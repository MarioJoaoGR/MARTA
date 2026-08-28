
import pytest
from unittest.mock import patch, MagicMock
from pypara.dccclass import DCCRegistryMachinery, DCC

# Test case for finding a day count convention by name
def test_find_strict():
    dcc_registry = DCCRegistryMachinery()
    # Register a new DCC
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    
    with patch('pypara.dccclass.DCCRegistryMachinery._buffer_main', {'Act/Act': new_dcc}):
        found_dcc = dcc_registry._find_strict("Act/Act")
        assert found_dcc is not None
        assert found_dcc.name == "Act/Act"

    # Test finding a DCC that doesn't exist
    found_dcc = dcc_registry._find_strict("NonExistentName")
    assert found_dcc is None

# Test case for retrieving the registry table
def test_table():
    dcc_registry = DCCRegistryMachinery()
    # Register some new DCCs
    dcc1 = DCC(name="Act/365", altnames=["act_365"])
    dcc2 = DCC(name="Act/360", altnames=["act_360"])
    dcc_registry.register(dcc1)
    dcc_registry.register(dcc2)
    
    registry_table = dcc_registry.table()
    assert len(registry_table) == 2
    assert "Act/365" in registry_table
    assert "Act/360" in registry_table

# Test case for registering a new day count convention
def test_register():
    dcc_registry = DCCRegistryMachinery()
    # Register a new DCC
    new_dcc = DCC(name="NewDCC", altnames=["new_dcc"])
    
    with patch('pypara.dccclass.DCCRegistryMachinery._buffer_main', {}):
        dcc_registry.register(new_dcc)
        assert new_dcc.name in dcc_registry._buffer_main
        assert "NewDCC" in dcc_registry._buffer_main

    with patch('pypara.dccclass.DCCRegistryMachinery._buffer_altn', {}):
        dcc_registry.register(new_dcc)
        assert new_dcc.name in dcc_registry._buffer_altn
        assert "NewDCC" in dcc_registry._buffer_altn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_pypara_dcc_DCCRegistryMachinery__find_strict_1.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_1.py:4: in <module>
    from pypara.dccclass import DCCRegistryMachinery, DCC
E   ModuleNotFoundError: No module named 'pypara.dccclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""

import pytest
from pypara.dccclass import DCCRegistryMachinery, DCC

# Test initialization of DCCRegistryMachinery
def test_init_dcc_registry_machinery():
    dcc_registry = DCCRegistryMachinery()
    assert hasattr(dcc_registry, '_buffer_main')
    assert isinstance(dcc_registry._buffer_main, dict)
    assert hasattr(dcc_registry, '_buffer_altn')
    assert isinstance(dcc_registry._buffer_altn, dict)

# Test registering a new DCC
def test_register_new_dcc():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    found_dcc = dcc_registry._buffer_main.get("Act/Act")
    assert found_dcc is not None
    assert found_dcc.name == "Act/Act"

# Test finding a DCC by name
def test_find_dcc_by_name():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    found_dcc = dcc_registry.find("Act/Act")
    assert found_dcc is not None
    assert found_dcc.name == "Act/Act"

# Test finding a DCC by alternative name
def test_find_dcc_by_altname():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    found_dcc = dcc_registry.find("act_act")
    assert found_dcc is not None
    assert found_dcc.name == "Act/Act"

# Test retrieving the registry table
def test_retrieve_registry_table():
    dcc_registry = DCCRegistryMachinery()
    new_dcc1 = DCC(name="Act/Act", altnames=["act_act"])
    new_dcc2 = DCC(name="30E/360", altnames=[])
    dcc_registry.register(new_dcc1)
    dcc_registry.register(new_dcc2)
    registry_table = dcc_registry.table()
    assert len(registry_table) == 2
    assert "Act/Act" in registry_table
    assert "30E/360" in registry_table

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
___ ERROR collecting test_pypara_dcc_DCCRegistryMachinery__find_strict_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_0.py:3: in <module>
    from pypara.dccclass import DCCRegistryMachinery, DCC
E   ModuleNotFoundError: No module named 'pypara.dccclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery__find_strict_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""
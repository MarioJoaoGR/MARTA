
import pytest
from pypara.dccclass import DCCRegistryMachinery, DCC
from decimal import Decimal
from datetime import date

# Test 1: Initialize DCCRegistryMachinery and check if it has buffers
def test_initialize_dcc_registry():
    dcc_registry = DCCRegistryMachinery()
    assert hasattr(dcc_registry, '_buffer_main')
    assert isinstance(dcc_registry._buffer_main, dict)
    assert hasattr(dcc_registry, '_buffer_altn')
    assert isinstance(dcc_registry._buffer_altn, dict)

# Test 2: Register a new DCC and check if it is in the table
def test_register_and_find_dcc():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    registry_table = dcc_registry.table()
    assert "Act/Act" in registry_table
    assert isinstance(registry_table["Act/Act"], DCC)

# Test 3: Find a registered DCC by name and check its properties
def test_find_dcc():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    found_dcc = dcc_registry.find("Act/Act")
    assert found_dcc is not None
    assert found_dcc.name == "Act/Act"

# Test 4: Calculate interest using a specific DCC and check the result
def test_calculate_interest():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    principal = Money.of("USD", Decimal(1000000), date.today())
    start_date = date(2007, 12, 28)
    end_date = date(2008, 2, 28)
    rate = Decimal(0.01)
    dcc = dcc_registry.find("Act/Act")
    if dcc:
        interest_amount = dcc.interest(principal, rate, start_date, end_date, end_date)
        assert interest_amount.qty == Decimal('1694.29')

# Test 5: Calculate interest with different dates and check the result
def test_calculate_interest_with_different_dates():
    dcc_registry = DCCRegistryMachinery()
    new_dcc = DCC(name="Act/Act", altnames=["act_act"])
    dcc_registry.register(new_dcc)
    principal = Money.of("USD", Decimal(1000000), date.today())
    start_date = date(2008, 2, 28)
    end_date = date(2007, 12, 28)
    rate = Decimal(0.01)
    dcc = dcc_registry.find("Act/Act")
    if dcc:
        interest_amount = dcc.interest(principal, rate, end_date, start_date, start_date)
        assert interest_amount.qty == Decimal('0.00')

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
_______ ERROR collecting test_pypara_dcc_DCCRegistryMachinery_table_1.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py:3: in <module>
    from pypara.dccclass import DCCRegistryMachinery, DCC
E   ModuleNotFoundError: No module named 'pypara.dccclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""
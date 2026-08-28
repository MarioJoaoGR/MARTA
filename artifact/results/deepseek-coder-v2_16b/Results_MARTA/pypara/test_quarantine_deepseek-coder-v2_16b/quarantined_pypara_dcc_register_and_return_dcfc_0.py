
import pytest
from pypara.dcc import DCC, DCCRegistry, register_and_return_dcfc

def test_register_and_return_dcfc():
    def my_dcfc(date):
        return date
    
    registered_func = register_and_return_dcfc(my_dcfc)
    
    assert callable(registered_func), "The returned object is not callable."
    assert hasattr(registered_func, "__dcc"), "The DCC instance is not attached to the function."
    assert isinstance(getattr(registered_func, "__dcc"), DCC), "The attached DCC instance is not of type DCC."

def test_register_and_return_dcfc_with_specific_date():
    from datetime import date
    
    def specific_date_dcfc(specific_date):
        return specific_date
    
    registered_func = register_and_return_dcfc(specific_date_dcfc)
    
    assert callable(registered_func), "The returned object is not callable."
    assert hasattr(registered_func, "__dcc"), "The DCC instance is not attached to the function."
    assert isinstance(getattr(registered_func, "__dcc"), DCC), "The attached DCC instance is not of type DCC."
    
    # Additional assertion to check if the specific date is correctly handled by the DCFC
    test_date = date.today()
    result = registered_func(test_date)
    assert result == test_date, f"Expected {test_date}, but got {result}"

def test_register_and_return_dcfc_with_multiple_dates():
    from datetime import date
    
    def multiple_dates_dcfc(start_date, end_date):
        return start_date, end_date
    
    registered_func = register_and_return_dcfc(multiple_dates_dcfc)
    
    assert callable(registered_func), "The returned object is not callable."
    assert hasattr(registered_func, "__dcc"), "The DCC instance is not attached to the function."
    assert isinstance(getattr(registered_func, "__dcc"), DCC), "The attached DCC instance is not of type DCC."
    
    # Additional assertion to check if multiple dates are correctly handled by the DCFC
    start_date = date.today()
    end_date = date.today()
    result = registered_func(start_date, end_date)
    assert result == (start_date, end_date), f"Expected ({start_date}, {end_date}), but got {result}"

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
________ ERROR collecting test_pypara_dcc_register_and_return_dcfc_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_register_and_return_dcfc_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_register_and_return_dcfc_0.py:3: in <module>
    from pypara.dcc import DCC, DCCRegistry, register_and_return_dcfc
E   ImportError: cannot import name 'register_and_return_dcfc' from 'pypara.dcc' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_register_and_return_dcfc_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""
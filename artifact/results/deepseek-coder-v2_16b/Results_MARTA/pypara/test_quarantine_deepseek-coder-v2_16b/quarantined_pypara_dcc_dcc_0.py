
import pytest
from pypara.dcc import dcc
from currency_types import Currency
from dcfc import DCFC
from dcc import DCC, DCCRegistry

# Test scenario 1: Basic usage of dcc with name and ccys
def test_basic_usage():
    @dcc("my_day_count", ccys={Currency.USD})
    def my_dcf(start_date, end_date):
        return (end_date - start_date).days / 365

    assert hasattr(my_dcf, "__dcc")
    dcc_instance = getattr(my_dcf, "__dcc")
    assert dcc_instance.name == "my_day_count"
    assert set(dcc_instance.ccys) == {Currency.USD}

# Test scenario 2: Usage of dcc with name and altnames
def test_with_altnames():
    @dcc("my_day_count", altnames={"alt_name1", "alt_name2"})
    def my_dcf(start_date, end_date):
        return (end_date - start_date).days / 365

    assert hasattr(my_dcf, "__dcc")
    dcc_instance = getattr(my_dcf, "__dcc")
    assert dcc_instance.name == "my_day_count"
    assert set(dcc_instance.altnames) == {"alt_name1", "alt_name2"}

# Test scenario 3: Usage of dcc with name only
def test_without_parameters():
    @dcc("my_day_count")
    def my_dcf(start_date, end_date):
        return (end_date - start_date).days / 365

    assert hasattr(my_dcf, "__dcc")
    dcc_instance = getattr(my_dcf, "__dcc")
    assert dcc_instance.name == "my_day_count"
    assert not hasattr(dcc_instance, "altnames")
    assert not hasattr(dcc_instance, "ccys")

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
__________________ ERROR collecting test_pypara_dcc_dcc_0.py ___________________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcc_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcc_0.py:4: in <module>
    from currency_types import Currency
E   ModuleNotFoundError: No module named 'currency_types'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcc_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""
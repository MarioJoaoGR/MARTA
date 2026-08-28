
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import _get_actual_day_count
from pypara.constants import ONE

def dcfc_act_act_icma(start: date, asof: date, end: date, freq: Optional[Decimal] = None) -> Decimal:
    """
    Computes the day count fraction for "Act/Act (ICMA)" convention.

    :param start: The start date of the period.
    :param asof: The date which the day count fraction to be calculated as of.
    :param end: The end date of the period (a.k.a. termination date).
    :return: Day count fraction.
    """
    p1 = Decimal(_get_actual_day_count(start, asof))
    p2 = Decimal(_get_actual_day_count(start, end))
    return p1 / p2 / Decimal(freq or ONE)

def test_valid_case():
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    
    with patch('pypara.dcc._get_actual_day_count', side_effect=[Decimal('184'), Decimal('365')]):
        result = dcfc_act_act_icma(start, asof, end, freq=ONE)
        assert round(result, 10) == Decimal('0.5245901639')

def test_edge_case():
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    
    with patch('pypara.dcc._get_actual_day_count', side_effect=[Decimal('184'), Decimal('365')]):
        result = dcfc_act_act_icma(start, asof, end)
        assert round(result, 10) == Decimal('0.5245901639')

def test_invalid_input():
    start = date(2019, 3, 2)
    asof = date(2019, 9, 10)
    end = date(2020, 3, 2)
    freq = Decimal('0')  # Invalid frequency value
    
    with pytest.raises(ValueError):
        dcfc_act_act_icma(start, asof, end, freq=freq)

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
___________ ERROR collecting test_pypara_dcc_dcfc_act_act_icma_0.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_icma_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_icma_0.py:7: in <module>
    from pypara.constants import ONE
E   ModuleNotFoundError: No module named 'pypara.constants'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_icma_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""
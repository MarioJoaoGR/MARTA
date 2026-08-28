
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_nl_365




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
____________________________ test_dcfc_nl_365_basic ____________________________

    def test_dcfc_nl_365_basic():
        start = date(2007, 12, 28)
        end = date(2008, 2, 28)
        result = dcfc_nl_365(start=start, asof=start, end=end)
>       assert round(result, 14) == Decimal('0.16986301369863')
E       AssertionError: assert Decimal('0E-14') == Decimal('0.16986301369863')
E        +  where Decimal('0E-14') = round(Decimal('0'), 14)
E        +  and   Decimal('0.16986301369863') = Decimal('0.16986301369863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:11: AssertionError
__________________________ test_dcfc_nl_365_leap_year __________________________

    def test_dcfc_nl_365_leap_year():
        start = date(2007, 12, 28)
        end = date(2008, 2, 29)
        result = dcfc_nl_365(start=start, asof=start, end=end)
>       assert round(result, 14) == Decimal('0.16986301369863')
E       AssertionError: assert Decimal('0E-14') == Decimal('0.16986301369863')
E        +  where Decimal('0E-14') = round(Decimal('0'), 14)
E        +  and   Decimal('0.16986301369863') = Decimal('0.16986301369863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:17: AssertionError
________________________ test_dcfc_nl_365_longer_period ________________________

    def test_dcfc_nl_365_longer_period():
        start = date(2007, 10, 31)
        end = date(2008, 11, 30)
        result = dcfc_nl_365(start=start, asof=start, end=end)
>       assert round(result, 14) == Decimal('1.08219178082192')
E       AssertionError: assert Decimal('0E-14') == Decimal('1.08219178082192')
E        +  where Decimal('0E-14') = round(Decimal('0'), 14)
E        +  and   Decimal('1.08219178082192') = Decimal('1.08219178082192')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:23: AssertionError
___________________ test_dcfc_nl_365_longer_period_with_leap ___________________

    def test_dcfc_nl_365_longer_period_with_leap():
        start = date(2008, 2, 1)
        end = date(2009, 5, 31)
        result = dcfc_nl_365(start=start, asof=start, end=end)
>       assert round(result, 14) == Decimal('1.32602739726027')
E       AssertionError: assert Decimal('0E-14') == Decimal('1.32602739726027')
E        +  where Decimal('0E-14') = round(Decimal('0'), 14)
E        +  and   Decimal('1.32602739726027') = Decimal('1.32602739726027')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_dcfc_nl_365_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_dcfc_nl_365_leap_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_dcfc_nl_365_longer_period
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_dcfc_nl_365_longer_period_with_leap
============================== 4 failed in 0.08s ===============================
"""
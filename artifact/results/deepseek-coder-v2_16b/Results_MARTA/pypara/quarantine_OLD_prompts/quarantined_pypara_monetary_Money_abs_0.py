
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Money

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money_abs_0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_abs_defined_money ____________________________

    def test_abs_defined_money():
        with pytest.raises(NotImplementedError):
>           money = Money(ccy=Currency('USD'), qty=Decimal('-100.50'), dov=date.today())
E           TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money_abs_0.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money_abs_0.py::test_abs_defined_money
============================== 1 failed in 0.09s ===============================
"""

import pytest
from decimal import Decimal
from datetime import date
from pypara.currencies import Currencies
from pypara.exchange import FXRate

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate___invert___0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invert_zero_rate _____________________________

    def test_invert_zero_rate():
        ccy1 = Currencies["EUR"]
        ccy2 = Currencies["USD"]
        date_today = date.today()
        zero_value = Decimal("0")
        rate = FXRate(ccy1, ccy2, date_today, zero_value)
    
>       with pytest.raises(ZeroDivisionError):
E       Failed: DID NOT RAISE <class 'ZeroDivisionError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate___invert___0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate___invert___0.py::test_invert_zero_rate
============================== 1 failed in 0.08s ===============================
"""
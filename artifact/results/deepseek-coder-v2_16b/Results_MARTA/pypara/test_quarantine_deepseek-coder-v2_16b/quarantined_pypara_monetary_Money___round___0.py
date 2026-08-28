
# test_pypara_monetary_Money___round___.py
from pypara.monetary import Money, Currency, Decimal
import pytest


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money___round___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_rounding ______________________________

    def test_valid_rounding():
>       money = Money(ccy='USD', qty=Decimal('1234.5678'))
E       TypeError: Money() takes no arguments

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money___round___0.py:7: TypeError
____________________________ test_default_rounding _____________________________

    def test_default_rounding():
        undefined_money = Money()
>       rounded_undefined_money = undefined_money.__round__()

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money___round___0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/monetary.py:363: in __round__
    return self.round(ndigits or 0)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pypara.monetary.Money object at 0x7f5f96bafc40>, ndigits = 0

    @abstractmethod
    def round(self, ndigits: int = 0) -> "Money":
        """
        Rounds the quantity of the monetary value to ``ndigits`` by using ``HALF_EVEN`` method if *defined*, itself
        otherwise.
        """
>       raise NotImplementedError
E       NotImplementedError

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/monetary.py:153: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money___round___0.py::test_valid_rounding
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Money___round___0.py::test_default_rounding
============================== 2 failed in 0.11s ===============================
"""

import pytest
from pypara.monetary import SomeMoney



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_round_default ______________________________

    def test_round_default():
>       money_instance = SomeMoney(currency='USD', amount=100.567)
E       TypeError: SomeMoney.__new__() got an unexpected keyword argument 'currency'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py:6: TypeError
_____________________________ test_round_specified _____________________________

    def test_round_specified():
>       money_instance = SomeMoney(currency='USD', amount=100.567)
E       TypeError: SomeMoney.__new__() got an unexpected keyword argument 'currency'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py:12: TypeError
_____________________________ test_round_new_money _____________________________

    def test_round_new_money():
>       new_money = SomeMoney(currency='EUR', amount=150.789)
E       TypeError: SomeMoney.__new__() got an unexpected keyword argument 'currency'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py:18: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py::test_round_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py::test_round_specified
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomeMoney_round_0.py::test_round_new_money
============================== 3 failed in 0.11s ===============================
"""
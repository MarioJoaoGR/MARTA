
import pytest
from pypara.monetary import SomePrice


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_round_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_round_default ______________________________

    def test_round_default():
>       price = SomePrice(currency='USD', quantity=10.5, discount=2)
E       TypeError: SomePrice.__new__() got an unexpected keyword argument 'currency'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_round_1.py:6: TypeError
_____________________________ test_round_specified _____________________________

    def test_round_specified():
>       price = SomePrice(currency='USD', quantity=10.5, discount=2)
E       TypeError: SomePrice.__new__() got an unexpected keyword argument 'currency'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_round_1.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_round_1.py::test_round_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_round_1.py::test_round_specified
============================== 2 failed in 0.10s ===============================
"""

import pytest
from pypara.monetary import NoneMoney, Money



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_addition ______________________________

    def test_valid_addition():
        money1 = NoneMoney()
>       money2 = Money(10)
E       TypeError: Money() takes no arguments

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py:7: TypeError
____________________________ test_invalid_addition _____________________________

    def test_invalid_addition():
        money1 = NoneMoney()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py:14: Failed
__________________________ test_undefined_comparison ___________________________

    def test_undefined_comparison():
        money1 = NoneMoney()
        money2 = NoneMoney()
>       assert not (money1 == money2), "Expected two undefined money objects to be considered not equal"
E       AssertionError: Expected two undefined money objects to be considered not equal
E       assert not <pypara.monetary.NoneMoney object at 0x7f3b863cfa00> == <pypara.monetary.NoneMoney object at 0x7f3b863cfbe0>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py::test_valid_addition
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py::test_invalid_addition
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_add_0.py::test_undefined_comparison
============================== 3 failed in 0.09s ===============================
"""
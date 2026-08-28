
import pytest
from pypara.monetary import NonePrice, Price



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_addition ______________________________

    def test_valid_addition():
        price1 = NonePrice()
>       price2 = Price(50)
E       TypeError: Price() takes no arguments

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py:7: TypeError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py:13: Failed
____________________________ test_invalid_addition _____________________________

    def test_invalid_addition():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py::test_valid_addition
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_add_0.py::test_invalid_addition
============================== 3 failed in 0.08s ===============================
"""
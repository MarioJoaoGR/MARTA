
import pytest
from pypara.monetary import NonePrice, SomePrice, NoMoney



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_subtract ______________________________

    def test_valid_subtract():
>       price1 = SomePrice(value=100)
E       TypeError: SomePrice.__new__() got an unexpected keyword argument 'value'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py:6: TypeError
___________________________ test_edge_case_subtract ____________________________

    def test_edge_case_subtract():
>       price1 = SomePrice(value=100)
E       TypeError: SomePrice.__new__() got an unexpected keyword argument 'value'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py:13: TypeError
____________________________ test_invalid_subtract _____________________________

    def test_invalid_subtract():
        price1 = NonePrice()
        price2 = NonePrice()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py::test_valid_subtract
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py::test_edge_case_subtract
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_subtract_1.py::test_invalid_subtract
============================== 3 failed in 0.07s ===============================
"""

import pytest
from pypara.monetary import NonePrice, NoMoney


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_times_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_noneprice_arithmetic ___________________________

    def test_noneprice_arithmetic():
        none_price = NonePrice()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_times_2.py:7: Failed
_____________________________ test_noneprice_times _____________________________

    def test_noneprice_times():
        none_price = NonePrice()
        result = none_price.times(3)
>       assert isinstance(result, NoMoney), "Expected times(3) to return an instance of NoMoney"
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_times_2.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_times_2.py::test_noneprice_arithmetic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_times_2.py::test_noneprice_times
============================== 2 failed in 0.12s ===============================
"""
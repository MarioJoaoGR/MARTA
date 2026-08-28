
import pytest
from pypara.monetary import NoneMoney


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_with_dov_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_edge_case_arithmetic_operations _____________________

    def test_edge_case_arithmetic_operations():
        none_money = NoneMoney()
    
        # Addition with numeric value should raise TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_with_dov_1.py:9: Failed
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        none_money = NoneMoney()
    
        # Adding a numeric value to NoneMoney should raise TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_with_dov_1.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_with_dov_1.py::test_edge_case_arithmetic_operations
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_with_dov_1.py::test_invalid_input_error_handling
============================== 2 failed in 0.08s ===============================
"""
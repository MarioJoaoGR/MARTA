
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

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_lte_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        nm = NoneMoney()
        comparison_obj = None
        with pytest.raises(TypeError):
>           assert nm == comparison_obj, "Expected TypeError when comparing NoneMoney to None"
E           AssertionError: Expected TypeError when comparing NoneMoney to None
E           assert <pypara.monetary.NoneMoney object at 0x7f4a3f707e40> == None

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_lte_0.py:9: AssertionError
___________________________ test_invalid_comparison ____________________________

    def test_invalid_comparison():
        nm = NoneMoney()
        invalid_obj = 'string'
        with pytest.raises(TypeError):
>           assert nm == invalid_obj, "Expected TypeError when comparing NoneMoney to a string"
E           AssertionError: Expected TypeError when comparing NoneMoney to a string
E           assert <pypara.monetary.NoneMoney object at 0x7f4a3f707920> == 'string'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_lte_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_lte_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_lte_0.py::test_invalid_comparison
============================== 2 failed in 0.07s ===============================
"""

import pytest
from pymonet.immutable_list import ImmutableList

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_concatenation ___________________________

    def test_empty_concatenation():
        non_empty_list = ImmutableList(head=1)
        empty_list = ImmutableList(is_empty=True)
    
        concatenated_list = non_empty_list.__add__(empty_list)
    
>       assert concatenated_list.to_list() == [1]
E       assert [1, None] == [1]
E         
E         Left contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py::test_empty_concatenation
============================== 1 failed in 0.06s ===============================
"""
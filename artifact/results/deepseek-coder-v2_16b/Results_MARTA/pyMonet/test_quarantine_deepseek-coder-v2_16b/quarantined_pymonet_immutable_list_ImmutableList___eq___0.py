
import pytest
from pymonet.immutable_list import ImmutableList

# Test valid case where an empty list is created and compared to an actual empty list

# Test error case where a comparison with a non-immutable list raises TypeError
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_empty_list __________________________

    def test_valid_case_empty_list():
        my_list = ImmutableList(is_empty=True)
>       assert my_list.to_list() == []
E       assert [None] == []
E         
E         Left contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py:8: AssertionError
______________________ test_error_case_invalid_comparison ______________________

    def test_error_case_invalid_comparison():
        list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
        non_immutable_list = []
        with pytest.raises(TypeError):
>           assert list1 == non_immutable_list
E           assert <pymonet.immutable_list.ImmutableList object at 0x7f8009d58070> == []

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py::test_valid_case_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py::test_error_case_invalid_comparison
============================== 2 failed in 0.06s ===============================
"""
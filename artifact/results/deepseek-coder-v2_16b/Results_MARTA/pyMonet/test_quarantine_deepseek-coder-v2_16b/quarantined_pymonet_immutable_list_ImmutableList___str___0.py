
import pytest
from pymonet.immutable_list import ImmutableList

# Test valid case where an empty list is created

# Test edge case where the input is None

# Test invalid case where appending to an ImmutableList raises AttributeError
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_empty_list __________________________

    def test_valid_case_empty_list():
        my_list = ImmutableList(is_empty=True)
>       assert my_list.to_list() == []
E       assert [None] == []
E         
E         Left contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py:8: AssertionError
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
        immutable_list = ImmutableList(head=None, tail=ImmutableList(head=None))
>       assert immutable_list.to_list() == [None]
E       assert [None, None] == [None]
E         
E         Left contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py:13: AssertionError
___________________________ test_invalid_case_append ___________________________

    def test_invalid_case_append():
        my_list = ImmutableList(head=1)
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py::test_valid_case_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py::test_edge_case_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___str___0.py::test_invalid_case_append
============================== 3 failed in 0.06s ===============================
"""
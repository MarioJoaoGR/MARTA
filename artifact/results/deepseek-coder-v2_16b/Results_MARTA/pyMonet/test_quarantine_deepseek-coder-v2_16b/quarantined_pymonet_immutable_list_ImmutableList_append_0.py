
import pytest
from pymonet.immutable_list import ImmutableList

# Test edge case where ImmutableList is initially empty and appending an element

# Test case where appending to an invalid type raises a TypeError
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_edge_case_empty_append __________________________

    def test_edge_case_empty_append():
        my_list = ImmutableList(is_empty=True)
        updated_list = my_list.append(1)
        assert isinstance(updated_list, ImmutableList)
>       assert updated_list.to_list() == [1]
E       assert [None, 1] == [1]
E         
E         At index 0 diff: None != 1
E         Left contains one more item: 1
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_0.py:10: AssertionError
_____________________________ test_invalid_append ______________________________

    def test_invalid_append():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_0.py::test_edge_case_empty_append
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_0.py::test_invalid_append
============================== 2 failed in 0.06s ===============================
"""
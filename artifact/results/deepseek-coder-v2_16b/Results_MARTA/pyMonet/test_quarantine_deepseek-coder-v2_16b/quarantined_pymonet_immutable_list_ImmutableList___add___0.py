
import pytest
from pymonet.immutable_list import ImmutableList

# Test empty concatenation scenario

# Test concatenation with an empty list scenario
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_empty_concatenation ___________________________

    def test_empty_concatenation():
        list1 = ImmutableList(is_empty=True)
        list2 = ImmutableList(head=3, tail=ImmutableList(head=4))
        concatenated_list = list1.__add__(list2)
>       assert concatenated_list.to_list() == [3, 4]
E       assert [None, 3, 4] == [3, 4]
E         
E         At index 0 diff: None != 3
E         Left contains one more item: 4
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py:10: AssertionError
________________________ test_concatenation_with_empty _________________________

    def test_concatenation_with_empty():
        list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
        list2 = ImmutableList(is_empty=True)
        concatenated_list = list1.__add__(list2)
>       assert concatenated_list.to_list() == [1, 2]
E       assert [1, 2, None] == [1, 2]
E         
E         Left contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py::test_empty_concatenation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___add___0.py::test_concatenation_with_empty
============================== 2 failed in 0.06s ===============================
"""
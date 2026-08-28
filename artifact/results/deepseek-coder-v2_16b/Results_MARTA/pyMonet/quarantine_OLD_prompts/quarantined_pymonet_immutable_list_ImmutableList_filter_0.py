
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

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_filter_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
        my_list = ImmutableList(head=1, tail=sub_list)
    
        def is_even(n):
            return n % 2 == 0
    
        filtered_list = my_list.filter(is_even)
        assert isinstance(filtered_list, ImmutableList), "Filtered list should be an instance of ImmutableList"
        assert filtered_list.head == 2, "The head of the filtered list should be 2"
        assert isinstance(filtered_list.tail, ImmutableList), "The tail of the filtered list should be an instance of ImmutableList"
>       assert filtered_list.tail.head == 3, "The head of the tail of the filtered list should be 3"
E       AssertionError: The head of the tail of the filtered list should be 3
E       assert None == 3
E        +  where None = <pymonet.immutable_list.ImmutableList object at 0x7f1f1863b1c0>.head
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7f1f1863b1c0> = <pymonet.immutable_list.ImmutableList object at 0x7f1f1863b100>.tail

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_filter_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_filter_0.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
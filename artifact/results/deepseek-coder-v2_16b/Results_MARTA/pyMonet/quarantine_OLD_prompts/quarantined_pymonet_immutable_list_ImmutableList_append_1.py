
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        my_list = ImmutableList(is_empty=True)
        updated_list = my_list.append(1)
        assert isinstance(updated_list, ImmutableList)
>       assert updated_list.head == 1
E       assert None == 1
E        +  where None = <pymonet.immutable_list.ImmutableList object at 0x7f823ec7c1f0>.head

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_1.py:9: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        my_empty_list = ImmutableList(is_empty=True)
        updated_list = my_empty_list.append(None)
        assert isinstance(updated_list, ImmutableList)
        assert updated_list.head is None
>       assert updated_list.tail is None
E       assert <pymonet.immutable_list.ImmutableList object at 0x7f823ec95fc0> is None
E        +  where <pymonet.immutable_list.ImmutableList object at 0x7f823ec95fc0> = <pymonet.immutable_list.ImmutableList object at 0x7f823ec95810>.tail

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_1.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_append_1.py::test_edge_cases
============================== 2 failed in 0.07s ===============================
"""
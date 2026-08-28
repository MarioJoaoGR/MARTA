
import pytest
from unittest.mock import patch
from pymonet.immutable_list import ImmutableList



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            my_list = ImmutableList.of(1, 2, 3)
>           assert my_list.head == 1
E           AttributeError: 'ImmutableList' object has no attribute 'head'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py:9: AttributeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            # Test with None as head
            my_list = ImmutableList.of(None)
>           assert my_list.head is None
E           AttributeError: 'ImmutableList' object has no attribute 'head'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py:17: AttributeError
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
>           my_list = ImmutableList.of()
E           TypeError: ImmutableList.of() missing 1 required positional argument: 'head'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py:23: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_of_1.py::test_empty_list
============================== 3 failed in 0.99s ===============================
"""
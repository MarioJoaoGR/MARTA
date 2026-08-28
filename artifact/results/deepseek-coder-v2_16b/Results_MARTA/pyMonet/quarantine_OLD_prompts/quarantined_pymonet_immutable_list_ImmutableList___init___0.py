
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

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_create_empty_list ____________________________

    def test_create_empty_list():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            my_list = ImmutableList(is_empty=True)
>           assert my_list.is_empty is True
E           AttributeError: 'ImmutableList' object has no attribute 'is_empty'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py:9: AttributeError
_______________________ test_create_single_element_list ________________________

    def test_create_single_element_list():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            my_list = ImmutableList(head=1)
>           assert my_list.is_empty is False
E           AttributeError: 'ImmutableList' object has no attribute 'is_empty'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py:14: AttributeError
________________________ test_create_multi_element_list ________________________

    def test_create_multi_element_list():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
            my_list = ImmutableList(head=1, tail=sub_list)
>           assert my_list.is_empty is False
E           AttributeError: 'ImmutableList' object has no attribute 'is_empty'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py:20: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py::test_create_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py::test_create_single_element_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___init___0.py::test_create_multi_element_list
============================== 3 failed in 0.13s ===============================
"""
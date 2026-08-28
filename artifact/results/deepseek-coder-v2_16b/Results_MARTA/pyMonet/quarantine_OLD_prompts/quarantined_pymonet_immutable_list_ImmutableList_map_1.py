
import pytest
from pymonet.immutable_list import ImmutableList
from unittest.mock import patch


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    
        def square(x):
            return x * x
    
        with patch('pymonet.immutable_list.ImmutableList.map', lambda self, fn: [fn(self.head), *self.tail.map(fn)] if not self.is_empty else []) as mock_map:
>           mapped_list = my_list.map(square)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py:12: in <lambda>
    with patch('pymonet.immutable_list.ImmutableList.map', lambda self, fn: [fn(self.head), *self.tail.map(fn)] if not self.is_empty else []) as mock_map:
/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py:12: in <lambda>
    with patch('pymonet.immutable_list.ImmutableList.map', lambda self, fn: [fn(self.head), *self.tail.map(fn)] if not self.is_empty else []) as mock_map:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.immutable_list.ImmutableList object at 0x7f3e22e8e050>
fn = <function test_valid_input.<locals>.square at 0x7f3e22e21ea0>

>   with patch('pymonet.immutable_list.ImmutableList.map', lambda self, fn: [fn(self.head), *self.tail.map(fn)] if not self.is_empty else []) as mock_map:
E   AttributeError: 'NoneType' object has no attribute 'map'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py:12: AttributeError
__________________________ test_edge_case_empty_list ___________________________

    def test_edge_case_empty_list():
        my_list = ImmutableList(is_empty=True)
    
        def add_one(x):
            return x + 1
    
        with patch('pymonet.immutable_list.ImmutableList.map', lambda self, fn: [] if self.is_empty else [fn(self.head), *self.tail.map(fn)]):
            mapped_list = my_list.map(add_one)
>           assert mapped_list == ImmutableList(is_empty=True)
E           assert [] == <pymonet.immutable_list.ImmutableList object at 0x7f3e22e8fdc0>
E            +  where <pymonet.immutable_list.ImmutableList object at 0x7f3e22e8fdc0> = ImmutableList(is_empty=True)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_map_1.py::test_edge_case_empty_list
============================== 2 failed in 0.06s ===============================
"""
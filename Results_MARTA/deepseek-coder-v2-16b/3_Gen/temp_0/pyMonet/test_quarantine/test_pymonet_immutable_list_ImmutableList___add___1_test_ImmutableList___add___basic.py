
import pytest
from pymonet.immutable_list import ImmutableList

def test_ImmutableList___add___basic():
    empty_list = ImmutableList()
    list_with_one_element = ImmutableList(head=1)
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))

    concatenated_list = list_with_one_element + list_with_multiple_elements

    assert isinstance(concatenated_list, ImmutableList), "Concatenation result should be an instance of ImmutableList"
    assert concatenated_list.head == 1, "Head of the concatenated list should be 1"
    assert isinstance(concatenated_list.tail, ImmutableList), "Tail of the concatenated list should be an instance of ImmutableList"
    assert concatenated_list.tail.head == 2, "Second element of the concatenated list should be 2"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_ImmutableList___add___basic.py F [100%]

=================================== FAILURES ===================================
_______________________ test_ImmutableList___add___basic _______________________

    def test_ImmutableList___add___basic():
        empty_list = ImmutableList()
        list_with_one_element = ImmutableList(head=1)
        list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    
        concatenated_list = list_with_one_element + list_with_multiple_elements
    
        assert isinstance(concatenated_list, ImmutableList), "Concatenation result should be an instance of ImmutableList"
        assert concatenated_list.head == 1, "Head of the concatenated list should be 1"
        assert isinstance(concatenated_list.tail, ImmutableList), "Tail of the concatenated list should be an instance of ImmutableList"
>       assert concatenated_list.tail.head == 2, "Second element of the concatenated list should be 2"
E       AssertionError: Second element of the concatenated list should be 2
E       assert 1 == 2
E        +  where 1 = <pymonet.immutable_list.ImmutableList object at 0x7f5a672e9490>.head
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7f5a672e9490> = <pymonet.immutable_list.ImmutableList object at 0x7f5a672e9550>.tail

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_ImmutableList___add___basic.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_ImmutableList___add___basic.py::test_ImmutableList___add___basic
============================== 1 failed in 0.08s ===============================
"""
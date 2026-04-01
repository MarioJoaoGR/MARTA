
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    empty_list = ImmutableList()
    
    # Test appending to an empty list
    new_empty_list = empty_list.append(None)
    assert new_empty_list.is_empty is False
    assert new_empty_list.head is None
    assert isinstance(new_empty_list.tail, ImmutableList) and new_empty_list.tail.is_empty

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        empty_list = ImmutableList()
    
        # Test appending to an empty list
        new_empty_list = empty_list.append(None)
        assert new_empty_list.is_empty is False
        assert new_empty_list.head is None
>       assert isinstance(new_empty_list.tail, ImmutableList) and new_empty_list.tail.is_empty
E       assert (True and False)
E        +  where True = isinstance(<pymonet.immutable_list.ImmutableList object at 0x7ff22e726350>, ImmutableList)
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7ff22e726350> = <pymonet.immutable_list.ImmutableList object at 0x7ff22d6a3f90>.tail
E        +  and   False = <pymonet.immutable_list.ImmutableList object at 0x7ff22e726350>.is_empty
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7ff22e726350> = <pymonet.immutable_list.ImmutableList object at 0x7ff22d6a3f90>.tail

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0_test_edge_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""
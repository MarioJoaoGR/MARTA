
from pymonet.immutable_list import ImmutableList

def test_valid_init():
    # Creating an empty instance of ImmutableList
    empty_list = ImmutableList.empty()
    
    # Asserting that the created list is indeed empty
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail == empty_list  # The tail should be a reference to itself for an empty list

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___init___1_test_valid_init.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_init ________________________________

    def test_valid_init():
        # Creating an empty instance of ImmutableList
        empty_list = ImmutableList.empty()
    
        # Asserting that the created list is indeed empty
        assert empty_list.is_empty is True
        assert empty_list.head is None
>       assert empty_list.tail == empty_list  # The tail should be a reference to itself for an empty list
E       assert None == <pymonet.immutable_list.ImmutableList object at 0x7f51b3b09350>
E        +  where None = <pymonet.immutable_list.ImmutableList object at 0x7f51b3b09350>.tail

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___init___1_test_valid_init.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___init___1_test_valid_init.py::test_valid_init
============================== 1 failed in 0.06s ===============================
"""
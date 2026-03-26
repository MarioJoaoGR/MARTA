
import pytest
from superstring import SuperString

def test_to_printable():
    s = SuperString("Hello, World!")
    
    # Test default case where start_index and end_index are not provided
    assert s.to_printable() == "Hello, World!"
    
    # Test specific substring extraction
    assert s.to_printable(7, 12) == "World"
    
    # Test edge cases with invalid indices
    with pytest.raises(IndexError):
        s.to_printable(-1)
    with pytest.raises(IndexError):
        s.to_printable(0, len("Hello, World!") + 1)
        
    # Test negative indices
    assert s.to_printable(-6) == "World!"
    assert s.to_printable(-6, -1) == "World"
    
    # Test start_index greater than end_index
    with pytest.raises(ValueError):
        s.to_printable(12, 7)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_to_printable _______________________________

    def test_to_printable():
        s = SuperString("Hello, World!")
    
        # Test default case where start_index and end_index are not provided
        assert s.to_printable() == "Hello, World!"
    
        # Test specific substring extraction
        assert s.to_printable(7, 12) == "World"
    
        # Test edge cases with invalid indices
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_1_test_edge_cases.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_1_test_edge_cases.py::test_to_printable
============================== 1 failed in 0.06s ===============================
"""
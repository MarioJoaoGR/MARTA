
import pytest
from superstring.superstring import SuperString, SuperStringUpper

def test_edge_cases():
    s = SuperStringUpper(SuperString("Hello, World!"))
    
    # Test with None indices
    assert s.to_printable() == "HELLO, WORLD!"
    assert s.to_printable(None, None) == "HELLO, WORLD!"
    
    # Test with valid start and end indices
    assert s.to_printable(7, 12) == "WORLD"
    
    # Test with only start index provided
    assert s.to_printable(7, None) == "WORLD!"
    
    # Test with only end index provided
    assert s.to_printable(None, 5) == "HELLO"
    
    # Test with invalid indices (start > end)
    with pytest.raises(IndexError):
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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        s = SuperStringUpper(SuperString("Hello, World!"))
    
        # Test with None indices
        assert s.to_printable() == "HELLO, WORLD!"
        assert s.to_printable(None, None) == "HELLO, WORLD!"
    
        # Test with valid start and end indices
        assert s.to_printable(7, 12) == "WORLD"
    
        # Test with only start index provided
        assert s.to_printable(7, None) == "WORLD!"
    
        # Test with only end index provided
        assert s.to_printable(None, 5) == "HELLO"
    
        # Test with invalid indices (start > end)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_1_test_edge_cases.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.04s ===============================
"""
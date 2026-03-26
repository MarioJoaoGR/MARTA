
import pytest
from superstring import SuperString

def test_invalid_input():
    superstring = SuperString('Hello, World!')
    
    # Test when start_index is out of bounds
    with pytest.raises(IndexError):
        superstring.substring(14)  # Index out of bounds for the given string length
        
    # Test when end_index is before start_index
    with pytest.raises(ValueError):
        superstring.substring(7, 5)  # end_index should not be less than start_index
        
    # Test when index in character_at is out of bounds
    with pytest.raises(IndexError):
        superstring.character_at(13)  # Index out of bounds for the given string length

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        superstring = SuperString('Hello, World!')
    
        # Test when start_index is out of bounds
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_2_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""

import pytest
from flutes.fs import remove_suffix

def test_invalid_input():
    # Test case for invalid input type (non-string)
    with pytest.raises(TypeError):
        remove_suffix(42, "invalid")  # s is an integer
    
    # Test case for invalid suffix type (non-string)
    with pytest.raises(TypeError):
        remove_suffix("https://github.com/huzecong", 42)  # suffix is an integer
    
    # Test case for fully_match type (non-boolean)
    with pytest.raises(TypeError):
        remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=None)  # fully_match is not a boolean

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test case for invalid input type (non-string)
        with pytest.raises(TypeError):
            remove_suffix(42, "invalid")  # s is an integer
    
        # Test case for invalid suffix type (non-string)
        with pytest.raises(TypeError):
            remove_suffix("https://github.com/huzecong", 42)  # suffix is an integer
    
        # Test case for fully_match type (non-boolean)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_input.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""

import pytest
from flutes.fs import remove_prefix

def test_invalid_input_error_handling():
    # Test case for invalid input type (non-string)
    with pytest.raises(TypeError):
        remove_prefix(123, "https://")  # Expecting TypeError
    
    # Test case for invalid prefix type (non-string)
    with pytest.raises(TypeError):
        remove_prefix("https://github.com/huzecong/flutes", 123)  # Expecting TypeError
    
    # Test case for fully_match being of incorrect type (non-boolean)
    with pytest.raises(TypeError):
        remove_prefix("https://github.com/huzecong/flutes", "https://", fully_match="not a bool")  # Expecting TypeError

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

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        # Test case for invalid input type (non-string)
        with pytest.raises(TypeError):
            remove_prefix(123, "https://")  # Expecting TypeError
    
        # Test case for invalid prefix type (non-string)
        with pytest.raises(TypeError):
            remove_prefix("https://github.com/huzecong/flutes", 123)  # Expecting TypeError
    
        # Test case for fully_match being of incorrect type (non-boolean)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_invalid_input_error_handling.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.09s ===============================
"""
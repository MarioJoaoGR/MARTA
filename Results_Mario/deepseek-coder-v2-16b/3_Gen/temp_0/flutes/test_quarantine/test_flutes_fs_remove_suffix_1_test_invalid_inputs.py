
import pytest
from flutes.fs import remove_suffix

def test_invalid_inputs():
    # Test with invalid inputs
    with pytest.raises(TypeError):
        remove_suffix(123, "suffix")  # s is not a string
    
    with pytest.raises(TypeError):
        remove_suffix("string", 456)  # suffix is not a string
    
    with pytest.raises(TypeError):
        remove_suffix("string", "suffix", fully_match=123)  # fully_match is not a boolean
    
    with pytest.raises(ValueError):
        remove_suffix("", "")  # Both s and suffix are empty strings

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with invalid inputs
        with pytest.raises(TypeError):
            remove_suffix(123, "suffix")  # s is not a string
    
        with pytest.raises(TypeError):
            remove_suffix("string", 456)  # suffix is not a string
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================

"""
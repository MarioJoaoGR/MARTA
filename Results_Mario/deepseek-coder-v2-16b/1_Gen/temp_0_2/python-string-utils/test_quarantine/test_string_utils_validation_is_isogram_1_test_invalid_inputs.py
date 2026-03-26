
import pytest
from string_utils.validation import is_isogram

def test_invalid_inputs():
    # Test with None input
    with pytest.raises(TypeError):
        assert not is_isogram(None)
    
    # Test with empty string
    with pytest.raises(TypeError):
        assert not is_isogram("")
    
    # Test with a single space
    with pytest.raises(TypeError):
        assert not is_isogram(" ")
    
    # Test with a string containing only spaces and hyphens
    with pytest.raises(TypeError):
        assert not is_isogram(" - - ")
    
    # Test with a non-string type (e.g., integer)
    with pytest.raises(TypeError):
        assert not is_isogram(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with None input
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_1_test_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""
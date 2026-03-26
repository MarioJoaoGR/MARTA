
import pytest
from flutes.fs import readable_size

def test_invalid_input():
    # Test case for invalid input types
    with pytest.raises(TypeError):
        readable_size("1024")  # String instead of float or int
    
    # Test case for negative size values
    with pytest.raises(ValueError):
        readable_size(-1)  # Negative value should raise ValueError

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

flutes/Test4DT_tests/test_flutes_fs_readable_size_7_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test case for invalid input types
        with pytest.raises(TypeError):
            readable_size("1024")  # String instead of float or int
    
        # Test case for negative size values
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_readable_size_7_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_7_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""
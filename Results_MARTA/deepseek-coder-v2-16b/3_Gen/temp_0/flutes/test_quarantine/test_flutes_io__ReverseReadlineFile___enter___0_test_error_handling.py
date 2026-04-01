
import pytest
from flutes.io import _ReverseReadlineFile

def test_invalid_inputs():
    # Test with a non-file-like object
    gen = (line[::-1] for line in ["Hello, world!"])
    with pytest.raises(TypeError):
        _ReverseReadlineFile("not_a_file_object", gen)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with a non-file-like object
        gen = (line[::-1] for line in ["Hello, world!"])
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_error_handling.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_error_handling.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""
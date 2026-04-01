
import pytest
from dataclasses_json.utils import _isinstance_safe

def test_invalid_inputs():
    # Test with None as input
    assert not _isinstance_safe(None, int)
    
    # Test with invalid type (should raise an exception and return False)
    with pytest.raises(TypeError):
        _isinstance_safe("hello", str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_5_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with None as input
        assert not _isinstance_safe(None, int)
    
        # Test with invalid type (should raise an exception and return False)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_5_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_5_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""
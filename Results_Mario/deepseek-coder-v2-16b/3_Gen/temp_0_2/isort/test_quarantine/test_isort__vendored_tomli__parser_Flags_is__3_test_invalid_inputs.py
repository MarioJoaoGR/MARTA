
import pytest
from isort._vendored.tomli._parser import Flags

def test_invalid_inputs():
    flags = Flags()
    
    # Test with invalid key type
    with pytest.raises(TypeError):
        flags.is_(123, 0)
    
    # Test with invalid flag value
    with pytest.raises(ValueError):
        flags.is_("key", "invalid_flag")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__3_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        flags = Flags()
    
        # Test with invalid key type
        with pytest.raises(TypeError):
            flags.is_(123, 0)
    
        # Test with invalid flag value
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__3_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__3_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.15s ===============================
"""
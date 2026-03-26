
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_error_handling():
    maybe_instance = Maybe(None, True)  # Creating an instance of Maybe with is_nothing set to True
    
    with pytest.raises(TypeError):
        maybe_instance.to_validation()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_2_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        maybe_instance = Maybe(None, True)  # Creating an instance of Maybe with is_nothing set to True
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_2_test_error_handling.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_2_test_error_handling.py::test_error_handling
============================== 1 failed in 0.08s ===============================
"""
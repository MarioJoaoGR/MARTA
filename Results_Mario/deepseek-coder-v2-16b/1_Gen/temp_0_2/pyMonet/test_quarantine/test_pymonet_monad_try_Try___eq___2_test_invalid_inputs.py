
import pytest
from pymonet.monad_try import Try

def test_invalid_inputs():
    with pytest.raises(TypeError):
        invalid_input_1 = Try('Invalid', 'True')  # Invalid type for value
        assert not invalid_input_1.is_success

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

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___eq___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            invalid_input_1 = Try('Invalid', 'True')  # Invalid type for value
>           assert not invalid_input_1.is_success
E           AssertionError: assert not 'True'
E            +  where 'True' = <pymonet.monad_try.Try object at 0x7f2b4a15ba10>.is_success

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___eq___2_test_invalid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___eq___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""
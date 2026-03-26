
import pytest
from flutes.exception import log_exception
from logging import Logger, StreamHandler
from unittest.mock import patch

def mock_log(*args, **kwargs):
    pass

log_exception = lambda e, *args, **kwargs: mock_log(e, *args, **kwargs)

@pytest.mark.parametrize("invalid_input", [123, None, "string", b"bytes"])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        log_exception(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [123, None, "string", b"bytes"])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py:14: Failed
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [123, None, "string", b"bytes"])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py:14: Failed
_________________________ test_invalid_inputs[string] __________________________

invalid_input = 'string'

    @pytest.mark.parametrize("invalid_input", [123, None, "string", b"bytes"])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py:14: Failed
__________________________ test_invalid_inputs[bytes] __________________________

invalid_input = b'bytes'

    @pytest.mark.parametrize("invalid_input", [123, None, "string", b"bytes"])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py::test_invalid_inputs[123]
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py::test_invalid_inputs[string]
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_3_test_invalid_inputs.py::test_invalid_inputs[bytes]
============================== 4 failed in 0.10s ===============================

"""
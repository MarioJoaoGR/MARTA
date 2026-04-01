
import pytest
from flutes.io import progress_open
import io

@pytest.mark.parametrize("mode", ["invalid", "r", "rb"])
def test_invalid_inputs(mode):
    with pytest.raises(ValueError):
        if mode == "invalid":
            with progress_open('dummy_path', mode=mode) as f:
                pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_inputs.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_inputs[r] ____________________________

mode = 'r'

    @pytest.mark.parametrize("mode", ["invalid", "r", "rb"])
    def test_invalid_inputs(mode):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_inputs.py:8: Failed
___________________________ test_invalid_inputs[rb] ____________________________

mode = 'rb'

    @pytest.mark.parametrize("mode", ["invalid", "r", "rb"])
    def test_invalid_inputs(mode):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_inputs.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_inputs.py::test_invalid_inputs[r]
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_inputs.py::test_invalid_inputs[rb]
========================= 2 failed, 1 passed in 0.11s ==========================
"""
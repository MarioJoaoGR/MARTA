
import pytest
from codetiming._timer import Timer

@pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        Timer(name=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py:7: Failed
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py:7: Failed
_________________________ test_invalid_inputs[string] __________________________

invalid_input = 'string'

    @pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py:7: Failed
_____________________ test_invalid_inputs[invalid_input3] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py:7: Failed
_____________________ test_invalid_inputs[invalid_input4] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [None, 123, "string", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py::test_invalid_inputs[123]
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py::test_invalid_inputs[string]
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py::test_invalid_inputs[invalid_input3]
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_invalid_inputs.py::test_invalid_inputs[invalid_input4]
============================== 5 failed in 0.02s ===============================
"""
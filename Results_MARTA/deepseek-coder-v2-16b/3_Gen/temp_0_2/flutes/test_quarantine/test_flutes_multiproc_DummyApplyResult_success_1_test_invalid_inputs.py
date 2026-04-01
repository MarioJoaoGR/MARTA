
import pytest
from flutes.multiproc import DummyApplyResult

def dummy_apply_result(value):
    return DummyApplyResult(value)

@pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        dummy_apply_result(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py:10: Failed
____________________________ test_invalid_inputs[0] ____________________________

invalid_input = 0

    @pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py:10: Failed
____________________________ test_invalid_inputs[] _____________________________

invalid_input = ''

    @pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py:10: Failed
_____________________ test_invalid_inputs[invalid_input3] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py:10: Failed
_____________________ test_invalid_inputs[invalid_input4] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [None, 0, "", [], {}])
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py::test_invalid_inputs[0]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py::test_invalid_inputs[]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py::test_invalid_inputs[invalid_input3]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_invalid_inputs.py::test_invalid_inputs[invalid_input4]
============================== 5 failed in 0.10s ===============================
"""
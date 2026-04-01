
import pytest
import sys
import os
from flutes.io import shut_up

@pytest.mark.parametrize("stderr, stdout", [
    (None, False),  # Invalid type for stderr
    (True, None),   # Invalid type for stdout
    ("string", False),  # Invalid type for stderr
    (True, "string"),   # Invalid type for stdout
])
def test_invalid_input(stderr, stdout):
    with pytest.raises(TypeError):
        shut_up(stderr=stderr, stdout=stdout)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py FFFF [100%]

=================================== FAILURES ===================================
________________________ test_invalid_input[None-False] ________________________

stderr = None, stdout = False

    @pytest.mark.parametrize("stderr, stdout", [
        (None, False),  # Invalid type for stderr
        (True, None),   # Invalid type for stdout
        ("string", False),  # Invalid type for stderr
        (True, "string"),   # Invalid type for stdout
    ])
    def test_invalid_input(stderr, stdout):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py:14: Failed
________________________ test_invalid_input[True-None] _________________________

stderr = True, stdout = None

    @pytest.mark.parametrize("stderr, stdout", [
        (None, False),  # Invalid type for stderr
        (True, None),   # Invalid type for stdout
        ("string", False),  # Invalid type for stderr
        (True, "string"),   # Invalid type for stdout
    ])
    def test_invalid_input(stderr, stdout):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py:14: Failed
_______________________ test_invalid_input[string-False] _______________________

stderr = 'string', stdout = False

    @pytest.mark.parametrize("stderr, stdout", [
        (None, False),  # Invalid type for stderr
        (True, None),   # Invalid type for stdout
        ("string", False),  # Invalid type for stderr
        (True, "string"),   # Invalid type for stdout
    ])
    def test_invalid_input(stderr, stdout):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py:14: Failed
_______________________ test_invalid_input[True-string] ________________________

stderr = True, stdout = 'string'

    @pytest.mark.parametrize("stderr, stdout", [
        (None, False),  # Invalid type for stderr
        (True, None),   # Invalid type for stdout
        ("string", False),  # Invalid type for stderr
        (True, "string"),   # Invalid type for stdout
    ])
    def test_invalid_input(stderr, stdout):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py::test_invalid_input[None-False]
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py::test_invalid_input[True-None]
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py::test_invalid_input[string-False]
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_input.py::test_invalid_input[True-string]
============================== 4 failed in 0.11s ===============================
"""

import pytest
from sty import EightbitBg

def test_invalid_input():
    # Test that initializing with an invalid number raises a ValueError
    with pytest.raises(ValueError):
        EightbitBg(-1)  # Invalid negative number
        assert False, "Expected ValueError for invalid input"
    with pytest.raises(ValueError):
        EightbitBg(256)  # Invalid number larger than 255
        assert False, "Expected ValueError for invalid input"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that initializing with an invalid number raises a ValueError
        with pytest.raises(ValueError):
            EightbitBg(-1)  # Invalid negative number
>           assert False, "Expected ValueError for invalid input"
E           AssertionError: Expected ValueError for invalid input
E           assert False

sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_invalid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""
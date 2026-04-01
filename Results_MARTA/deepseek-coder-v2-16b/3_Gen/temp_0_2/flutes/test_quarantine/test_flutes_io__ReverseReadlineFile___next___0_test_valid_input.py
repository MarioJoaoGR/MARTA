
import pytest
from unittest.mock import MagicMock
from flutes.io import _ReverseReadlineFile

@pytest.fixture
def setup_reverse_readline():
    file_obj = MagicMock()
    gen = (line for line in ["Line1\n", "Line2\n", "Line3\n"])
    reverse_readline = _ReverseReadlineFile(file_obj, gen)
    return reverse_readline

def test_valid_input(setup_reverse_readline):
    reverse_readline = setup_reverse_readline
    assert next(reverse_readline) == "Line3\n"
    assert next(reverse_readline) == "Line2\n"
    assert next(reverse_readline) == "Line1\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7f7828704110>

    def test_valid_input(setup_reverse_readline):
        reverse_readline = setup_reverse_readline
>       assert next(reverse_readline) == "Line3\n"
E       AssertionError: assert 'Line1\n\n' == 'Line3\n'
E         
E         - Line3
E         ?     ^
E         + Line1
E         ?     ^
E         +

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""

import pytest
from unittest.mock import MagicMock
from flutes.io import _ReverseReadlineFile

@pytest.fixture
def setup_reverse_readline():
    fp = MagicMock()
    gen = (line[::-1] for line in ["Line1", "Line2", "Line3"])
    return _ReverseReadlineFile(fp, gen)

def test_error_handling(setup_reverse_readline):
    reverse_readline = setup_reverse_readline
    with pytest.raises(SystemExit):
        reverse_readline.__exit__(None, None, None)

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7f87b8c689d0>

    def test_error_handling(setup_reverse_readline):
        reverse_readline = setup_reverse_readline
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_handling.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_handling.py::test_error_handling
============================== 1 failed in 0.09s ===============================
"""
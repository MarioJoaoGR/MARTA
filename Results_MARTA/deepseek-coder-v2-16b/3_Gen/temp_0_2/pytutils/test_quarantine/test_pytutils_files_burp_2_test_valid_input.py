
import pytest
from io import StringIO
from pytutils.files import burp

def test_valid_input():
    # Test writing to a file
    result = StringIO()
    burp('example.txt', 'Hello, world!', allow_stdout=False)
    assert result.getvalue() == 'Hello, world!'

    # Test writing to stdout
    captured_output = StringIO()
    with pytest.raises(SystemExit):
        burp('-', 'Hello, world!', allow_stdout=True)
    assert captured_output.getvalue() == 'Hello, world!'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test writing to a file
        result = StringIO()
        burp('example.txt', 'Hello, world!', allow_stdout=False)
>       assert result.getvalue() == 'Hello, world!'
E       AssertionError: assert '' == 'Hello, world!'
E         
E         - Hello, world!

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""

import pytest
from pytutils.pretty import pp
import sys
import six
try:
    import pygments
except ImportError:
    pygments = None

@pytest.mark.skipif(pygments is None, reason="Pygments is not available")
def test_valid_input():
    # Mock the output file to capture the printed content
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    pp({'key': 'value'}, outfile=captured_output)
    assert captured_output.getvalue().strip() == "{'key': 'value'}"

    # Reset the output file to standard output
    sys.stdout = sys.__stdout__

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

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_valid_input.py F   [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    @pytest.mark.skipif(pygments is None, reason="Pygments is not available")
    def test_valid_input():
        # Mock the output file to capture the printed content
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
    
        pp({'key': 'value'}, outfile=captured_output)
>       assert captured_output.getvalue().strip() == "{'key': 'value'}"
E       assert '\x1b[38;2;24...242m}\x1b[39m' == "{'key': 'value'}"
E         
E         - {'key': 'value'}
E         + [38;2;248;248;242m{[39m[38;2;230;219;116m'[39m[38;2;230;219;116mkey[39m[38;2;230;219;116m'[39m[38;2;248;248;242m:[39m[38;2;248;248;242m [39m[38;2;230;219;116m'[39m[38;2;230;219;116mvalue[39m[38;2;230;219;116m'[39m[38;2;248;248;242m}[39m

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_valid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""
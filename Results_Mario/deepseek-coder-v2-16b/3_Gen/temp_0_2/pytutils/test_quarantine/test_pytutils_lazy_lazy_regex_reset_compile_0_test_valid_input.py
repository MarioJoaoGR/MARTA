
import re
from unittest.mock import patch, MagicMock
from pytutils.lazy.lazy_regex import _real_re_compile, reset_compile

def test_valid_input():
    # Save the original re.compile function
    original_re_compile = re.compile
    
    # Mocking _real_re_compile to be a dummy function
    with patch('pytutils.lazy.lazy_regex._real_re_compile', MagicMock()):
        reset_compile()
        
        # After resetting, the re.compile should point back to the original function
        assert re.compile == _real_re_compile

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_reset_compile_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Save the original re.compile function
        original_re_compile = re.compile
    
        # Mocking _real_re_compile to be a dummy function
        with patch('pytutils.lazy.lazy_regex._real_re_compile', MagicMock()):
            reset_compile()
    
            # After resetting, the re.compile should point back to the original function
>           assert re.compile == _real_re_compile
E           AssertionError: assert <MagicMock id='139655542287376'> == _real_re_compile
E            +  where <MagicMock id='139655542287376'> = re.compile

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_reset_compile_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_reset_compile_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""

import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_input():
    lazy_regex = LazyRegex(args=('^[a-zA-Z0-9]+$',), kwargs={'flags': re.IGNORECASE})
    
    # When the regex is accessed, it should be compiled with the given pattern and flags
    assert hasattr(lazy_regex, 'findall')  # This will trigger compilation
    
    # Now we can use the findall method to check if it works correctly
    result = lazy_regex.findall("Hello123")
    assert result == ['Hello', '123']

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        lazy_regex = LazyRegex(args=('^[a-zA-Z0-9]+$',), kwargs={'flags': re.IGNORECASE})
    
        # When the regex is accessed, it should be compiled with the given pattern and flags
        assert hasattr(lazy_regex, 'findall')  # This will trigger compilation
    
        # Now we can use the findall method to check if it works correctly
        result = lazy_regex.findall("Hello123")
>       assert result == ['Hello', '123']
E       AssertionError: assert ['Hello123'] == ['Hello', '123']
E         
E         At index 0 diff: 'Hello123' != 'Hello'
E         Right contains one more item: '123'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
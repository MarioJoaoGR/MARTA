
from pytutils.lazy.lazy_regex import LazyRegex, lazy_compile
import re

def test_valid_input():
    # Create a LazyRegex object with valid regex pattern and flags
    lazy_regex = lazy_compile(r'pattern', ignorecase=True)
    
    # Check if the _real_regex attribute is not None after creation, indicating it has been compiled
    assert hasattr(lazy_regex._real_regex, 'pattern')

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a LazyRegex object with valid regex pattern and flags
        lazy_regex = lazy_compile(r'pattern', ignorecase=True)
    
        # Check if the _real_regex attribute is not None after creation, indicating it has been compiled
>       assert hasattr(lazy_regex._real_regex, 'pattern')
E       AssertionError: assert False
E        +  where False = hasattr(None, 'pattern')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f863a644ca0>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""
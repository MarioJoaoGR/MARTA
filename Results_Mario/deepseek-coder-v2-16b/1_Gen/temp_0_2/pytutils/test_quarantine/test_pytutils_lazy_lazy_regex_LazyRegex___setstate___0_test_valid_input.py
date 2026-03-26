
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_input():
    # Test valid input with a regex pattern and flags
    lazy_regex = LazyRegex(r'hello', re.IGNORECASE)
    assert isinstance(lazy_regex._real_regex, re.Pattern), f"Expected _real_regex to be an instance of re.Pattern but got {type(lazy_regex._real_regex)}"

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test valid input with a regex pattern and flags
        lazy_regex = LazyRegex(r'hello', re.IGNORECASE)
>       assert isinstance(lazy_regex._real_regex, re.Pattern), f"Expected _real_regex to be an instance of re.Pattern but got {type(lazy_regex._real_regex)}"
E       AssertionError: Expected _real_regex to be an instance of re.Pattern but got <class 'NoneType'>
E       assert False
E        +  where False = isinstance(None, <class 're.Pattern'>)
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f5e6bc40280>._real_regex
E        +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___0_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""
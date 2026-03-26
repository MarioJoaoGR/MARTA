
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_input():
    lazy_regex = LazyRegex(r'hello', re.IGNORECASE)
    assert lazy_regex.match('Hello') is not None

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        lazy_regex = LazyRegex(r'hello', re.IGNORECASE)
>       assert lazy_regex.match('Hello') is not None

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_regex.py:159: in __getattr__
    self._compile_and_collapse()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f82f927c280>

    def _compile_and_collapse(self):
        """Actually compile the requested regex"""
>       self._real_regex = self._real_re_compile(*self._regex_args,
                                                 **self._regex_kwargs)
E       TypeError: pytutils.lazy.lazy_regex.LazyRegex._real_re_compile() argument after ** must be a mapping, not RegexFlag

pytutils/pytutils/lazy/lazy_regex.py:126: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""
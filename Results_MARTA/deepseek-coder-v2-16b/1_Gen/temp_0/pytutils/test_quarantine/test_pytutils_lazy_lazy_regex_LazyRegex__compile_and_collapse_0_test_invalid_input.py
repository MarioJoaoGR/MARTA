
import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_invalid_input():
    with pytest.raises(re.error):
        lazy_regex = LazyRegex()
        lazy_regex.findall("invalid input")

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(re.error):
            lazy_regex = LazyRegex()
>           lazy_regex.findall("invalid input")

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_regex.py:159: in __getattr__
    self._compile_and_collapse()
pytutils/pytutils/lazy/lazy_regex.py:126: in _compile_and_collapse
    self._real_regex = self._real_re_compile(*self._regex_args,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f75818c3370>, args = ()
kwargs = {}

    def _real_re_compile(self, *args, **kwargs):
        """Thunk over to the original re.compile"""
        try:
>           return _real_re_compile(*args, **kwargs)
E           TypeError: compile() missing 1 required positional argument: 'pattern'

pytutils/pytutils/lazy/lazy_regex.py:134: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""
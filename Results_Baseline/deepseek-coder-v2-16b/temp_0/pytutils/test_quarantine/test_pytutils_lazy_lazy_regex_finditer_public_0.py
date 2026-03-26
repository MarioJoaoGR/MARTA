
import pytest
from pytutils.lazy.lazy_regex import finditer_public
import re

# Test cases for finditer_public function

def test_basic_usage():
    result = finditer_public(r'\d+', '123abc456')
    matches = [match.group() for match in result]
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_finditer_public_0.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_lazyregex_instance ____________________________

    def test_lazyregex_instance():
        from pytutils.lazy.lazy_regex import LazyRegex
        lazy_pattern = LazyRegex(r'\d+')
>       result = finditer_public(lazy_pattern, '123abc456')

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_finditer_public_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_regex.py:204: in finditer_public
    return pattern.finditer(string)
pytutils/pytutils/lazy/lazy_regex.py:159: in __getattr__
    self._compile_and_collapse()
pytutils/pytutils/lazy/lazy_regex.py:126: in _compile_and_collapse
    self._real_regex = self._real_re_compile(*self._regex_args,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fa5cd137b50>
args = ('\\', 'd', '+'), kwargs = {}

    def _real_re_compile(self, *args, **kwargs):
        """Thunk over to the original re.compile"""
        try:
>           return _real_re_compile(*args, **kwargs)
E           TypeError: compile() takes from 1 to 2 positional arguments but 3 were given

pytutils/pytutils/lazy/lazy_regex.py:134: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_finditer_public_0.py::test_lazyregex_instance
========================= 1 failed, 1 passed in 0.06s ==========================
"""

import pytest
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern
import re

def test_invalid_input():
    with pytest.raises(InvalidPattern) as excinfo:
        lazy_regex = LazyRegex(args=("^[a-zA-Z0-9]+$",))
        # This should trigger the compilation and raise an InvalidPattern error since the pattern is invalid
        lazy_regex._real_re_compile()
    assert str(excinfo.value) == '"^[a-zA-Z0-9]+$" Invalid regular expression: nothing to repeat'

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(InvalidPattern) as excinfo:
            lazy_regex = LazyRegex(args=("^[a-zA-Z0-9]+$",))
            # This should trigger the compilation and raise an InvalidPattern error since the pattern is invalid
>           lazy_regex._real_re_compile()

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_1_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f747bd1f640>, args = ()
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
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""
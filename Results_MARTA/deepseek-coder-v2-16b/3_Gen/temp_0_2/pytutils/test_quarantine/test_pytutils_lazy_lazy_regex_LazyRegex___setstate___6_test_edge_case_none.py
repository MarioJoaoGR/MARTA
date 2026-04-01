
import re
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

@pytest.mark.parametrize("args, kwargs", [((None,), {'flags': re.IGNORECASE})])
def test_edge_case_none(args, kwargs):
    lazy_regex = LazyRegex(args=args, kwargs=kwargs)
    assert isinstance(lazy_regex._real_regex, type(re.compile(*args, **kwargs)))

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___6_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
______________________ test_edge_case_none[args0-kwargs0] ______________________

args = (None,), kwargs = {'flags': re.IGNORECASE}

    @pytest.mark.parametrize("args, kwargs", [((None,), {'flags': re.IGNORECASE})])
    def test_edge_case_none(args, kwargs):
        lazy_regex = LazyRegex(args=args, kwargs=kwargs)
>       assert isinstance(lazy_regex._real_regex, type(re.compile(*args, **kwargs)))

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___6_test_edge_case_none.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/re/__init__.py:227: in compile
    return _compile(pattern, flags)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

pattern = None, flags = 2

    def _compile(pattern, flags):
        # internal: compile pattern
        if isinstance(flags, RegexFlag):
            flags = flags.value
        try:
            return _cache[type(pattern), pattern, flags]
        except KeyError:
            pass
        if isinstance(pattern, Pattern):
            if flags:
                raise ValueError(
                    "cannot process flags argument with a compiled pattern")
            return pattern
        if not _compiler.isstring(pattern):
>           raise TypeError("first argument must be string or compiled pattern")
E           TypeError: first argument must be string or compiled pattern

/usr/local/lib/python3.11/re/__init__.py:286: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___6_test_edge_case_none.py::test_edge_case_none[args0-kwargs0]
============================== 1 failed in 0.08s ===============================
"""
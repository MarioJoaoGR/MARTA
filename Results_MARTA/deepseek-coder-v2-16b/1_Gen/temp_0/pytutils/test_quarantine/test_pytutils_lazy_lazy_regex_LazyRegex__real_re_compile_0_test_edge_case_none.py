
import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern

def test_edge_case_none():
    lazy_regex = LazyRegex(args=("pattern",), kwargs={"ignorecase": True})
    with pytest.raises(InvalidPattern):
        assert isinstance(lazy_regex._real_regex, re.Pattern)

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        lazy_regex = LazyRegex(args=("pattern",), kwargs={"ignorecase": True})
        with pytest.raises(InvalidPattern):
>           assert isinstance(lazy_regex._real_regex, re.Pattern)
E           AssertionError: assert False
E            +  where False = isinstance(None, <class 're.Pattern'>)
E            +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f19a3c3a8c0>._real_regex
E            +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""
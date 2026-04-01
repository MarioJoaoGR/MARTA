
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    # Test initialization with valid inputs
    lazy_regex = LazyRegex(r'hello')
    assert isinstance(lazy_regex, LazyRegex)
    assert lazy_regex._regex_args == ('hello',)
    assert lazy_regex._regex_kwargs == {}

    complex_pattern = r'(?P<first>test)(?P<second>test)'
    lazy_complex = LazyRegex(complex_pattern, re.IGNORECASE)
    assert isinstance(lazy_complex, LazyRegex)
    assert lazy_complex._regex_args == (complex_pattern,)
    assert lazy_complex._regex_kwargs == {'flags': re.IGNORECASE}

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getstate___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test initialization with valid inputs
        lazy_regex = LazyRegex(r'hello')
        assert isinstance(lazy_regex, LazyRegex)
>       assert lazy_regex._regex_args == ('hello',)
E       AssertionError: assert 'hello' == ('hello',)
E        +  where 'hello' = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fec9df68280>._regex_args

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getstate___0_test_valid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getstate___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""
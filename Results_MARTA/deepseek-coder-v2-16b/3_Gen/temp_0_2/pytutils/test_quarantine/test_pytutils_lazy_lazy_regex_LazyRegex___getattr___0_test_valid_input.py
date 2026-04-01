
import re
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

@pytest.mark.parametrize("pattern, flags", [("[a-zA-Z0-9]+", re.IGNORECASE)])
def test_valid_input(pattern, flags):
    lazy_regex = LazyRegex(args=(pattern,), kwargs={'flags': flags})
    assert hasattr(lazy_regex, '_real_regex')
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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_________________ test_valid_input[[a-zA-Z0-9]+-re.IGNORECASE] _________________

pattern = '[a-zA-Z0-9]+', flags = re.IGNORECASE

    @pytest.mark.parametrize("pattern, flags", [("[a-zA-Z0-9]+", re.IGNORECASE)])
    def test_valid_input(pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={'flags': flags})
        assert hasattr(lazy_regex, '_real_regex')
>       assert isinstance(lazy_regex._real_regex, re.Pattern)
E       AssertionError: assert False
E        +  where False = isinstance(None, <class 're.Pattern'>)
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7ff02c105630>._real_regex
E        +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py::test_valid_input[[a-zA-Z0-9]+-re.IGNORECASE]
============================== 1 failed in 0.06s ===============================
"""
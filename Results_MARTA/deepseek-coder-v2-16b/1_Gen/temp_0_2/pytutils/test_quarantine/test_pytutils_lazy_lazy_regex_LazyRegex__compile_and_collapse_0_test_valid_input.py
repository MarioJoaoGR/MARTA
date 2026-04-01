
import re
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    @pytest.mark.parametrize("pattern, flags", [
        ("hello", re.IGNORECASE),
        (r"^[a-z]+$", 0)
    ])
    def test_valid_input(self, pattern, flags):
        lazy_regex = LazyRegex(pattern, flags)
        assert hasattr(lazy_regex, '_real_regex'), "The regex should be compiled when accessed."
        assert isinstance(lazy_regex._real_regex, re.Pattern), "The result of the regex should be a pattern object."

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ TestLazyRegex.test_valid_input[hello-re.IGNORECASE] ______________

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.TestLazyRegex object at 0x7fbe47708310>
pattern = 'hello', flags = re.IGNORECASE

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", re.IGNORECASE),
        (r"^[a-z]+$", 0)
    ])
    def test_valid_input(self, pattern, flags):
        lazy_regex = LazyRegex(pattern, flags)
        assert hasattr(lazy_regex, '_real_regex'), "The regex should be compiled when accessed."
>       assert isinstance(lazy_regex._real_regex, re.Pattern), "The result of the regex should be a pattern object."
E       AssertionError: The result of the regex should be a pattern object.
E       assert False
E        +  where False = isinstance(None, <class 're.Pattern'>)
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbe470f43a0>._real_regex
E        +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:14: AssertionError
__________________ TestLazyRegex.test_valid_input[^[a-z]+$-0] __________________

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.TestLazyRegex object at 0x7fbe4713d090>
pattern = '^[a-z]+$', flags = 0

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", re.IGNORECASE),
        (r"^[a-z]+$", 0)
    ])
    def test_valid_input(self, pattern, flags):
        lazy_regex = LazyRegex(pattern, flags)
        assert hasattr(lazy_regex, '_real_regex'), "The regex should be compiled when accessed."
>       assert isinstance(lazy_regex._real_regex, re.Pattern), "The result of the regex should be a pattern object."
E       AssertionError: The result of the regex should be a pattern object.
E       assert False
E        +  where False = isinstance(None, <class 're.Pattern'>)
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbe470f52d0>._real_regex
E        +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py::TestLazyRegex::test_valid_input[hello-re.IGNORECASE]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py::TestLazyRegex::test_valid_input[^[a-z]+$-0]
============================== 2 failed in 0.06s ===============================
"""
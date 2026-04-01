
import pytest
from pytutils.lazy.lazy_regex import lazy_compile, LazyRegex
import re

@pytest.mark.parametrize("pattern, flags", [
    ('hello\\d+', 0),
    (r'hello\d+', re.IGNORECASE),
    ('hello\\d+', re.DOTALL),
    (r'hello\d+', re.IGNORECASE | re.DOTALL)
])
def test_valid_input(pattern, flags):
    lazy_regex = lazy_compile(pattern, flags)
    assert hasattr(lazy_regex._real_regex, 'search'), "The regex object should be compiled"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_valid_input[hello\\d+-0] _________________________

pattern = 'hello\\d+', flags = 0

    @pytest.mark.parametrize("pattern, flags", [
        ('hello\\d+', 0),
        (r'hello\d+', re.IGNORECASE),
        ('hello\\d+', re.DOTALL),
        (r'hello\d+', re.IGNORECASE | re.DOTALL)
    ])
    def test_valid_input(pattern, flags):
        lazy_regex = lazy_compile(pattern, flags)
>       assert hasattr(lazy_regex._real_regex, 'search'), "The regex object should be compiled"
E       AssertionError: The regex object should be compiled
E       assert False
E        +  where False = hasattr(None, 'search')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbeeb968f70>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py:14: AssertionError
__________________ test_valid_input[hello\\d+-re.IGNORECASE] ___________________

pattern = 'hello\\d+', flags = re.IGNORECASE

    @pytest.mark.parametrize("pattern, flags", [
        ('hello\\d+', 0),
        (r'hello\d+', re.IGNORECASE),
        ('hello\\d+', re.DOTALL),
        (r'hello\d+', re.IGNORECASE | re.DOTALL)
    ])
    def test_valid_input(pattern, flags):
        lazy_regex = lazy_compile(pattern, flags)
>       assert hasattr(lazy_regex._real_regex, 'search'), "The regex object should be compiled"
E       AssertionError: The regex object should be compiled
E       assert False
E        +  where False = hasattr(None, 'search')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbeeb969240>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py:14: AssertionError
____________________ test_valid_input[hello\\d+-re.DOTALL] _____________________

pattern = 'hello\\d+', flags = re.DOTALL

    @pytest.mark.parametrize("pattern, flags", [
        ('hello\\d+', 0),
        (r'hello\d+', re.IGNORECASE),
        ('hello\\d+', re.DOTALL),
        (r'hello\d+', re.IGNORECASE | re.DOTALL)
    ])
    def test_valid_input(pattern, flags):
        lazy_regex = lazy_compile(pattern, flags)
>       assert hasattr(lazy_regex._real_regex, 'search'), "The regex object should be compiled"
E       AssertionError: The regex object should be compiled
E       assert False
E        +  where False = hasattr(None, 'search')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbeeb95ce50>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py:14: AssertionError
_____________ test_valid_input[hello\\d+-re.IGNORECASE|re.DOTALL] ______________

pattern = 'hello\\d+', flags = re.IGNORECASE|re.DOTALL

    @pytest.mark.parametrize("pattern, flags", [
        ('hello\\d+', 0),
        (r'hello\d+', re.IGNORECASE),
        ('hello\\d+', re.DOTALL),
        (r'hello\d+', re.IGNORECASE | re.DOTALL)
    ])
    def test_valid_input(pattern, flags):
        lazy_regex = lazy_compile(pattern, flags)
>       assert hasattr(lazy_regex._real_regex, 'search'), "The regex object should be compiled"
E       AssertionError: The regex object should be compiled
E       assert False
E        +  where False = hasattr(None, 'search')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbeeb95cd30>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py::test_valid_input[hello\\d+-0]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py::test_valid_input[hello\\d+-re.IGNORECASE]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py::test_valid_input[hello\\d+-re.DOTALL]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_1_test_valid_input.py::test_valid_input[hello\\d+-re.IGNORECASE|re.DOTALL]
============================== 4 failed in 0.07s ===============================
"""

import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern

@pytest.mark.parametrize("pattern", ["*", ".*"])
def test_invalid_input(pattern):
    with pytest.raises(InvalidPattern) as exc_info:
        lazy_regex = LazyRegex(args=(pattern,))
        # Attempting to access the regex will trigger compilation which should raise InvalidPattern if the pattern is invalid
        next(re.finditer(lazy_regex._real_regex.pattern, "test"))

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_2_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_input[*] _____________________________

pattern = '*'

    @pytest.mark.parametrize("pattern", ["*", ".*"])
    def test_invalid_input(pattern):
        with pytest.raises(InvalidPattern) as exc_info:
            lazy_regex = LazyRegex(args=(pattern,))
            # Attempting to access the regex will trigger compilation which should raise InvalidPattern if the pattern is invalid
>           next(re.finditer(lazy_regex._real_regex.pattern, "test"))
E           AttributeError: 'NoneType' object has no attribute 'pattern'

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_2_test_invalid_input.py:11: AttributeError
____________________________ test_invalid_input[.*] ____________________________

pattern = '.*'

    @pytest.mark.parametrize("pattern", ["*", ".*"])
    def test_invalid_input(pattern):
        with pytest.raises(InvalidPattern) as exc_info:
            lazy_regex = LazyRegex(args=(pattern,))
            # Attempting to access the regex will trigger compilation which should raise InvalidPattern if the pattern is invalid
>           next(re.finditer(lazy_regex._real_regex.pattern, "test"))
E           AttributeError: 'NoneType' object has no attribute 'pattern'

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_2_test_invalid_input.py:11: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_2_test_invalid_input.py::test_invalid_input[*]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_2_test_invalid_input.py::test_invalid_input[.*]
============================== 2 failed in 0.07s ===============================
"""
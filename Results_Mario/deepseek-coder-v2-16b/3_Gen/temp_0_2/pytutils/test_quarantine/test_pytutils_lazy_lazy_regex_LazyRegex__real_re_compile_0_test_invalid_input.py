
import pytest
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern

@pytest.mark.parametrize("pattern", ["invalidpattern"])
def test_invalid_input(pattern):
    with pytest.raises(InvalidPattern) as excinfo:
        lazy_regex = LazyRegex(args=(pattern,))
        # Attempt to access a method that will trigger the regex compilation
        lazy_regex._real_re_compile()  # This should raise an InvalidPattern error

    assert str(excinfo.value) == f'"{pattern}" is not a valid regex pattern'

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input[invalidpattern] ______________________

pattern = 'invalidpattern'

    @pytest.mark.parametrize("pattern", ["invalidpattern"])
    def test_invalid_input(pattern):
        with pytest.raises(InvalidPattern) as excinfo:
            lazy_regex = LazyRegex(args=(pattern,))
            # Attempt to access a method that will trigger the regex compilation
>           lazy_regex._real_re_compile()  # This should raise an InvalidPattern error

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f6bbe2776d0>, args = ()
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
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_invalid_input.py::test_invalid_input[invalidpattern]
============================== 1 failed in 0.06s ===============================
"""
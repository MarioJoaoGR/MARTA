
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

@pytest.mark.parametrize("pattern, kwargs", [
    ("pattern", {"ignorecase": True}),
    (r'\d+', {"ignorecase": False})
])
def test_valid_input(pattern, kwargs):
    lazy_regex = LazyRegex(pattern, **kwargs)
    assert hasattr(lazy_regex, '_real_regex')
    assert isinstance(lazy_regex._real_regex, type(re.compile(pattern, **kwargs)))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:12:51: E0602: Undefined variable 're' (undefined-variable)


"""
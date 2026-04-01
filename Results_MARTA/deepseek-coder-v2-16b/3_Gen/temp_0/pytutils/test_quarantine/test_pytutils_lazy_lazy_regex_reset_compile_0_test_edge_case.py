
import pytest
from pytutils.lazy import lazy_regex

@pytest.fixture(autouse=True)
def reset_re_compile():
    original_compile = lazy_regex._real_re_compile
    yield
    re.compile = original_compile

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_reset_compile_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_reset_compile_0_test_edge_case.py:9:4: E0602: Undefined variable 're' (undefined-variable)


"""
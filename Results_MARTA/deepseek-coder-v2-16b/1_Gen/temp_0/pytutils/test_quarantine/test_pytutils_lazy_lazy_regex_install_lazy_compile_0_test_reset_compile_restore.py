
import pytest
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile

def test_reset_compile_restore():
    from re import compile as _compile
    
    # Override the default behavior to use lazy_compile
    def lazy_compile(pattern, flags=0):
        print("Compiling lazily")
        return _compile(pattern, flags)
    
    def reset_compile():
        re.compile = _compile
    
    install_lazy_compile()  # Now re.compile uses lazy_compile by default.
    
    # Check if the assertion is correct
    assert re.compile is lazy_compile
    
    # Revert back to the original functionality
    reset_compile()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_reset_compile_restore
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_reset_compile_restore.py:14:8: E0602: Undefined variable 're' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_reset_compile_restore.py:16:4: E0602: Undefined variable 'install_lazy_compile' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_reset_compile_restore.py:19:11: E0602: Undefined variable 're' (undefined-variable)


"""

import pytest
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile

def install_lazy_compile():
    """Make lazy_compile the default compile mode for regex compilation.

    This overrides re.compile with lazy_compile. To restore the original
    functionality, call reset_compile().
    """
    from re import compile as _compile
    re.compile = lazy_compile

def test_install_lazy_compile_default():
    # Save the original compile function
    original_compile = re.compile
    
    try:
        install_lazy_compile()
        assert re.compile == lazy_compile
        
        # Test that reset_compile restores the original functionality
        reset_compile()
        assert re.compile == original_compile
    finally:
        # Ensure to restore the original compile function after the test
        reset_compile()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_install_lazy_compile_default
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_install_lazy_compile_default.py:12:4: E0602: Undefined variable 're' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_install_lazy_compile_default.py:16:23: E0602: Undefined variable 're' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_install_lazy_compile_default.py:20:15: E0602: Undefined variable 're' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0_test_install_lazy_compile_default.py:24:15: E0602: Undefined variable 're' (undefined-variable)


"""

import pytest
import re
from pytutils.lazy import lazy_regex

# Assuming _real_re_compile is a reference to the original re.compile function
_real_re_compile = re.compile  # Save the original re.compile for later restoration

def reset_compile():
    """Restore the original function to `re.compile()`.

    This function resets `re.compile` to its original state as imported from the `re` module. It is designed to be called multiple times without causing issues, though it does not track nesting levels and will always restore `re.compile` back to its initial value at import time.

    Examples:
        >>> reset_compile()
        >>> isinstance(re.compile, types.FunctionType)
        True

    Note:
        - This function is idempotent and can be called multiple times without side effects.
        - It does not handle nested or recursive calls to `re.compile`.
        - Always restores `re.compile` to its original state at import time.
    """
    re.compile = _real_re_compile

def test_multiple_calls():
    # Call reset_compile() multiple times and ensure no side effects or issues arise
    for _ in range(3):  # Multiple calls to simulate nesting or repeated use
        reset_compile()
    assert re.compile == _real_re_compile

def test_invalid_input():
    # Test handling of invalid inputs like None or incorrect types
    with pytest.raises(TypeError):
        reset_compile(None)  # Passing None should raise a TypeError


import pytest
from ansible.module_utils.common.validation import safe_eval

def test_safe_eval_basic():
    # Test evaluating a simple literal expression
    result = safe_eval("42")
    assert result == 42

    # Test evaluating an array literal
    result = safe_eval("[1, 2, 3]")
    assert result == [1, 2, 3]

    # Test handling a method call that is not allowed (with exceptions included)
    try:
        result = safe_eval("os.path.join('foo', 'bar')", include_exceptions=True)
    except Exception as e:
        assert isinstance(e, AttributeError)
        assert str(e) == "'str' object has no attribute 'os'"

    # Test preventing an import statement (with exceptions included)
    try:
        result = safe_eval("import os", include_exceptions=True)
    except Exception as e:
        assert isinstance(e, ImportError)
        assert str(e) == "No module named 'os'"

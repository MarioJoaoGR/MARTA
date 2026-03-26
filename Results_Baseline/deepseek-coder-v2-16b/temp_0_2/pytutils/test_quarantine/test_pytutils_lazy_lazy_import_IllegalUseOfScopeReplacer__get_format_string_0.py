
# Module: pytutils.lazy.lazy_import
import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_basic_usage():
    err = IllegalUseOfScopeReplacer('example_name', 'This is an example error message.')
    assert str(err) == "ScopeReplacer object 'example_name' was used incorrectly: This is an example error message."

def test_with_extra_information():
    err = IllegalUseOfScopeReplacer('another_name', 'Something went wrong.', extra='Additional details here.')
    assert str(err) == "ScopeReplacer object 'another_name' was used incorrectly: Something went wrong.: Additional details here."

def test_custom_exception_handling():
    try:
        scope_replacer = ScopeReplacer('example', 'This is an example of incorrect usage.')
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "ScopeReplacer object 'example' was used incorrectly: This is an example of incorrect usage."

def test_with_extra_information_exception_handling():
    try:
        scope_replacer = ScopeReplacer('another_example', 'Another reason for misuse.', extra='Additional context.')
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "ScopeReplacer object 'another_example' was used incorrectly: Another reason for misuse.: Additional context."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0.py:16:25: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0.py:22:25: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)


"""
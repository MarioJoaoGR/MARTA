
from pytutils.lazy.lazy_import import lazy_import
import pytest

@pytest.mark.parametrize("member, children, expected_error", [
    (None, {'bar':(['foo', 'bar'], None, {})}, ValueError),
    ('bar', {}, ValueError),
])
def test_invalid_input_error_handling(member, children, expected_error):
    with pytest.raises(expected_error):
        ImportReplacer(scope=globals(), name='foo', module_path=['foo'], member=member, children=children)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_invalid_input_error_handling
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_invalid_input_error_handling.py:11:8: E0602: Undefined variable 'ImportReplacer' (undefined-variable)


"""
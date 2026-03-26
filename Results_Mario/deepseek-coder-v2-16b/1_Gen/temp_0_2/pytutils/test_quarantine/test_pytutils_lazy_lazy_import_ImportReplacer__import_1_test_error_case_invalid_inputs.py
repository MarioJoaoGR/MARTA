
import pytest
from unittest.mock import patch
from your_module_name import ImportReplacer  # Replace with the actual module name where ImportReplacer is defined

@pytest.mark.parametrize("member, children", [
    (None, {'bar': (['foo', 'bar'], None, {})}),
    ('foo', {}),
])
def test_error_case_invalid_inputs(member, children):
    with pytest.raises(ValueError) as excinfo:
        ImportReplacer(scope={}, name='test', module_path=['foo'], member=member, children=children)
    assert 'Cannot supply both a member and children' in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportReplacer__import_1_test_error_case_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_1_test_error_case_invalid_inputs.py:4:0: E0401: Unable to import 'your_module_name' (import-error)


"""
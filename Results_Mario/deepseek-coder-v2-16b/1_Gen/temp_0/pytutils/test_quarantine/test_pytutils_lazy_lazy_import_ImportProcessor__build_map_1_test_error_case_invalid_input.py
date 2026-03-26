
from pytutils.lazy import lazy_import
from pytutils.Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_error_case_invalid_input import ImportProcessor, errors

def test_error_case_invalid_input():
    processor = ImportProcessor()
    
    # Test with invalid input that doesn't start with 'import ' or 'from '
    text = "some random text"
    try:
        processor._build_map(text)
    except errors.InvalidImportLine as e:
        assert str(e) == f"{text} doesn't start with 'import ' or 'from '"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_error_case_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_error_case_invalid_input.py:3:0: E0401: Unable to import 'pytutils.Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_error_case_invalid_input' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_error_case_invalid_input.py:3:0: E0611: No name 'Test4DT_tests' in module 'pytutils' (no-name-in-module)


"""
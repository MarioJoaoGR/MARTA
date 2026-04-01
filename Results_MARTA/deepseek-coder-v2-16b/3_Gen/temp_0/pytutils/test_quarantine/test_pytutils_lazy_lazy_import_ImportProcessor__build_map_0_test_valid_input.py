
from unittest.mock import patch
from pytutils.lazy.lazy_import import ImportReplacer
from pytutils.lazy.import_processor import ImportProcessor

def test_valid_input():
    with patch('pytutils.lazy.lazy_import.ImportReplacer') as mock_import_replacer:
        processor = ImportProcessor()
        scope = {}
        text = "from math import sqrt, pi"
        
        # Call the method under test
        processor._build_map(text)
        
        # Assertions to verify the behavior
        assert len(processor.imports) == 2
        assert 'sqrt' in processor.imports
        assert 'pi' in processor.imports
        mock_import_replacer.assert_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_0_test_valid_input.py:4:0: E0401: Unable to import 'pytutils.lazy.import_processor' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_0_test_valid_input.py:4:0: E0611: No name 'import_processor' in module 'pytutils.lazy' (no-name-in-module)


"""
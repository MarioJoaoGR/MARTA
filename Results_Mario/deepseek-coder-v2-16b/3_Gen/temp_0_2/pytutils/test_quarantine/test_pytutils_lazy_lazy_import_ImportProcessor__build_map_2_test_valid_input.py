
from unittest import mock
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
from pytutils.errors import InvalidImportLine

@pytest.fixture
def processor():
    return ImportProcessor()

def test_valid_input(processor):
    text = """
    import os
    from math import sin
    from subprocess import Popen
    """
    
    with mock.patch('pytutils.lazy.lazy_import.ImportReplacer._convert_import_str', autospec=True) as mock_convert_import:
        with mock.patch('pytutils.lazy.lazy_import.ImportReplacer._convert_from_str', autospec=True) as mock_convert_from:
            processor._build_map(text)
            
    assert len(processor.imports) == 3
    assert 'os' in processor.imports
    assert 'sin' in processor.imports
    assert 'Popen' in processor.imports
    
    mock_convert_import.assert_called()
    mock_convert_from.assert_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_2_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_2_test_valid_input.py:5:0: E0401: Unable to import 'pytutils.errors' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_2_test_valid_input.py:5:0: E0611: No name 'errors' in module 'pytutils' (no-name-in-module)


"""
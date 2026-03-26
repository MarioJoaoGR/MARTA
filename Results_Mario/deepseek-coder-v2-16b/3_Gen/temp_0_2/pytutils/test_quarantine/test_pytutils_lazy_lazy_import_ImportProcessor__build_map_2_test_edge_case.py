
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
from unittest.mock import patch
import pytest
from errors import InvalidImportLine

@pytest.fixture
def setup_processor():
    return ImportProcessor()

def test_build_map_valid_imports(setup_processor):
    text = """
    import os
    import sys
    from math import sqrt
    """
    with patch('ImportProcessor._canonicalize_import_text', return_value=text.splitlines()):
        setup_processor._build_map(text)
        assert 'os' in setup_processor.imports
        assert 'sys' in setup_processor.imports
        assert 'math' in setup_processor.imports
        assert '_lazy_import_class' in dir(setup_processor)

def test_build_map_invalid_imports(setup_processor):
    text = """
    invalid line
    from math import sqrt
    """
    with patch('ImportProcessor._canonicalize_import_text', return_value=text.splitlines()):
        with pytest.raises(InvalidImportLine):
            setup_processor._build_map(text)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_2_test_edge_case
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_2_test_edge_case.py:5:0: E0401: Unable to import 'errors' (import-error)


"""
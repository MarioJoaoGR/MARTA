
from pytutils.lazy import lazy_import
from pytutils.errors import InvalidImportLine, ImportNameCollision
import pytest

@pytest.fixture
def processor():
    return lazy_import.ImportProcessor()

def test_build_map_with_valid_imports(processor):
    text = """
    import os
    from math import sqrt
    from datetime import date as d, timedelta
    """
    processor._build_map(text)
    assert len(processor.imports) == 3
    assert 'os' in processor.imports
    assert processor.imports['os'] == ([], None, {})
    assert 'sqrt' in processor.imports
    assert processor.imports['sqrt'] == (['math'], 'sqrt', {})
    assert 'd' in processor.imports
    assert processor.imports['d'] == (['datetime'], 'date', {})
    assert 'timedelta' in processor.imports
    assert processor.imports['timedelta'] == (['datetime'], 'timedelta', {})

def test_build_map_with_invalid_import(processor):
    text = """
    import invalid_module
    from non_existent_module import function
    """
    with pytest.raises(InvalidImportLine) as excinfo:
        processor._build_map(text)
    assert "doesn't start with 'import '" in str(excinfo.value)

def test_build_map_with_duplicate_names(processor):
    text = """
    import os
    from math import sqrt as s, pi
    """
    processor._build_map(text)
    assert len(processor.imports) == 3
    assert 'os' in processor.imports
    assert processor.imports['os'] == ([], None, {})
    assert 'sqrt' in processor.imports
    assert processor.imports['sqrt'] == (['math'], 'sqrt', {})
    assert 'pi' in processor.imports
    assert processor.imports['pi'] == (['math'], 'pi', {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_edge_case_none
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_edge_case_none.py:3:0: E0401: Unable to import 'pytutils.errors' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_1_test_edge_case_none.py:3:0: E0611: No name 'errors' in module 'pytutils' (no-name-in-module)


"""
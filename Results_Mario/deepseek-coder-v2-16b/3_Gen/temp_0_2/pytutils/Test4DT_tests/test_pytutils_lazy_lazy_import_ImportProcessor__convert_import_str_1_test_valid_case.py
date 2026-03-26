
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_valid_case():
    processor = ImportProcessor()
    
    # Test a valid import string
    import_str = 'import os, os.path as op, sys'
    processor._convert_import_str(import_str)
    
    assert len(processor.imports) == 3
    assert 'os' in processor.imports
    assert processor.imports['os'] == (['os'], None, {})
    assert 'op' in processor.imports
    assert processor.imports['op'] == (['os', 'path'], None, {})
    assert 'sys' in processor.imports
    assert processor.imports['sys'] == (['sys'], None, {})

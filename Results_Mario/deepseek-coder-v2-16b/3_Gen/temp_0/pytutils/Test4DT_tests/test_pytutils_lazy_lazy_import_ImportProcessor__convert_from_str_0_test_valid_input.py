
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_valid_input():
    processor = ImportProcessor()
    from_str = 'from foo import bar'
    processor._convert_from_str(from_str)
    assert len(processor.imports) == 1
    assert 'bar' in processor.imports

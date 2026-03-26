
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_invalid_input():
    processor = ImportProcessor()
    
    with pytest.raises(ValueError):
        processor._convert_from_str('foo bar')

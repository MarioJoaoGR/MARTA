
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

def test_invalid_input():
    processor = ImportProcessor()
    
    with pytest.raises(ValueError):
        processor._convert_import_str('invalid import string')

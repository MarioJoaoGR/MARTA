
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_none_input():
    processor = ImportProcessor()
    with pytest.raises(ValueError):
        processor._convert_from_str("some random string")

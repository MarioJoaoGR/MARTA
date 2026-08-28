
import pytest
from pytutils.lazy import lazy_import
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

# Test default replacer functionality

# Test custom replacer functionality

# Test handling of malformed input
def test_malformed_input():
    processor = ImportProcessor()
    with pytest.raises(ValueError) as excinfo:
        processor._convert_from_str('invalid input')
    assert str(excinfo.value) == 'bad from/import \'invalid input\''
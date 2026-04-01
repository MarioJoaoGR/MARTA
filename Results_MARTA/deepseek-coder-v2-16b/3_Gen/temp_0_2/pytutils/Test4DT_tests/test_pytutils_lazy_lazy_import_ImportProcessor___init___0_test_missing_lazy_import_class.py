
from pytutils.lazy.lazy_import import ImportReplacer
from unittest.mock import patch
import pytest

@pytest.fixture(autouse=True)
def setup():
    with patch('pytutils.lazy.lazy_import.ImportReplacer', autospec=True):
        yield

def test_missing_lazy_import_class():
    from pytutils.lazy.lazy_import import ImportProcessor
    
    processor = ImportProcessor(lazy_import_class=None)
    assert isinstance(processor._lazy_import_class, ImportReplacer)

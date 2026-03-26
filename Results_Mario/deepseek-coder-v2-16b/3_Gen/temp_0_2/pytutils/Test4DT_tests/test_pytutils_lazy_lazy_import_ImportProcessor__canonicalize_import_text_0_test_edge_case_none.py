
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
import pytest

def test_edge_case_none():
    processor = ImportProcessor()
    with pytest.raises(AttributeError):
        processor._canonicalize_import_text(None)

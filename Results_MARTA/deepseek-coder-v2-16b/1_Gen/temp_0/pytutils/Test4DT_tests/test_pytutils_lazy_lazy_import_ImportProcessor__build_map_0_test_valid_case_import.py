
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

@pytest.fixture
def processor():
    return ImportProcessor()

def test_valid_case_import(processor):
    text = "import os, sys"
    processor._build_map(text)
    assert 'os' in processor.imports
    assert 'sys' in processor.imports

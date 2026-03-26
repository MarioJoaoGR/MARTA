
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

@pytest.fixture(autouse=True)
def setup():
    processor = ImportProcessor()
    yield processor

def test_valid_input(setup):
    processor = setup
    text = "import os, sys"
    scope = {}
    result = processor._convert_import_str(text)
    assert 'os' in processor.imports
    assert 'sys' in processor.imports

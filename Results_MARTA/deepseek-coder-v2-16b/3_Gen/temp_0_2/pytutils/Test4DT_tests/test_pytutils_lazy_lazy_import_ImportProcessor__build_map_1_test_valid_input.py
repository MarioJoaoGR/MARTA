
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

@pytest.fixture(name="mock_processor")
def fixture_mock_processor():
    return ImportProcessor()

def test_valid_input(mock_processor):
    text = """
    import os
    from math import sin
    from datetime import date
    """
    mock_processor._build_map(text)
    assert 'os' in mock_processor.imports
    assert 'sin' in mock_processor.imports
    assert 'date' in mock_processor.imports

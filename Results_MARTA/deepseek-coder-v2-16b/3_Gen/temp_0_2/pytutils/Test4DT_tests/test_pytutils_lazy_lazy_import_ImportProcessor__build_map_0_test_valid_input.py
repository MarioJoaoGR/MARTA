
import pytest
from unittest.mock import MagicMock
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

@pytest.fixture(autouse=True)
def setup():
    mock_processor = ImportProcessor()
    mock_processor.imports = {}
    yield mock_processor

def test_valid_input(setup):
    mock_processor = setup
    text = """
    import os
    from math import sin
    from sys import platform as sys_platform
    """
    mock_processor._build_map(text)
    assert 'os' in mock_processor.imports
    assert 'sin' in mock_processor.imports
    assert 'sys_platform' in mock_processor.imports

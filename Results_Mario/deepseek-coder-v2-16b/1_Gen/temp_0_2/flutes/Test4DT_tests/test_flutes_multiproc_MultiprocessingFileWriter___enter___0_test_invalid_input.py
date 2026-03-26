
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def invalid_input():
    return None  # This is an invalid input since it doesn't match the expected type for 'path'

@patch('flutes.multiproc.mp', spec=True)
def test_invalid_input(mock_mp, invalid_input):
    with pytest.raises(TypeError):
        MultiprocessingFileWriter(invalid_input)

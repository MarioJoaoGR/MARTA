
import pytest
from unittest.mock import patch, MagicMock
from flutes.fs import get_folder_size
from pathlib import Path

@pytest.mark.parametrize("path", [Path('.'), Path('/some/directory')])
def test_valid_input(path):
    with patch('subprocess.check_output', return_value=MagicMock(spec=bytes)):
        assert isinstance(get_folder_size(path), int)

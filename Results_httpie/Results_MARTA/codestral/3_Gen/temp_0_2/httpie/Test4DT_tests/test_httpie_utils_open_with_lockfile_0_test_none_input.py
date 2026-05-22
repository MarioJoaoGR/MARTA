
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.utils import open_with_lockfile

def test_none_input():
    with patch('httpie.utils.open', return_value=None):
        file_path = Path('/some/directory/file.txt')
        with pytest.raises(TypeError):
            for stream in open_with_lockfile(file_path):
                pass

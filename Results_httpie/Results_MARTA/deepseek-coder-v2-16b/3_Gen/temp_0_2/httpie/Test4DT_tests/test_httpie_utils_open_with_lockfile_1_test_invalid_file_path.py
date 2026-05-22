
import pytest
from pathlib import Path
from httpie.utils import open_with_lockfile
from unittest.mock import patch, MagicMock
from tempfile import gettempdir
import base64
import os

def test_invalid_file_path():
    with patch('httpie.utils.open', new=MagicMock()):
        file_path = Path('/nonexistent/directory/file.txt')
        with pytest.raises(TypeError):
            for stream in open_with_lockfile(file_path):
                pass

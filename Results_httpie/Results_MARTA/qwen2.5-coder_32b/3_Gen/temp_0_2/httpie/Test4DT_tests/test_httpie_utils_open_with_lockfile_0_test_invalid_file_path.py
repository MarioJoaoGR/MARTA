
import pytest
from pathlib import Path
from tempfile import gettempdir
import base64
import os
from unittest.mock import patch, MagicMock
from httpie.utils import open_with_lockfile

def test_invalid_file_path():
    with patch('httpie.utils.open', create=True) as mock_open:
        with patch('os.fsencode') as mock_fsencode:
            with patch('base64.b64encode') as mock_b64encode:
                with patch('tempfile.gettempdir', return_value='/tmp'):
                    file_path = Path('/invalid/file/path')
                    
                    with pytest.raises(TypeError):
                        for stream in open_with_lockfile(file_path):
                            pass

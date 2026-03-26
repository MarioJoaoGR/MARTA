
import io
import sys
from configparser import ConfigParser
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from isort.api import sort_file


@pytest.mark.parametrize("filename", ["test_file.py"])  # Assuming a valid file for testing
def test_valid_case(filename):
    with patch('isort.api._config', return_value=MagicMock()):
        with patch('isort.api.io.File.read') as mock_read:
            mock_file = MagicMock()
            mock_file.path = Path(filename)
            mock_stream = io.StringIO("import os\nimport sys")
            mock_file.stream = mock_stream
            
            mock_read.return_value = mock_file
            
            with patch('isort.api.sort_stream') as mock_sort_stream:
                mock_sort_stream.return_value = True  # Assuming sort_stream returns True if changes are made
                
                result = sort_file(filename)
                
                assert result is True, "Expected the file to be sorted and marked as changed"


import os
import re
import stat
from unittest.mock import patch

from isort.settings import Config


def test_is_supported_filetype():
    config = Config()
    
    # Test with a supported file extension
    assert config.is_supported_filetype("testfile.py") == True
    
    # Test with a blocked file extension
    assert config.is_supported_filetype("testfile.txt") == False
    
    # Test with an unsupported but not blocked file extension
    assert config.is_supported_filetype("testfile.java") == False
    
    # Test with an editor backup file
    assert config.is_supported_filetype("testfile~") == False
    
    # Test with a FIFO special file (should return False)
    with patch('os.stat') as mock_stat:
        mock_stat.return_value.st_mode = stat.S_IFIFO
        assert config.is_supported_filetype("testfifo") == False
    
    # Test with a regular file that starts with a shebang line (should return True)
    with patch('builtins.open', create=True) as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.readline.return_value = b"#!/usr/bin/env python\n"
        assert config.is_supported_filetype("testshebang") == True
    
    # Test with a regular file that does not start with a shebang line (should return False)
    mock_file.readline.return_value = b"# Some other comment\n"
    assert config.is_supported_filetype("testnoshebang") == False

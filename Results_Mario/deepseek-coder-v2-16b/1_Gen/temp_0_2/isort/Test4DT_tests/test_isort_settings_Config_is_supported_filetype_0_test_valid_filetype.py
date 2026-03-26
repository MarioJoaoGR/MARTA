
import os
import stat
import re
from isort.settings import Config

def test_valid_filetype():
    config = Config()
    
    # Test a file with a supported extension
    assert config.is_supported_filetype("testfile.py") == True
    
    # Test a file with an unsupported extension
    assert config.is_supported_filetype("testfile.txt") == False
    
    # Test a file with a blocked extension
    assert config.is_supported_filetype("testfile.cpp") == False
    
    # Test an editor backup file
    assert config.is_supported_filetype("testfile~") == False
    
    # Test a named pipe (FIFO) which is not supported
    if os.name != 'nt':  # Skip this test on Windows as it doesn't support FIFO files
        with open('tempfifo', 'wb') as fp:
            pass  # Create an empty FIFO file for testing
        assert config.is_supported_filetype('tempfifo') == False
        os.remove('tempfifo')  # Clean up the created FIFO file
    
    # Test a regular file with a shebang line
    with open("testfile", "w") as fp:
        fp.write("#!/usr/bin/env python\nprint('Hello, World!')")
    assert config.is_supported_filetype("testfile") == True
    os.remove("testfile")  # Clean up the created test file

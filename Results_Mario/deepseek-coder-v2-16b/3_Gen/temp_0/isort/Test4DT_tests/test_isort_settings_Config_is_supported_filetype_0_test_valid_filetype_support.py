
import os
from unittest.mock import patch
import pytest
from isort.settings import Config

@pytest.fixture
def config():
    return Config()

def test_valid_filetype_support(config):
    # Test a Python file
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a non-Python file with a .py extension (should be supported)
    assert config.is_supported_filetype("non_python_script.py") == True
    
    # Test an unsupported file type without .py extension
    assert config.is_supported_filetype("unsupported_file") == False
    
    # Test a Python file with a shebang line
    with open("test_script.py", "w") as f:
        f.write("#!/usr/bin/env python\nprint('Hello, World!')")
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a Python file with only whitespace in the shebang line
    with open("test_script.py", "w") as f:
        f.write("#! \nprint('Hello, World!')")
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a non-Python file with a shebang line (should not be supported)
    with open("non_python_script.sh", "w") as f:
        f.write("#!/usr/bin/bash\necho 'Hello, World!'")
    assert config.is_supported_filetype("non_python_script.sh") == False

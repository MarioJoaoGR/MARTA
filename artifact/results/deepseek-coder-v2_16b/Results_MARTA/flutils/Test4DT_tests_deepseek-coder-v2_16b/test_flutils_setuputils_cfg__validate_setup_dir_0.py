
import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

# Scenario 1: Valid directory with 'setup.py' and 'setup.cfg' files
def test_valid_directory_with_setup_files():
    setup_dir = '/tmp/myproject'
    os.makedirs(setup_dir, exist_ok=True)
    open(os.path.join(setup_dir, 'setup.py'), 'w').close()
    open(os.path.join(setup_dir, 'setup.cfg'), 'w').close()
    
    _validate_setup_dir(setup_dir)  # Should not raise an error

# Scenario 2: Non-existent directory
def test_nonexistent_directory():
    setup_dir = '/non/existent/directory'
    
    with pytest.raises(FileNotFoundError):
        _validate_setup_dir(setup_dir)  # Should raise FileNotFoundError

# Scenario 3: Existing but non-directory path
def test_non_directory_path():
    notadir = '/tmp/notadir'
    open(notadir, 'w').close()
    
    with pytest.raises(NotADirectoryError):
        _validate_setup_dir(notadir)  # Should raise NotADirectoryError

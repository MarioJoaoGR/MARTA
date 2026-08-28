
import os
from unittest.mock import patch, Mock
import pytest
from flutils.setuputils.cfg import _prep_setup_dir



def test_invalid_directory():
    # Mocking the getcwd to return a path that does not contain setup.py
    with patch('os.getcwd', return_value='non/existent/directory'):
        with pytest.raises(FileNotFoundError) as excinfo:
            _prep_setup_dir()
        assert "Unable to find the directory that contains the 'setup.py' file." in str(excinfo.value)
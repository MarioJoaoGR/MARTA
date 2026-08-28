
import pytest
from unittest.mock import patch
from flutils.setuputils.cfg import _validate_setup_dir


def test_non_existent_directory():
    with patch('os.path.exists', return_value=False):
        with pytest.raises(FileNotFoundError) as excinfo:
            _validate_setup_dir('/non/existent/directory')
        assert str(excinfo.value) == "The given 'setup_dir' of '/non/existent/directory' does NOT exist."

def test_non_directory():
    with patch('os.path.exists', return_value=True):
        with patch('os.path.isdir', return_value=False):
            with pytest.raises(NotADirectoryError) as excinfo:
                _validate_setup_dir('/non/directory')
            assert str(excinfo.value) == "The given 'setup_dir' of '/non/directory' is NOT a directory."

def test_valid_directory_without_setup_py():
    with patch('os.path.exists', return_value=True):
        with patch('os.path.isdir', return_value=True):
            with patch('os.path.isfile', side_effect=[False, True]):  # setup.py does not exist initially, then it exists
                with pytest.raises(FileNotFoundError) as excinfo:
                    _validate_setup_dir('/valid/directory/without/setup.py')
                assert str(excinfo.value) == "The given 'setup_dir' of '/valid/directory/without/setup.py' does NOT contain a setup.py file."

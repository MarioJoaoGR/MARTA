
# Module: apimd.loader
import pytest
from apimd.loader import loader
from unittest.mock import patch, MagicMock
from os.path import isfile as real_isfile

# Mocking _read and _load_module for controlled testing
def mock_read(path):
    if path.endswith('.py'):
        return "def foo():\n    pass"
    elif path.endswith('.pyi'):
        return "def bar() -> None:\n    ..."
    else:
        raise FileNotFoundError(f"No such file: '{path}'")

def mock_load_module(name, path, parser):
    if name == 'validmodule' and path.endswith('.so'):
        return True
    return False

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_pure_py(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return True for .py and False for others
    def mock_isfile_side_effect(path):
        return path.endswith('.py') or path.endswith('.pyi')
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    output = loader('/path/to/packages', 'mypackage', link=True, level=2, toc=True)
    assert isinstance(output, str)

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_extension_module(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return False for .py and .pyi, True for .so
    def mock_isfile_side_effect(path):
        return path.endswith('.so')
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    output = loader('/path/to/packages', 'validmodule', link=True, level=2, toc=True)
    assert isinstance(output, str)

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_no_extension_module(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return False for .py, .pyi, and .so
    def mock_isfile_side_effect(path):
        return False
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    with patch('apimd.loader.logger.warning') as mock_warning:
        output = loader('/path/to/packages', 'invalidmodule', link=True, level=2, toc=True)
        assert isinstance(output, str)
        mock_warning.assert_not_called()

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_mixed_files(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return True for .py and .so
    def mock_isfile_side_effect(path):
        return path.endswith('.py') or path.endswith('.so')
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    output = loader('/path/to/packages', 'mixedmodule', link=True, level=2, toc=True)
    assert isinstance(output, str)

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_only_pyi(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return True for .pyi and False for others
    def mock_isfile_side_effect(path):
        return path.endswith('.pyi')
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    output = loader('/path/to/packages', 'mypackage', link=True, level=2, toc=True)
    assert isinstance(output, str)

@patch('apimd.loader._read', side_effect=mock_read)
@patch('apimd.loader._load_module', side_effect=mock_load_module)
@patch('os.path.isfile')
def test_loader_no_files(mock_isfile, mock_load_module, mock_read):
    # Mock isfile to return False for all file types
    def mock_isfile_side_effect(path):
        return False
    
    mock_isfile.side_effect = mock_isfile_side_effect
    
    with patch('apimd.loader.logger.warning') as mock_warning:
        output = loader('/path/to/packages', 'mypackage', link=True, level=2, toc=True)
        assert isinstance(output, str)
        mock_warning.assert_not_called()

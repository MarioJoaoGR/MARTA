
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def doccli():
    args = ['--list-modules']  # Mock command-line arguments for testing
    return DocCLI(args=args)

def test_init(doccli):
    assert isinstance(doccli, DocCLI), "DocCLI instance should be created successfully"

@patch('ansible.cli.doc.PluginLoader')
def test_get_plugin_list_filenames(mock_loader, doccli):
    mock_instance = mock_loader.return_value
    mock_instance.find_plugin.side_effect = [
        "/path/to/module1.py",  # Found and not a directory or .ps1 file
        None,                   # Not found
        "/path/to/module2.py",   # Found but is a .ps1 file
        "/path/to/directory",    # Is a directory
    ]
    
    doccli.plugin_list = ['module1', 'module2']  # Mock plugin list
    result = doccli._get_plugin_list_filenames(mock_instance)
    
    assert len(result) == 1, "Only one module should be included in the result"
    assert "/path/to/module1.py" in result.values(), "The correct path should be included"

@patch('ansible.cli.doc.display')
def test_get_plugin_list_descriptions(mock_display, doccli):
    mock_loader = MagicMock()
    mock_loader.return_value.find_plugin.side_effect = [
        "/path/to/module1.py",  # Found and not a directory or .ps1 file
        None,                   # Not found
        "/path/to/module2.py",   # Found but is a .ps1 file
        "/path/to/directory",    # Is a directory
    ]
    
    doccli.plugin_list = ['module1', 'module2']  # Mock plugin list
    result = doccli._get_plugin_list_descriptions(mock_loader)
    
    assert len(result) == 1, "Only one module should be included in the result"
    assert "/path/to/module1.py" in result.values(), "The correct path should be included"

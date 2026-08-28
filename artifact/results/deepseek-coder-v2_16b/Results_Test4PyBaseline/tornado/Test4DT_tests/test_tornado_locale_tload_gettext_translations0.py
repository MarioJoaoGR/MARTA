
import pytest
from unittest.mock import patch, MagicMock
import os
import gettext

# Assuming the function is defined in a module named tornado.locale
from tornado.locale import load_gettext_translations

@patch('tornado.locale.os.listdir')
@patch('tornado.locale.os.path.isfile')
@patch('tornado.locale.os.stat')
@patch('tornado.locale.gettext.translation')
@patch('tornado.locale.gen_log.error')
def test_load_gettext_translations(mock_error, mock_gettext, mock_stat, mock_isfile, mock_listdir):
    # Mock data
    directory = "/path/to/locale/tree"
    domain = "myapp"
    
    # Mock listdir to return a list of language directories
    mock_listdir.return_value = ["en", "fr", "pt_BR"]
    
    # Mock isfile to always return False (no .mo files in the directory)
    mock_isfile.side_effect = [False, False, False]  # Called for each language directory and pt_BR/LC_MESSAGES/myapp.mo
    
    # Mock stat to raise an exception for pt_BR/LC_MESSAGES/myapp.mo
    mock_stat.side_effect = FileNotFoundError("File not found")
    
    # Call the function
    load_gettext_translations(directory, domain)
    
    # Assertions
    assert mock_listdir.called_once_with(directory)
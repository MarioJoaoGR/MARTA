
import pytest
from unittest.mock import patch, mock_open
import os
import csv
import codecs
from tornado.locale import load_translations, _translations, _supported_locales, gen_log

def test_load_translations_basic():
    with patch('builtins.open', mock_open()):
        with pytest.raises(FileNotFoundError):
            load_translations("path/to/translation/directory")

def test_load_translations_with_encoding():
    with patch('builtins.open', mock_open()):
        with pytest.raises(FileNotFoundError):
            load_translations("path/to/translation/directory", encoding="utf-16")

def test_load_translations_with_bom_detection():
    with patch('builtins.open', mock_open()):
        with pytest.raises(FileNotFoundError):
            load_translations("path/to/translation/directory")

def test_load_translations_unsupported_locales():
    with patch('builtins.open', mock_open()):
        with pytest.raises(FileNotFoundError):
            load_translations("path/to/translation/directory", encoding="utf-8")

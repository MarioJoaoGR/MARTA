
import os
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.replay import load

# Test for valid case where the directory and 'cookiecutter.json' file exist
def test_valid_case():
    with patch('os.path.isdir', return_value=True):
        with patch('os.path.isfile', return_value=True):
            context = load('data', 'example')
            assert isinstance(context, dict)
            assert 'cookiecutter' in context

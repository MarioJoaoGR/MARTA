
import pytest
from unittest.mock import patch
from thefuck.conf import Settings


def test_settings_from_args_with_debug():
    with patch('argparse.Namespace', autospec=True) as mock_namespace:
        mock_namespace.yes = False
        mock_namespace.debug = True
        mock_namespace.repeat = None

        settings = Settings()
        result = settings._settings_from_args(mock_namespace)
        assert 'debug' in result
        assert result['debug'] is True

def test_settings_from_args_with_repeat():
    with patch('argparse.Namespace', autospec=True) as mock_namespace:
        mock_namespace.yes = False
        mock_namespace.debug = False
        mock_namespace.repeat = 3

        settings = Settings()
        result = settings._settings_from_args(mock_namespace)
        assert 'repeat' in result
        assert result['repeat'] == 3
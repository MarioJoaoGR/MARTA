
import pytest
from unittest.mock import patch
from tornado.locale import get_supported_locales, _supported_locales

def test_get_supported_locales():
    # Define a mock list of supported locales
    with patch('tornado.locale._supported_locales', ['en-US', 'es-ES', 'fr-FR']):
        assert get_supported_locales() == ['en-US', 'es-ES', 'fr-FR']


import pytest
from tornado.locale import CSVLocale
from typing import Dict

def test_valid_init():
    translations = {
        'en': {'hello': 'Hello', 'goodbye': 'Goodbye'},
        'fr': {'hello': 'Bonjour', 'goodbye': 'Au revoir'}
    }
    locale = CSVLocale('en-US', translations)
    assert hasattr(locale, 'translations')
    assert locale.translations == translations

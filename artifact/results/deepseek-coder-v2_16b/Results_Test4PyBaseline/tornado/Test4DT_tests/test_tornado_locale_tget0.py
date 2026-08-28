
import pytest
from tornado.locale import get, Locale

# Test cases for the get function in the tornado.locale module

def test_basic_usage():
    # Get the closest match for English (en)
    en_locale = get("en")
    assert en_locale.code == "en" or en_locale.code == "en_US"

def test_multiple_codes():
    # Get the closest match for Spanish (es) and French (fr)
    es_locale = get("es", "fr")
    assert es_locale.code in ["es", "fr"] or es_locale.code == "en_US"

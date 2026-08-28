
import pytest
from unittest.mock import patch
from mimesis.providers.structure import Structure
from mimesis.exceptions import UnsupportedLocale



def test_invalid_inputs():
    with pytest.raises(UnsupportedLocale):
        with patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', {'en-US': True}):
            structure = Structure(locale='en-us', seed=42)
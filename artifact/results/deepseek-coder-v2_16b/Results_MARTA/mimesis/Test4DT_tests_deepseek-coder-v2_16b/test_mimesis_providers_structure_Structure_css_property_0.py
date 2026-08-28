
import pytest
from mimesis.providers.structure import Structure
from mimesis.exceptions import UnsupportedLocale



def test_invalid_input_error_handling():
    with pytest.raises(UnsupportedLocale):
        Structure(locale='invalid-locale', seed=42)
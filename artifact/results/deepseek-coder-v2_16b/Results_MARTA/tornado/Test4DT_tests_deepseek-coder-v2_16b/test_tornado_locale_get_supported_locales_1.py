
import pytest
from typing import Iterable

# Assuming _supported_locales is a predefined list of valid locale codes
_supported_locales = ["en-US", "es-ES", "fr-FR"]

def get_supported_locales() -> Iterable[str]:
    """Returns a list of all the supported locale codes."""
    return _supported_locales

# Test scenarios

def test_valid_input():
    assert get_supported_locales() == ["en-US", "es-ES", "fr-FR"]

def test_empty_list():
    with pytest.raises(TypeError):
        get_supported_locales([])

def test_invalid_input():
    with pytest.raises(TypeError):
        get_supported_locales(None)

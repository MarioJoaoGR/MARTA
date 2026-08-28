
import pytest
from unittest.mock import patch, MagicMock
from mimesis.providers.structure import Structure
from mimesis.data import CSS_PROPERTIES, CSS_SIZE_UNITS

@pytest.fixture(scope="module")
def structure():
    return Structure(locale='en', seed=42)

def test_css_property_generates_valid_css(structure):
    with patch('mimesis.providers.structure.CSS_PROPERTIES', CSS_PROPERTIES):
        css = structure.css_property()
        prop, value = css.split(': ')
        assert prop in CSS_PROPERTIES
        if isinstance(CSS_PROPERTIES[prop], list):
            assert value in CSS_PROPERTIES[prop]
        elif CSS_PROPERTIES[prop] == 'color':
            from mimesis.providers.text import Text
            text = Text('en', seed=42)
            assert len(value) == 7 and value.startswith('#')
        elif CSS_PROPERTIES[prop] == 'size':
            assert int(value[:-2]) > 0 and value[-2:] in CSS_SIZE_UNITS

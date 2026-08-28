# Module: mimesis.providers.text
# test_text.py
from mimesis import Text
import pytest

@pytest.fixture
def text_instance():
    return Text()

def test_color_default(text_instance):
    color = text_instance.color()
    assert isinstance(color, str), "Expected a string representation of a color"

def test_color_locale_seed(text_instance):
    locale = 'en'
    seed = 12345
    text_instance_localized = Text(locale=locale, seed=seed)
    color_localized = text_instance_localized.color()
    assert isinstance(color_localized, str), "Expected a string representation of a color"

def test_color_method_exists(text_instance):
    assert hasattr(text_instance, 'color'), "Expected the Text class to have a color method"

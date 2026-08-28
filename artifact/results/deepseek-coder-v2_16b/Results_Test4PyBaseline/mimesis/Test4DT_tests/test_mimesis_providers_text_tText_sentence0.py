
# Module: mimesis.providers.text
# test_mimesis_text.py
from mimesis.providers.text import Text
import pytest

@pytest.fixture
def text_generator():
    return Text(locale='en', seed=42)  # Corrected locale to 'en' which is a valid Locale

def test_initialization(text_generator):
    assert isinstance(text_generator, Text), "Instance should be an instance of the Text class"
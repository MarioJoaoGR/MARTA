
# Module: mimesis.providers.text
# test_text.py
from mimesis.providers.text import Text
import pytest

@pytest.fixture
def text_instance():
    return Text()

def test_word_default(text_instance):
    word = text_instance.word()
    assert isinstance(word, str), "Expected a string"
    assert len(word) > 0, "Expected a non-empty string"

def test_word_specific_locale_seed():
    with pytest.raises(ValueError):
        specific_locale_instance = Text(locale='en-US', seed=42)
        word_with_specifics = specific_locale_instance.word()
        assert isinstance(word_with_specifics, str), "Expected a string"
        assert len(word_with_specifics) > 0, "Expected a non-empty string"

def test_word_multiple_calls(text_instance):
    words = [text_instance.word() for _ in range(5)]
    unique_words = set(words)
    assert len(unique_words) >= 1, "Expected at least one unique word across multiple calls"

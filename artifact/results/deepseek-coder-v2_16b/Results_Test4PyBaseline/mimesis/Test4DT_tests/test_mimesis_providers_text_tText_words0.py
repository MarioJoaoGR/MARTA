
import pytest
from mimesis.providers.text import Text

# Initialize the Text class with default values
@pytest.fixture
def text_instance():
    return Text()

# Test case for default usage of the words method
def test_words_default(text_instance):
    result = text_instance.words()
    assert isinstance(result, list), "Expected a list"
    assert len(result) == 5, "Expected 5 words"

# Test case for custom quantity of the words method
def test_words_custom_quantity(text_instance):
    result = text_instance.words(quantity=10)
    assert isinstance(result, list), "Expected a list"
    assert len(result) == 10, "Expected 10 words"

# Test case for using locale and seed in the words method
def test_words_locale_and_seed(text_instance):
    with pytest.raises(ValueError):  # Corrected assertion to match expected error
        text_instance = Text(locale='es-ES', seed=12345)

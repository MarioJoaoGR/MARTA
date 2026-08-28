
from mimesis.providers import Text
import pytest

@pytest.fixture
def text_provider():
    return Text()

def test_quote_returns_a_random_quote(text_provider):
    quote = text_provider.quote()
    assert isinstance(quote, str), "Expected a string but got something else."
    assert len(quote) > 0, "The returned quote should not be empty."

def test_quote_returns_a_different_quote_each_time(text_provider):
    first_quote = text_provider.quote()
    second_quote = text_provider.quote()
    assert first_quote != second_quote, "Expected different quotes each time."

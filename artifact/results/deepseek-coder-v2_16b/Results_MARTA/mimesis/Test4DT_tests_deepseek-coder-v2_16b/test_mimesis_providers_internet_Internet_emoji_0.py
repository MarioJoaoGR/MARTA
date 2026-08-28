
import pytest
from mimesis.providers import Internet


def test_invalid_emoji():
    internet = Internet()
    
    # Mocking the random choice to raise an exception for testing purposes
    def mock_random_choice(*args, **kwargs):
        raise Exception("Mocked random choice error")
    
    with pytest.raises(Exception):
        with pytest.MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr('mimesis.providers.internet.Internet.random.choice', mock_random_choice)
            internet.emoji()
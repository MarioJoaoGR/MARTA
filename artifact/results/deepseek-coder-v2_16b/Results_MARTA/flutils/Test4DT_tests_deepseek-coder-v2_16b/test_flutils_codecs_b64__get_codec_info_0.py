
import pytest
from flutils.codecs.b64 import _get_codec_info
import codecs

# Define a constant NAME for testing
NAME = 'example_codec'

def decode(obj, **kwargs):
    return obj

def encode(obj, **kwargs):
    return obj

@pytest.fixture
def setup():
    yield  # Ensure the fixture is used as a context manager


def test_get_codec_info_does_not_match(setup):
    result = _get_codec_info('nonexistent_codec')
    assert result is None, "Expected None for a non-matching codec name"

import pytest
from flutils.codecs.raw_utf8_escape import _get_codec_info, NAME
import codecs


def test_none_input():
    # Test when the input name does not match any codec
    result = _get_codec_info('non_matching_name')
    assert result is None

def test_invalid_input():
    # Test with an invalid input type (should return None)
    result = _get_codec_info(12345)  # Invalid input type
    assert result is None
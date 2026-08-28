
import pytest
from flutils.codecs.raw_utf8_escape import _get_codec_info, NAME, encode, decode
import codecs

def test_valid_codec_name():
    # Test when the codec name matches the expected NAME constant
    result = _get_codec_info(NAME)
    assert isinstance(result, codecs.CodecInfo), f"Expected a codecs.CodecInfo object but got {type(result)}"
    assert result.name == NAME, f"Expected codec name to be '{NAME}' but got '{result.name}'"
    assert callable(result.encode) and hasattr(result.encode, '__call__'), "Expected encode function to be callable"
    assert callable(result.decode) and hasattr(result.decode, '__call__'), "Expected decode function to be callable"

def test_invalid_codec_name():
    # Test when the codec name does not match any expected NAME constant
    result = _get_codec_info('non_matching_name')
    assert result is None, f"Expected None but got {result}"

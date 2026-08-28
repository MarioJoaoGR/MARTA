
import pytest
import codecs
from flutils.codecs import register_codecs

# Assuming NAME is defined somewhere in the module, for example:
NAME = 'raw_utf8_escape'

def test_register_codec():
    # Test that the codec is registered correctly
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
    
    register_codecs()
    
    assert callable(codecs.getdecoder(NAME))

def test_encode_decode():
    register_codecs()
    
    # Test encoding and decoding with the custom codec
    encoded = 'test©'.encode('raw_utf8_escape')
    decoded = b'test\xc2\xa9'.decode('raw_utf8_escape')
    
    assert encoded == b'test\\xc2\\xa9'
    assert decoded == 'test©'

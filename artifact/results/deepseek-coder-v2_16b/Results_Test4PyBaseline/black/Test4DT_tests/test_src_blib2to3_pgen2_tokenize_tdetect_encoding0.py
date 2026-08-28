
import pytest
from io import BytesIO
from typing import Callable, List, Tuple
from blib2to3.pgen2.tokenize import detect_encoding

def test_detect_encoding_with_utf8_bom():
    def readline():
        return b'\xef\xbb\xbf' + b"print('Hello, World!')"
    
    f = BytesIO(b'')
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8-sig', "Expected 'utf-8-sig' as the detected encoding."
    assert len(lines) == 1, "Expected only one line to be read."

def test_detect_encoding_with_invalid_charset():
    def readline():
        return b"# coding: invalid-charset\nprint('Hello, World!')"
    
    f = BytesIO(b'')
    with pytest.raises(SyntaxError):
        detect_encoding(readline)

def test_detect_encoding_without_bom_or_cookie():
    def readline():
        return b"print('Hello, World!')"
    
    f = BytesIO(b'')
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8', "Expected default to utf-8 when no BOM or cookie is present."
    assert len(lines) == 1, "Expected only one line to be read."

def test_detect_encoding_with_valid_cookie():
    def readline():
        return b"# coding: ascii\nprint('Hello, World!')"
    
    f = BytesIO(b'')
    encoding, lines = detect_encoding(readline)
    assert encoding == 'ascii', "Expected 'ascii' as the detected encoding from the cookie."
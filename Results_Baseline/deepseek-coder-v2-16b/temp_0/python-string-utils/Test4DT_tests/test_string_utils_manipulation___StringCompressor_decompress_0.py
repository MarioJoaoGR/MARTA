
import pytest
from string_utils import manipulation as sm
import zlib
import base64

def test_decompress_default_encoding():
    # Arrange
    input_string = "example"
    compressed = base64.urlsafe_b64encode(zlib.compress(input_string.encode('utf-8'))).decode('utf-8').replace('=', '')
    
    # Act
    result = sm.decompress(compressed)
    
    # Assert
    assert result == input_string, f"Expected decompressed string to be '{input_string}', but got '{result}'"

def test_decompress_specified_encoding():
    # Arrange
    input_string = "example"
    compressed = base64.urlsafe_b64encode(zlib.compress(input_string.encode('utf-8'))).decode('utf-8').replace('=', '')
    
    # Act
    result = sm.decompress(compressed, 'utf-8')
    
    # Assert
    assert result == input_string, f"Expected decompressed string to be '{input_string}', but got '{result}'"

def test_decompress_empty_input():
    # Arrange
    input_string = ""
    
    # Act & Assert
    with pytest.raises(ValueError) as e:
        sm.decompress(input_string)

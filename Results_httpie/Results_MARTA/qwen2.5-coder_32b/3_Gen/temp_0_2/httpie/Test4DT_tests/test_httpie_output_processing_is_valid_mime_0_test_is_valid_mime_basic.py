
import re
from unittest.mock import patch
from httpie.output.processing import is_valid_mime, MIME_RE

def test_is_valid_mime_basic():
    # Test valid MIME types
    assert is_valid_mime("image/png")  # Returns True
    assert is_valid_mime("text/html")  # Returns True
    assert is_valid_mime("application/pdf")  # Returns True
    
    # Test invalid MIME types
    assert not is_valid_mime("invalid-mime")  # Returns False

# Mock the MIME_RE pattern for testing
@patch('httpie.output.processing.MIME_RE', re.compile(r'^[a-zA-Z]+\/[a-zA-Z]+$'))
def test_is_valid_mime_with_mocked_pattern():
    # Test valid MIME types with mocked pattern
    assert is_valid_mime("image/png")  # Returns True
    assert is_valid_mime("text/html")  # Returns True
    assert is_valid_mime("application/pdf")  # Returns True
    
    # Test invalid MIME types with mocked pattern
    assert not is_valid_mime("invalid-mime")  # Returns False


import re
from httpie.downloads import ContentRangeError, parse_content_range
import pytest

def test_invalid_input():
    with pytest.raises(ContentRangeError):
        # Test case for invalid input where content_range is None
        parse_content_range(None, 0)
    
    with pytest.raises(ContentRangeError):
        # Test case for invalid input where content_range format is incorrect
        parse_content_range("invalid format", 0)
    
    with pytest.raises(ContentRangeError):
        # Test case for invalid input where first_byte_pos > last_byte_pos
        parse_content_range("bytes 47022-21010/47022", 21010)

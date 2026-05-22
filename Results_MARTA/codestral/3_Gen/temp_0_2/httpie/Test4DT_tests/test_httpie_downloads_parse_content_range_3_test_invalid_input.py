
import re
from httpie.downloads import ContentRangeError, parse_content_range
import pytest

def test_invalid_input():
    with pytest.raises(ContentRangeError):
        # Test case for invalid input where the content range is None
        parse_content_range(None, 0)

    with pytest.raises(ContentRangeError):
        # Test case for invalid input where the content range format is incorrect
        parse_content_range("invalid format", 0)

    with pytest.raises(ContentRangeError):
        # Test case for invalid input where first byte position is greater than last byte position
        parse_content_range("bytes 47022-21010/47022", 0)

    with pytest.raises(ContentRangeError):
        # Test case for invalid input where instance length is less than or equal to last byte position
        parse_content_range("bytes 0-100/99", 0)

    with pytest.raises(ContentRangeError):
        # Test case for invalid input where the content range does not match the requested range
        parse_content_range("bytes 21010-47021/47022", 0)

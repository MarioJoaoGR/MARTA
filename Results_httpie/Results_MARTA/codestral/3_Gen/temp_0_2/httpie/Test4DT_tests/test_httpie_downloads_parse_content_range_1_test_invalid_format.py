
import re
from httpie.downloads import ContentRangeError, parse_content_range
import pytest

def test_invalid_format():
    with pytest.raises(ContentRangeError):
        # Test an invalid format for the Content-Range header
        parse_content_range("bytes 47022-21010/47022", 21010)


import re
from httpie.downloads import ContentRangeError, parse_content_range

def test_missing_input():
    content_range = None
    resumed_from = 0
    
    try:
        result = parse_content_range(content_range, resumed_from)
    except ContentRangeError as e:
        assert str(e) == 'Missing Content-Range'
    else:
        assert False, "Expected ContentRangeError but no exception was raised"

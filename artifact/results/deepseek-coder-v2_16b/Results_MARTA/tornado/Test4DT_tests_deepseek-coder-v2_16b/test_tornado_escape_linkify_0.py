
import pytest
from tornado.escape import linkify

def test_valid_input_with_shorten_and_extra_params():
    text = 'Check out our website at http://example.com and https://www.facebook.com.'
    expected = 'Check out our website at <a href="http://example.com" class="external" rel="nofollow">http://example.com</a> and <a href="https://www.facebook.com" class="external" rel="nofollow">https://www.facebook.com</a>.'
    assert linkify(text, shorten=True, extra_params='class="external" rel="nofollow"') == expected

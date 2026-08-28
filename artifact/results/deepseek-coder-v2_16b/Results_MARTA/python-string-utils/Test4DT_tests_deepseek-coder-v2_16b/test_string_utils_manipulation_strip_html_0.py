
import pytest
from string_utils.manipulation import strip_html, InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

class TestStripHtml:
    
    def test_valid_input(self):
        assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
        assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    
    def test_invalid_input(self):
        with pytest.raises(InvalidInputError):
            strip_html(None)
    
    def test_keep_tag_content_false(self):
        assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
        assert strip_html('<b>bold text</b>', keep_tag_content=False) == ''
    
    def test_keep_tag_content_true(self):
        assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
        assert strip_html('<b>bold text</b>', keep_tag_content=True) == 'bold text'

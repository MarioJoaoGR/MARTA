
import pytest
from string_utils.manipulation import strip_html

def test_strip_html_no_tags():
    """Test stripping HTML from a string with no tags."""
    result = strip_html('This is a plain text.')
    assert result == 'This is a plain text.'



def test_strip_html_with_attributes():
    """Test stripping an HTML tag with attributes but no content."""
    result = strip_html('<img src="image.jpg" alt="">')
    assert result == ''

def test_strip_html_empty_string():
    """Test stripping HTML from an empty string."""
    result = strip_html('')
    assert result == ''

def test_strip_html_keep_tag_content():
    """Test keeping the content within HTML tags."""
    result = strip_html('<a href="foo/bar">click here</a>', keep_tag_content=True)
    assert result == 'click here'

def test_strip_html_multiple_tags_keep_content():
    """Test keeping the content within multiple HTML tags."""
    result = strip_html('<p>This is a <strong>bold</strong> paragraph.</p>', keep_tag_content=True)
    assert result == 'This is a bold paragraph.'
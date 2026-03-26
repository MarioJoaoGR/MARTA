# Module: string_utils.validation
import pytest
from string_utils.validation import is_slug

# Test cases for the is_slug function
def test_is_slug_valid():
    assert is_slug('my-blog-post-title') == True
    assert is_slug('my-1st-blog-post') == True
    assert is_slug('a-b-c-d-e-f-g') == True

def test_is_slug_invalid():
    assert is_slug('My blog post title') == False
    assert is_slug('my-Blog-Post-Title') == False
    assert is_slug('my-blog-post-title!') == False
    assert is_slug('') == False
    assert is_slug(None) == False

def test_is_slug_with_separator():
    assert is_slug('my-blog-post-title', separator='.') == False
    assert is_slug('my.blog.post.title', separator='.') == True

def test_is_slug_empty_string():
    assert is_slug('') == False

def test_is_slug_none():
    assert is_slug(None) == False

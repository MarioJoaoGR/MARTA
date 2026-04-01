
import pytest
from string_utils.manipulation import slugify

def test_valid_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Hello World!') == 'hello-world'
    assert slugify('This is a test string.') == 'this-is-a-test-string'
    assert slugify('1234567890') == '1234567890'

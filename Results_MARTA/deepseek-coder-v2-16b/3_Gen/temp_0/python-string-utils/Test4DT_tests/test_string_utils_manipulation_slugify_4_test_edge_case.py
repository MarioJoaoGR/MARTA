
import pytest
from string_utils.manipulation import slugify

def test_edge_case():
    # Test case for edge cases such as non-ASCII characters, multiple spaces, etc.
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('This is a test with multiple   spaces') == 'this-is-a-test-with-multiple-spaces'
    assert slugify('Hello, World!') == 'hello-world'
